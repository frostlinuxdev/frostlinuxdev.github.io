---
title: "How to Play Zenless Zone Zero on Linux"
description: "Run Zenless Zone Zero on Linux with a community launcher (Sleepy Launcher or TwintailLauncher) that handles the Wine setup, the same way as Genshin Impact."
game: "Zenless Zone Zero"
sidebar:
  label: "Zenless Zone Zero"
image: "/images/zenless-zone-zero/thumb.webp"
heroImage: "/images/zenless-zone-zero/hero.webp"
status: "works"
launcher: "twintail"
protonVersion: "Proton (default)"
rating: "custom-proton"
launcherName: "Sleepy Launcher"
hasGameplayVideo: true
onSteam: true
website: "https://zenless.hoyoverse.com/"
steamAppId: 4162040
protondbTier: "gold"
steamUrl: "https://store.steampowered.com/app/4162040/"
tags: ["zenless-zone-zero", "gacha"]
---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/E2I6Yv9HRF0" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

Zenless Zone Zero installs on Linux through a community launcher that handles the Wine setup, the same way as the Genshin Impact guide.

## What you need

| Item | Notes |
|------|-------|
| **Sleepy Launcher** | [Flathub](https://flathub.org/en/apps/moe.launcher.sleepy-launcher) · [GitHub](https://github.com/an-anime-team/sleepy-launcher) |
| **Free disk space** | Enough for the full game download |

You can also install Zenless Zone Zero with **[TwintailLauncher](https://flathub.org/en/apps/app.twintaillauncher.ttl)** ([GitHub](https://github.com/TwintailTeam/TwintailLauncher)).

## Steps

1. Install the launcher from Flathub (search "Sleepy launcher").
2. Open it, run the compatibility check and continue through the first-run setup. You can change the folders, defaults are fine.
3. Press **Download** and install Wine Mono when asked, then restart the launcher.
4. Press **Download** again for the game, wait for it to finish, then press **Launch**.

The launcher also has a settings page with a lot of configuration options.

## Frequently asked questions

**Do I need Windows to play this on Linux?**  
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**The game does not start. What should I try first?**  
Update your GPU drivers and Vulkan packages, try the newest Proton-GE, and create a fresh prefix if the old one may be corrupted.
