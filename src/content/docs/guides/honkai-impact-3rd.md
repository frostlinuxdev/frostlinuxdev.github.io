---
title: "How to Play Honkai Impact 3rd on Linux"
description: "Run Honkai Impact 3rd on Linux with the Honkers Launcher and DW-Proton installed through ProtonPlus. TwintailLauncher is a viable alternative."
wip: true
game: "Honkai Impact 3rd"
sidebar:
  label: "Honkai Impact 3rd"
image: "/images/honkai-impact-3rd/thumb.webp"
rating: "out-of-the-box"
status: "works"
launcher: "twintail"
protonVersion: "DW-Proton (Dawn Winery) latest"
launcherName: "Honkers Launcher"
onSteam: false
website: "https://honkaiimpact3.hoyoverse.com/"
protondbTier: "bronze"
tags: ["honkai-impact-3rd", "gacha"]
---

> **Works.** Played on Linux through the **Honkers Launcher** with the **DW-Proton (Dawn Winery)** runner.

Honkai Impact 3rd runs on Linux through the **Honkers Launcher**, a community launcher that automates the Wine setup — the same family of launchers used for the Genshin Impact, Zenless Zone Zero and Honkai: Star Rail guides. Run it with the **DW-Proton (Dawn Winery)** runner. **TwintailLauncher** is a viable alternative for both.

> **Use the Hoyoverse client, not the Steam version.** The Steam app is not the build most people play (different account/progression handling and a worse history under Proton); install through the [official launcher](https://honkaiimpact3.hoyoverse.com/) and the Honkers Launcher instead.

## What you need

| Item | Notes |
|------|-------|
| **Honkers Launcher** | [Flathub](https://flathub.org/en/apps/moe.launcher.honkers-launcher) · [GitHub](https://github.com/an-anime-team/honkers-launcher) |
| **Proton Plus** | Downloads the DW-Proton (Dawn Winery) runner |
| **Free disk space** | Enough for the full game download |

You can also install Honkai Impact 3rd with **[TwintailLauncher](https://flathub.org/en/apps/app.twintaillauncher.ttl)** ([GitHub](https://github.com/TwintailTeam/TwintailLauncher)).

## Steps

1. Install the **Honkers Launcher** (or **TwintailLauncher**).
2. Open **Proton Plus**, select the target launcher, and download the latest **DW-Proton (Dawn Winery)**.
3. Point the launcher at the DW-Proton runner in its runner or compatibility settings.
4. Download Honkai Impact 3rd and let the launcher install the Wine components when asked.
5. Launch the game and sign in.

## Troubleshooting

- **The launcher or game does not start:** update your GPU drivers and Vulkan packages, then try a fresh prefix.
- **Stutter on the first run:** let shaders compile — the first few minutes are usually the worst.

## Frequently asked questions

**Do I need Windows to play this on Linux?**
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**Which launcher should I use?**
Honkers Launcher is built for Honkai Impact 3rd. TwintailLauncher is a good general alternative if you play several HoYo games.

**Which runner should I use?**
DW-Proton (Dawn Winery), downloaded with Proton Plus. It is the build most likely to work for HoYo titles.
