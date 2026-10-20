# FrostLinux

Linux gaming guides for gacha games — Proton, Heroic, Steam and community launchers.

Built with [Astro](https://astro.build) + [Starlight](https://starlight.astro.build).

## Branches

| Branch | Purpose |
| ------ | ------- |
| `main` | Full site — every tracked game, the Nadare page and the gameplay page. |
| `launch` | Launch-ready subset — only guides flagged `launch = true`, without the Nadare or gameplay pages. |

`main` deploys to GitHub Pages via `.github/workflows/deploy.yml`.

```bash
git checkout launch   # switch to the launch variant
```

## Quick start

```bash
npm ci
npm run dev     # http://localhost:4321
npm run build   # -> dist/
npm run preview
```

## Adding a game guide

Create `src/content/docs/guides/<slug>.md`. Front matter drives the compatibility
table on `/games/` and the homepage grid — a guide only shows up there when `game`
is set.

| Field | Notes |
| ----- | ----- |
| `game` | Display name. Required for the entry to appear in the game lists. |
| `status` | `works`, `untested`, `drafted-from-video`, `needs-fix` or `broken`. |
| `launcher` | `steam`, `heroic`, `faugus`, `lutris`, `twintail`, `heroic-or-faugus` or `""`. |
| `onSteam` | Whether the game is on Steam. |
| `image` | Card image (16:9), relative to `public/` (e.g. `/images/nikke/thumb.webp`). |
| `heroImage` | Optional wide banner shown at the top of the guide page (e.g. `/images/nikke/hero.webp`). |
| `steamAppId` | Steam app id — enables the ProtonDB button, the "ProtonDB says it works" badge and the `scripts/fetch-images.py` art pull. |
| `nadare` | Shows the Nadare beta badge/callout. |
| `draft` | `true` hides the page from production builds. |

Multi-launcher guides use a folder — the `index` is the hub and the sub-pages are
separate guides. Put `game:` on the hub only, so the lists show one card:

```
src/content/docs/guides/chaos-zero-nightmare/
├── index.mdx    # hub (has `game:`)
├── faugus.md    # sub-page (no `game:`)
└── heroic.md
```

## Images

Cards are 16:9 WebP. Two helpers fetch art (both idempotent; `--force` to overwrite):

- `scripts/fetch-images.py <image-dir> <steam-appid> [--name "Game Name"]` — official
  art. Prefers **SteamGridDB** (public endpoint, no key) for a curated 1920x620 hero
  plus a 920x430 card, then falls back to Steam's `library_hero` / `background_raw`.
  Pass `none` as the appid for games that are not on Steam, and `--no-sgdb` to use
  Steam art only. Writes `hero.webp` (banner) and `thumb.webp` (16:9 card).
- `scripts/fetch-thumbs.py <slug> <youtube-id>` — YouTube thumbnail fallback for
  games that are not on Steam.

## Adding news

Create `src/content/docs/news/<slug>.md`:

```markdown
---
title: "Arknights: Endfield is now on Steam"
description: "One-line summary shown on the news list."
date: 2026-10-16
draft: true
---

Body goes here.
```

It appears automatically on `/news/`, newest first. Don't set `game:` on news
posts.

## Site configuration

Site-wide links (Discord, GitHub, YouTube, Nadare) live in
`src/site.config.mjs`. Legacy URL redirects live in `redirects.json`.
