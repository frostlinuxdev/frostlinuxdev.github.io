---
title: "How to Play Girls' Frontline 2: Exilium on Linux"
description: "Run Girls' Frontline 2: Exilium on Linux — the Dark Winter client works with a Wine runner, while the HaoPlay client needs a Lutris install script."
wip: true
game: "Girls' Frontline 2: Exilium"
sidebar:
  label: "Girls' Frontline 2: Exilium"
image: "/images/girls-frontline-2/thumb.webp"
heroImage: "/images/girls-frontline-2/hero.webp"
rating: "out-of-the-box"
status: "works"
launcher: "steam"
protonVersion: "Proton (default)"
onSteam: true
website: "https://gf2exilium.sunborngame.com/"
steamAppId: 3347400
protondbTier: "gold"
steamUrl: "https://store.steampowered.com/app/3347400/"
tags: ["girls-frontline-2", "gacha"]
---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/XIL1E97HWHA" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

> **Work in progress:** this guide was written from the FrostLinux video and has not been re-tested by me on a current install yet. Steps may change.

Girls' Frontline 2: Exilium has two clients on Linux. The Dark Winter version should work out of the box with just a Wine runner selected, while the HaoPlay version needs an install script or manual setup.

## What you need

| Item | Notes |
|------|-------|
| **[Lutris](https://flathub.org/en/apps/net.lutris.Lutris)** | From Flathub; used by the HaoPlay install script |
| **Free disk space** | About 45 GB |

## HaoPlay version with the Lutris install script

1. Install Lutris from Flathub and open it once so it finishes setting up DXVK, Proton and so on.
2. Find the community Lutris installer for GFL 2 (HaoPlay version), press **Install**, and let it open in Lutris.
3. Leave the install location and options at their defaults.
4. When the installer launcher opens, accept and press **One click install**.
5. When the game has downloaded, close the installer launcher so the script knows it is done (press the cog icon > **Quit**).
6. The game appears in Lutris. Launch it, press **Start**, and let it update.

## Steam / manual method
A manual Steam method is also shown in the video and is more work. Write this section from the video and the community guide it follows.

## Dark Winter version
Select your Wine runner and play; it should work out of the box.

## Frequently asked questions

**Do I need Windows to play this on Linux?**  
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**The game does not start. What should I try first?**  
Update your GPU drivers and Vulkan packages, try the newest Proton-GE, and create a fresh prefix if the old one may be corrupted.
