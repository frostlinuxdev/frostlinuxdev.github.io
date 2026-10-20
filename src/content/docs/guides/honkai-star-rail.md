---
title: "How to Play Honkai: Star Rail on Linux"
description: "Run Honkai: Star Rail on Linux with a community launcher and the DW-Proton (Dawn Winery) runner installed through Proton Plus."
wip: true
game: "Honkai: Star Rail"
sidebar:
  label: "Honkai: Star Rail"
image: "/images/honkai-star-rail/thumb.webp"
rating: "out-of-the-box"
status: "works"
launcher: "twintail"
protonVersion: "DW-Proton (Dawn Winery) latest"
launcherName: "Honkers Railway Launcher"
onSteam: false
website: "https://hsr.hoyoverse.com/"
tags: ["honkai-star-rail", "gacha"]
---

> **Works.** Tested on Linux with the **DW-Proton (Dawn Winery)** runner through the Honkers Railway Launcher. No video yet.

Honkai: Star Rail runs on Linux through a community launcher that automates the Wine setup — the same approach as the Genshin Impact and Zenless Zone Zero guides. Run it with the **DW-Proton (Dawn Winery)** runner. **TwintailLauncher** is a viable alternative that also supports Star Rail.

## What you need

| Item | Notes |
|------|-------|
| **Honkers Railway Launcher** | [Flathub](https://flathub.org/en/apps/moe.launcher.the-honkers-railway-launcher) · [GitHub](https://github.com/an-anime-team/the-honkers-railway-launcher) |
| **Proton Plus** | Downloads the DW-Proton (Dawn Winery) runner |
| **Free disk space** | Enough for the full game download |

You can also install Honkai: Star Rail with **[TwintailLauncher](https://flathub.org/en/apps/app.twintaillauncher.ttl)** ([GitHub](https://github.com/TwintailTeam/TwintailLauncher)).

## Steps

1. Install your launcher of choice — **Honkers Railway Launcher** or **TwintailLauncher**.
2. Open **Proton Plus**, select **Steam** (or the launcher you are targeting), and download the latest **DW-Proton (Dawn Winery)**.
3. Point the launcher at the DW-Proton runner in its runner or compatibility settings.
4. Download Honkai: Star Rail and let the launcher install the Wine components when asked.
5. Launch the game and sign in.

## Troubleshooting

- **The launcher or game does not start:** update your GPU drivers and Vulkan packages, then try a fresh prefix.
- **Stutter on the first run:** let shaders compile — the first few minutes are usually the worst.

## Frequently asked questions

**Do I need Windows to play this on Linux?**
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**Which launcher should I use?**
Honkers Railway Launcher is built for Star Rail. TwintailLauncher is a good general alternative if you play several HoYo games.

**Which runner should I use?**
DW-Proton (Dawn Winery), downloaded with Proton Plus. It is the build most likely to work for HoYo titles.
