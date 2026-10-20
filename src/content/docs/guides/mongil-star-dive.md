---
title: "How to Play Mongil: Star Dive on Linux"
description: "Run Mongil: Star Dive on Linux with the official Netmarble Launcher through Heroic, or the native community stardive-launcher. Both methods still need testing."
game: "Mongil: Star Dive"
sidebar:
  label: "Mongil: Star Dive"
image: "/images/mongil-star-dive/thumb.webp"
heroImage: "/images/mongil-star-dive/hero.webp"
status: "works"
launcher: "heroic"
protonVersion: ""
hasGameplayVideo: true
gameplay:
  - id: "VRTBU78ZT98"
    title: "Mongil Star Dive: First Minutes Linux CachyOS"
onSteam: false
tags: ["mongil-star-dive", "gacha"]
---

> There are two ways to launch the game: the official **Netmarble Launcher** (run through Heroic) and the native community **[`stardive-launcher`](https://github.com/Shidohs/stardive-launcher)**. Both need verifying on a current install before this guide is published.

<iframe width="100%" height="315" src="https://www.youtube.com/embed/25dvNQRNXvg" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

Mongil: Star Dive runs on Linux either through the **official Netmarble Launcher** in a Wine prefix (via [Heroic Games Launcher](https://flathub.org/en/apps/com.heroicgameslauncher.hgl)), or with the native community launcher **`stardive-launcher`**. Use the PC version from the official site (not the Epic Games version).

## Choose your launcher

| Launcher | Notes |
|----------|-------|
| **Netmarble Launcher** (official) | Installed through Heroic with Proton-CachyOS or DW-Proton. The method below. |
| **`stardive-launcher`** (community) | Native Linux launcher and downloader. [GitHub →](https://github.com/Shidohs/stardive-launcher) |

## What you need

| Item | Notes |
|------|-------|
| **PC installer (.exe)** | PC version from the official page (not Epic) |
| **Heroic Games Launcher** | Flathub or GitHub |
| **[ProtonPlus](https://flathub.org/en/apps/com.vysp3r.ProtonPlus)** | To download Proton-CachyOS or DW-Proton |
| **`stardive-launcher`** (alternative) | [GitHub](https://github.com/Shidohs/stardive-launcher) |

## Steps (Netmarble Launcher via Heroic)

1. If the PC download does not work in your browser (for example Brave), press PC > Download now, scroll to the FAQ and download from there.
2. Open Heroic once so it initialises, then open **ProtonPlus** and download Proton-CachyOS latest or DW-Proton latest (DW-Proton is geared toward anime games). Install to Steam so Heroic and [Lutris](https://flathub.org/en/apps/net.lutris.Lutris) can see it and you save space.
3. In Heroic press **Add Game**, type the name and press **Show Wine settings** and set the Wine version to the Proton you downloaded.
4. Press **Run installer first**, select the `.exe`, agree and install to the default location.
5. Close the installer, then press the folder icon next to **Select executable** and choose `drive_c/Program Files/Netmarble/Netmarble Launcher/Netmarble Launcher.exe`.
6. Press **Finish**, launch the launcher from Heroic and install the game to the default location.
7. Run the game and sign in.

### Alternative: `stardive-launcher`

Download the native launcher from [github.com/Shidohs/stardive-launcher](https://github.com/Shidohs/stardive-launcher) and follow its README. It handles the download and launch natively, so no Wine prefix is needed. **Untested — report how it goes.**

## Troubleshooting

- **Google login did not work:** sign in with email instead. This may depend on your browser.

## Gameplay

<div class="gameplay-grid"><figure><iframe src="https://www.youtube.com/embed/VRTBU78ZT98" title="Mongil Star Dive: First Minutes Linux CachyOS" loading="lazy" allowfullscreen></iframe><figcaption>Mongil Star Dive: First Minutes Linux CachyOS</figcaption></figure></div>

## Frequently asked questions

**Do I need Windows to play this on Linux?**
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**Which launcher should I use?**
Try the native [`stardive-launcher`](https://github.com/Shidohs/stardive-launcher) first — it avoids Wine entirely. The official Netmarble Launcher through Heroic is the fallback.

**The game does not start. What should I try first?**
Update your GPU drivers and Vulkan packages, try the newest Proton-GE, and create a fresh prefix if the old one may be corrupted.
