---
title: "How to Play Genshin Impact on Linux"
description: "Install Genshin Impact on Linux with the An Anime Game Launcher, which sets up Wine and Proton for you. Login, updates and troubleshooting covered."
game: "Genshin Impact"
sidebar:
  label: "Genshin Impact"
image: "/images/genshin-impact/thumb.webp"
rating: "out-of-the-box"
status: "works"
launcher: "twintail"
protonVersion: ""
launcherName: "An Anime Game Launcher (AAGL)"
hasGameplayVideo: true
gameplay:
  - id: "rPzDdPKatUg"
    title: "Genshin Impact gameplay, RTX 3060 12GB, CachyOS, 1440p max"
onSteam: false
website: "https://genshin.hoyoverse.com/"
tags: ["genshin-impact", "gacha", "aagl", "ttl"]
---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/VLeBCcRKdJ4" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

Genshin Impact can be installed on Linux with a community launcher that automates the Wine/Proton setup, so you do not configure a runner by hand.

## What you need

| Item | Notes |
|------|-------|
| **An Anime Game Launcher** | [Flathub](https://flathub.org/en/apps/moe.launcher.an-anime-game-launcher) · [GitHub](https://github.com/an-anime-team/an-anime-game-launcher) |
| **Free disk space** | The download fails if the drive is too full |
| Flathub enabled | Needed on some distros such as Fedora |

You can also install Genshin Impact with **[TwintailLauncher](https://flathub.org/en/apps/app.twintaillauncher.ttl)** ([GitHub](https://github.com/TwintailTeam/TwintailLauncher)), a general launcher for several HoYo games.

## Steps

1. Install the launcher from Flathub (search "anime game launcher"), the AUR, or the GitHub terminal command.
2. Open it and continue through the first-run setup. The defaults are fine, and every folder can be changed.
3. Let it install Wine Mono when asked, then restart the launcher.
4. Press **Download** and wait for the game to finish.
5. Check the settings (FSR, presets, MangoHud, FPS unlock) if you want, then press **Launch**.

## Troubleshooting

- **Download failed:** free up disk space and try again.

## Gameplay

<div class="gameplay-grid"><figure><iframe src="https://www.youtube.com/embed/rPzDdPKatUg" title="Genshin Impact gameplay, RTX 3060 12GB, CachyOS, 1440p max" loading="lazy" allowfullscreen></iframe><figcaption>Genshin Impact gameplay, RTX 3060 12GB, CachyOS, 1440p max</figcaption></figure></div>

## Frequently asked questions

**Do I need Windows to play this on Linux?**  
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**The game does not start. What should I try first?**  
Update your GPU drivers and Vulkan packages, try the newest Proton-GE, and create a fresh prefix if the old one may be corrupted.
