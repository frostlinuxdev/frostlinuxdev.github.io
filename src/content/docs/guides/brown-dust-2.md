---
title: "How to Play Brown Dust 2 on Linux"
description: "Run Brown Dust 2 on Linux with Heroic Games Launcher (or Faugus) and a Proton-GE runner, using the PC installer from the game's Discord."
game: "Brown Dust 2"
sidebar:
  label: "Brown Dust 2"
image: "/images/brown-dust-2/thumb.webp"
status: "works"
launcher: "heroic-or-faugus"
protonVersion: ""
onSteam: false
website: "https://www.browndust2.com/"
tags: ["brown-dust-2", "gacha"]
---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/1jIZEPL5Xmc" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

Brown Dust 2 runs on Linux through [Heroic Games Launcher](https://flathub.org/en/apps/com.heroicgameslauncher.hgl) with a Proton-GE runner and the PC installer from the game's Discord.

## What you need

| Item | Notes |
|------|-------|
| **PC installer (.exe)** | From the PC download channel on the official Brown Dust 2 Discord (see the [official site](https://www.browndust2.com/)) |
| **Heroic Games Launcher** | Flathub or GitHub |
| **Proton-GE** (or CachyOS) | Wine version for the game |

## Steps

1. Download the `.exe` from the Discord's PC download channel.
2. In Heroic press **Add Game**, type a name and press **Show Wine settings**.
3. Set **Wine version** to GE-Proton latest (Proton-CachyOS or GE-Proton both work).
4. Under **Select executable** press the folder icon and select the `.exe` you downloaded.
5. Press **Finish**, then right-click the game > **Settings** > **Advanced** and paste the game arguments from the Discord guide.
6. Launch the game. The installer runs and installs to the C drive as the Discord says. The download is about 13 GB.
7. Accept the terms and log in with your account. Press auto login.

Steam and Bottles methods are mentioned in the Discord but not covered in the video.

## Frequently asked questions

**Do I need Windows to play this on Linux?**  
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**The game does not start. What should I try first?**  
Update your GPU drivers and Vulkan packages, try the newest Proton-GE, and create a fresh prefix if the old one may be corrupted.
