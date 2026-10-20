#!/usr/bin/env python3
"""Fetch a YouTube thumbnail and store it as an optimized WebP card image.

The compatibility cards and guide hero images are sourced from our own YouTube
video thumbnails (1280x720). This script downloads one and converts it with
cwebp so the repo only carries small WebP files.

Usage:
  scripts/fetch-thumbs.py <game-slug> <video-id> [--force]
  scripts/fetch-thumbs.py --list thumbs.tsv        # lines: <game-slug>\t<video-id>

Writes public/images/<game-slug>/thumb.webp. Idempotent unless --force is given.
Requires: cwebp (webp package).
"""
import os
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(ROOT, "public", "images")
QUALITY = "85"


def download(video_id, dest):
    for name in ("maxresdefault", "sddefault", "hqdefault"):
        url = f"https://i.ytimg.com/vi/{video_id}/{name}.jpg"
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = r.read()
            if len(data) > 1000:
                with open(dest, "wb") as f:
                    f.write(data)
                return name
        except Exception:
            continue
    raise SystemExit(f"could not download a thumbnail for {video_id}")


def convert(src, out):
    cmd = ["cwebp", "-quiet", "-q", QUALITY, "-m", "6", "-resize", "1280", "0", src, "-o", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"cwebp failed for {src}: {r.stderr.strip()}")


def fetch(slug, video_id, force=False):
    outdir = os.path.join(IMAGES, slug)
    out = os.path.join(outdir, "thumb.webp")
    if os.path.exists(out) and not force:
        print(f"SKIP  {slug} (exists: {out})")
        return
    os.makedirs(outdir, exist_ok=True)
    tmp = os.path.join(outdir, ".thumb.src.jpg")
    name = download(video_id, tmp)
    convert(tmp, out)
    os.remove(tmp)
    print(f"OK    {slug}  {video_id} ({name}) -> {os.path.relpath(out, ROOT)}  {os.path.getsize(out)} bytes")


def main():
    args = sys.argv[1:]
    force = "--force" in args
    args = [a for a in args if a != "--force"]
    if not args:
        raise SystemExit(__doc__)
    if args[0] == "--list":
        if len(args) < 2:
            raise SystemExit("--list needs a tsv path")
        for line in open(args[1]):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            slug, _, vid = line.partition("\t")
            fetch(slug.strip(), vid.strip(), force)
        return
    slug, vid = args[0], args[1]
    fetch(slug, vid, force)


if __name__ == "__main__":
    main()
