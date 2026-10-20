---
title: "How to Play Blue Archive on Linux"
description: "Run Blue Archive on Linux through Steam with a Proton-GE runner installed via Proton Plus. Includes the account-linking step."
wip: true
game: "Blue Archive"
sidebar:
  label: "Blue Archive"
image: "/images/blue-archive/thumb.webp"
heroImage: "/images/blue-archive/hero.webp"
rating: "out-of-the-box"
status: "works"
launcher: "steam"
protonVersion: "Proton (default)"
hasGameplayVideo: true
gameplay:
  - id: "ch0Pv63JdRs"
    title: "Aris & Kei pulls on Blue Archive, running on Linux (gameplay proof)"
onSteam: true
website: "https://bluearchive.nexon.com/"
steamAppId: 3557620
protondbTier: "platinum"
steamUrl: "https://store.steampowered.com/app/3557620/"
tags: ["blue-archive", "gacha"]
---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/fkXJltMVoNM" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

> **Work in progress:** this guide was written from the FrostLinux video and has not been re-tested by me on a current install yet. Steps may change.

Blue Archive runs on Linux through Steam using Proton-GE.

## What you need

| Item | Notes |
|------|-------|
| **Steam** | With Blue Archive installed |
| **[ProtonPlus](https://flathub.org/en/apps/com.vysp3r.ProtonPlus)** | Used to install Proton-GE for Steam |

## Steps

1. Open **ProtonPlus**, choose **Steam**, select Proton-GE and download the latest version.
2. Close Steam completely (right-click the tray icon > Exit Steam, or `killall steam`), then start it again.
3. Open the game's cog icon > **Properties** > **Compatibility**.
4. Tick **Force the use of a specific Steam Play compatibility tool** and pick the latest Proton-GE.
5. Launch the game. It may ask you to link your Nexon account to your Steam account.

## Gameplay

<div class="gameplay-grid"><figure><iframe src="https://www.youtube.com/embed/ch0Pv63JdRs" title="Aris & Kei pulls on Blue Archive, running on Linux (gameplay proof)" loading="lazy" allowfullscreen></iframe><figcaption>Aris & Kei pulls on Blue Archive, running on Linux (gameplay proof)</figcaption></figure></div>

## Frequently asked questions

**Do I need Windows to play this on Linux?**  
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**The game does not start. What should I try first?**  
Update your GPU drivers and Vulkan packages, try the newest Proton-GE, and create a fresh prefix if the old one may be corrupted.
