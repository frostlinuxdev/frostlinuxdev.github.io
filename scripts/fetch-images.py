#!/usr/bin/env python3
"""Fetch official game art for a guide: wide hero + 16:9 card image.

Sources, in order:
  1. SteamGridDB (curated community art, no API key needed — uses its public
     endpoint). Looks the game up by name and prefers a 1920x620/3840x1240 hero.
  2. Steam: legacy library_hero.jpg (1920x620), then the appdetails
     background_raw/background (16:9).

Usage:
  scripts/fetch-images.py <image-dir> <steam-appid> [--name "Game Name"]
  scripts/fetch-images.py <image-dir> none --name "Game Name"      # non-Steam
  scripts/fetch-images.py --list images.tsv                        # dir<TAB>appid<TAB>name

Options: --force (overwrite), --no-thumb (skip the card), --no-sgdb (Steam only).
Writes <dir>/hero.webp (wide) and, unless --no-thumb, <dir>/thumb.webp (16:9 1280x720).
Requires ImageMagick (convert).
"""
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(ROOT, "public", "images")
LEGACY = "https://cdn.cloudflare.steamstatic.com/steam/apps/{app}/{file}"
STEAM_API = "https://store.steampowered.com/api/appdetails?appids={app}&cc=us&l=en"
SGDB = "https://www.steamgriddb.com/api/public"
UA = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
MIN_KB, MIN_W = 40, 1100


def http(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read()
    except Exception:
        return None


def http_json(url, body=None):
    req = urllib.request.Request(url, headers=UA, data=json.dumps(body).encode() if body else None)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except Exception:
        return None


# ---------------------------------------------------------------- SteamGridDB
def sgdb_assets(game_id, asset_type, dimensions=None, styles=None, languages=None):
    body = {
        "static": True, "animated": False, "humor": False, "nsfw": False,
        "epilepsy": False, "untagged": True, "asset_type": asset_type,
        "limit": 24, "order": "score_desc", "dimensions": dimensions or ["all"],
        "styles": styles or ["all"], "languages": languages or ["all"], "mime": ["all"],
        "game_id": [game_id], "page": 0,
    }
    d = http_json(f"{SGDB}/search/assets", body)
    if not d or not d.get("success"):
        return []
    return d["data"].get("assets") or []


SGDB_ALIASES = {
    "Star Saviour": "StarSavior",
}


def sgdb_candidates(name):
    """SGDB game ids for a name, best text match first (only close matches)."""
    query = SGDB_ALIASES.get(name, name)
    q = http_json(f"{SGDB}/search/autocomplete?term={urllib.parse.quote(query)}")
    target = _norm(query)
    scored = []
    for e in (q or {}).get("data", []) or []:
        n = _norm(e.get("name") or "")
        if not n:
            continue
        if n == target:
            s = 0
        elif n.startswith(target) or target.startswith(n):
            s = 1
        elif (target in n or n in target) and min(len(n), len(target)) / max(len(n), len(target)) >= 0.75:
            s = 2
        else:
            s = 3
        if s <= 2:
            scored.append((s, e["id"]))
    scored.sort(key=lambda x: x[0])
    return [gid for _, gid in scored]


ROMAN = {"ii": "2", "iii": "3", "iv": "4"}


def _norm(s):
    s = s.lower()
    s = re.sub(r"\b(ii|iii|iv)\b", lambda m: ROMAN[m.group(1)], s)
    return re.sub(r"[^a-z0-9]", "", s)


def sgdb_first(ids, asset_type, dimensions=None, languages=None):
    for gid in ids:
        for a in sgdb_assets(gid, asset_type, dimensions, languages=languages):
            if a.get("url"):
                return a["url"]
    return None


# ------------------------------------------------------------------- helpers
def dims(path):
    r = subprocess.run(["identify", "-format", "%w %h", path], capture_output=True, text=True)
    return tuple(map(int, r.stdout.split())) if r.returncode == 0 else (0, 0)


def is_real(path):
    return os.path.exists(path) and os.path.getsize(path) >= MIN_KB * 1024 and dims(path)[0] >= MIN_W


def write_bytes(data, path):
    with open(path, "wb") as f:
        f.write(data)


def convert(src, out, *args):
    r = subprocess.run(["convert", src, *args, "-quality", "85", out], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"convert failed for {src}: {r.stderr.strip()}")


def download_to(url, path):
    data = http(url)
    if not data or len(data) < 1024:
        return None
    write_bytes(data, path)
    return path


def appdata(appid):
    raw = http(STEAM_API.format(app=appid))
    if not raw:
        return {}
    try:
        return json.loads(raw).get(str(appid), {}).get("data") or {}
    except Exception:
        return {}


# --------------------------------------------------------------------- main
def fetch(directory, appid, name=None, force=False, thumb=True, sgdb=True,
          hero_url=None, card_url=None, lang=None):
    outdir = os.path.join(IMAGES, directory)
    os.makedirs(outdir, exist_ok=True)
    hero = os.path.join(outdir, "hero.webp")
    card = os.path.join(outdir, "thumb.webp")
    if os.path.exists(hero) and not force:
        print(f"SKIP  {directory} (exists: {os.path.relpath(hero, ROOT)})")
        return

    name = name or directory.replace("-", " ").title()
    src_dir = outdir
    hero_src = card_src = None
    origin = []
    langs = [lang] if lang else None

    if hero_url:
        hero_src = download_to(hero_url, os.path.join(src_dir, ".manual-hero"))
        origin.append("manual")
    if card_url:
        card_src = download_to(card_url, os.path.join(src_dir, ".manual-card"))

    # 1) SteamGridDB
    if not hero_src and sgdb:
        cands = sgdb_candidates(name)
        h = sgdb_first(cands, "hero", languages=langs)
        if h:
            hero_src = download_to(h, os.path.join(src_dir, ".sgdb-hero"))
            g = sgdb_first(cands, "grid", ["920x430"], languages=langs)
            if g:
                card_src = download_to(g, os.path.join(src_dir, ".sgdb-card"))
            origin.append("sgdb")

    # 2) Steam fallback
    data = appdata(appid) if appid and appid.isdigit() else {}
    if not hero_src:
        hero_src = None
        for url in [LEGACY.format(app=appid, file="library_hero.jpg"),
                    (data.get("background_raw") or ""), (data.get("background") or "")]:
            if url:
                p = download_to(url, os.path.join(src_dir, ".steam-hero"))
                if p and is_real(p):
                    hero_src = p
                    break
        if hero_src:
            origin.append("steam")

    if not hero_src:
        print(f"WARN  {directory}: no art found (name={name!r}, app={appid})")
        return

    if not card_src:
        card_src = hero_src

    convert(hero_src, hero, "-resize", "1920x")
    if thumb:
        convert(card_src, card, "-resize", "1280x720^", "-gravity", "center", "-extent", "1280x720")

    for f in os.listdir(outdir):
        if f.startswith(".sgdb-") or f.startswith(".steam-") or f.startswith(".manual-"):
            os.remove(os.path.join(outdir, f))

    made = [os.path.relpath(hero, ROOT)] + ([os.path.relpath(card, ROOT)] if thumb else [])
    print(f"OK    {directory}  [{'+'.join(origin) or 'n/a'}] -> {', '.join(made)}")


def main():
    args = sys.argv[1:]
    force = "--force" in args
    thumb = "--no-thumb" not in args
    sgdb = "--no-sgdb" not in args

    def opt(flag):
        if flag in args:
            i = args.index(flag)
            val = args[i + 1]
            del args[i:i + 2]
            return val
        return None

    name = opt("--name")
    hero_url = opt("--hero-url")
    card_url = opt("--card-url")
    lang = opt("--lang")

    if "--list" in args:
        lstfile = args[args.index("--list") + 1]
        for line in open(lstfile):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split("\t")]
            directory, appid = parts[0], parts[1]
            nm = parts[2] if len(parts) > 2 else None
            fetch(directory, appid, nm, force, thumb, sgdb)
        return
    args = [a for a in args if not a.startswith("--")]
    if not args:
        raise SystemExit(__doc__)
    fetch(args[0], args[1], name, force, thumb, sgdb, hero_url, card_url, lang)


if __name__ == "__main__":
    main()
