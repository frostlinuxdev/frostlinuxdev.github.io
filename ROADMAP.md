# FrostLinux site — roadmap / TODO

Later ideas and known loose ends. Not built yet.

## New pages to add

**Trust / explainer** (highest value now the site is public)

1. **How we test & rate** (`/how-we-test/`)
   - The test rig: RTX 3060 12GB, CachyOS, driver/Proton versions.
   - What each verdict means: `Works`, `Out of the box`, `Custom Proton`, `Untested`.
   - How the derived rating works and when it is overridden by hand.
   - How/when the **"ProtonDB says it works"** badge is shown (untested, platinum/gold/silver only).
2. **Getting started** (`/getting-started/`)
   - Short jargon-free primer: Flatpak, Proton, [ProtonPlus](https://flathub.org/en/apps/com.vysp3r.ProtonPlus), launchers.
   - Everything the individual guides assume. Link to it from guide intros.
3. **Launchers compared** (`/launchers/`)
   - Steam vs Heroic vs Faugus vs Lutris vs game-specific launchers.
   - Game-specific: AAGL (`moe.launcher.an-anime-game-launcher`), Honkers (`moe.launcher.honkers-launcher`),
     Sleepy (`moe.launcher.sleepy-launcher`), Honkers Railway (`moe.launcher.the-honkers-railway-launcher`),
     TwintailLauncher (`app.twintaillauncher.ttl`).
   - Which launcher to pick, and when.

**Community / reach**

4. **FAQ** (`/faq/`) — "will I get banned?", anti-cheat, cross-save, is it safe, why custom Proton.
5. **Android gacha on Linux (Waydroid)** (`/waydroid/`) — FGO + multi-instance; the channel already has videos for this.
6. **Known issues / blocked games** (`/known-issues/`) — kernel anti-cheat titles and any workarounds.
7. **Changelog** (`/changelog/`).
8. **Contribute / report a result** (`/contribute/`).

## Guide consistency

- Roll the **Screenshots** gallery (`.shot-grid`) + linked Steam capsule (`.store-shot`) out to the
  popular guides: Genshin, ZZZ, Wuthering Waves, HSR, HI3, NIKKE, etc. See
  `guides/arknights-endfield.md` for the pattern.

## Loose ends

- **Publish drafts** when ready — most guides are still `draft: true` (only a handful are live), so decide on a
  publish order. `draft: true` keeps a guide off the production build but visible on dev.
- **GFL2 rating** — currently "Out of the box" + launcher `steam`, but its primary guide method is the Lutris
  HaoPlay script. Owner decision.
- Add `ttl`/launcher tags to ZZZ/HSR/HI3 to match Genshin.
- Optional: enable linger / root systemd path units on `.45` for instant deploys (cron is a 1-min fallback).
