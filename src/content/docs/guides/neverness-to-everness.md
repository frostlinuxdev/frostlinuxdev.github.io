---
title: "How to Play Neverness to Everness on Linux"
description: "Run Neverness to Everness (NTE) on Linux with Heroic Games Launcher and DW-Proton, including the important C: drive install location."
wip: true
game: "Neverness to Everness"
sidebar:
  label: "Neverness to Everness"
image: "/images/neverness-to-everness/thumb.webp"
heroImage: "/images/neverness-to-everness/hero.webp"
status: "works"
launcher: "steam"
protonVersion: "DW-Proton (Dawn Winery) latest"
hasGameplayVideo: true
gameplay:
  - id: "ZLhQUIPrK7c"
    title: "Neverness To Everness | RTX 3060 12GB Linux CachyOS gameplay"
  - id: "hq1HH9MCTu8"
    title: "NTE on CachyOS: first 30 minutes gameplay"
onSteam: true
steamAppId: 4508340
protondbTier: "gold"
steamUrl: "https://store.steampowered.com/app/4508340/"
tags: ["neverness-to-everness", "gacha"]
---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/CGmwdh34jhk" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

> **Work in progress:** this guide was written from the FrostLinux video and has not been re-tested by me on a current install yet. Steps may change.

Neverness to Everness (NTE) runs on Linux using [Heroic Games Launcher](https://flathub.org/en/apps/com.heroicgameslauncher.hgl) with DW-Proton. The important step is changing the install location to the C drive.

## What you need

| Item | Notes |
|------|-------|
| **NTE installer (.exe)** | PC download from the official website, saved to Downloads |
| **Heroic Games Launcher** | Flathub or GitHub |
| **[ProtonPlus](https://flathub.org/en/apps/com.vysp3r.ProtonPlus)** | Used to download DW-Proton |

## Steps

1. Open Heroic once to initialise it, then open **ProtonPlus**.
2. Download the latest **DW-Proton** (installing it for Steam lets Heroic and [Lutris](https://flathub.org/en/apps/net.lutris.Lutris) see it too and saves space).
3. In Heroic press **Add Game**, type the name and press **Show Wine settings**.
4. Set **Wine version** to DW-Proton **before** the next step.
5. Press **Run installer first** and select the `.exe`.
6. In the installer pick your language, then choose **Custom install** instead of Start install. The installer may default to the W drive, so press **Change** and select `C:\Program Files`. It creates a Neverness to Everness folder there.
7. Agree and let the launcher install, then close it without installing the game yet.
8. Press the folder icon next to **Select executable**, go to `drive_c/Program Files/Neverness to Everness` and choose the global launcher.
9. Press **Finish**, then **Play** to open the launcher, press **Install** and sign in. External accounts worked in the video.

## Troubleshooting

- **Problems after install:** make sure the install location is `C:\Program Files` and not the W drive.

## Gameplay

<div class="gameplay-grid"><figure><iframe src="https://www.youtube.com/embed/ZLhQUIPrK7c" title="Neverness To Everness | RTX 3060 12GB Linux CachyOS gameplay" loading="lazy" allowfullscreen></iframe><figcaption>Neverness To Everness | RTX 3060 12GB Linux CachyOS gameplay</figcaption></figure><figure><iframe src="https://www.youtube.com/embed/hq1HH9MCTu8" title="NTE on CachyOS: first 30 minutes gameplay" loading="lazy" allowfullscreen></iframe><figcaption>NTE on CachyOS: first 30 minutes gameplay</figcaption></figure></div>

## Frequently asked questions

**Do I need Windows to play this on Linux?**  
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**The game does not start. What should I try first?**  
Update your GPU drivers and Vulkan packages, try the newest Proton-GE, and create a fresh prefix if the old one may be corrupted.
