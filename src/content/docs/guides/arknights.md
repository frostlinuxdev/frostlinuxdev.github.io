---
title: "How to Play Arknights on Linux"
description: "Install Arknights on Linux with the official PC client through Heroic and Proton-CachyOS or DW-Proton, or in one click with the Nadare launcher."
wip: true
game: "Arknights"
sidebar:
  label: "Arknights"
image: "/images/arknights/thumb.webp"
heroImage: "/images/arknights/hero.webp"
status: "works"
launcher: ""
protonVersion: ""
hasGameplayVideo: true
onSteam: false
website: "https://arknights.global/"
nadare: true
tags: ["arknights", "gacha"]
head: [{"tag": "meta", "attrs": {"name": "keywords", "content": "Arknights on Linux, Arknights Linux guide"}}]
---

:::tip[Nadare (beta): one-click install]
This game is supported by **Nadare**, a launcher that installs and configures it for you in one click. It is in beta, so the manual guide below always works as a fallback. [Learn more about Nadare](/nadare/).
:::

<iframe width="100%" height="315" src="https://www.youtube.com/embed/IyEp4NrIGFU" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

> **Work in progress:** this guide was written from the FrostLinux video and has not been re-tested by me on a current install yet. Steps may change.

Arknights (the original game) now has a PC client that can be installed on Linux through [Heroic Games Launcher](https://flathub.org/en/apps/com.heroicgameslauncher.hgl) with Proton-CachyOS or DW-Proton.

## What you need

| Item | Notes |
|------|-------|
| **Windows client (.exe)** | From the [official Arknights website](https://arknights.global/) ("Download Win client") |
| **Heroic Games Launcher** | Flathub or your app store |
| **Proton-CachyOS or DW-Proton** | Heroic's Wine Manager can download Proton-CachyOS |

## Steps

1. Install Heroic and complete the first-run setup. In **Wine Manager**, make sure Proton-CachyOS is downloaded (it may install automatically).
2. Press **Add Game**, type the game name, press **Show Wine settings** and set **Wine version** to Proton-CachyOS (or DW-Proton).
3. Press **Run installer first** and select the Arknights `.exe`. Install to the default path.
4. Close the installer without opening it, then press the folder icon next to **Select executable** and choose the launcher in `drive_c/Yostar Games/game launcher`.
5. Press **Finish**, play the launcher from Heroic and press **Install game** (default path).
6. Press **Start game**, choose whether to download all or some resources, then log in.

Your account is cross-platform, so progress is tied to your account and not your operating system.

## Troubleshooting

- Keep your Proton version and GPU drivers up to date; that fixes most issues.

## Frequently asked questions

**Do I need Windows to play this on Linux?**  
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**The game does not start. What should I try first?**  
Update your GPU drivers and Vulkan packages, try the newest Proton-GE, and create a fresh prefix if the old one may be corrupted.
