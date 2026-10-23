---
title: "How to Play Arknights: Endfield on Linux"
description: "Arknights: Endfield on Linux: install from Steam and force Dawn Wine Proton, or use Heroic with the official Gryphline client. Screenshots included."
game: "Arknights: Endfield"
sidebar:
  label: "Arknights: Endfield"
image: "/images/arknights-endfield/thumb.webp"
heroImage: "/images/arknights-endfield/hero.webp"
status: "works"
launcher: "steam"
protonVersion: "DW-Proton (Dawn Winery) latest"
hasGameplayVideo: true
gameplay:
  - id: "4XKm32BHpR0"
    title: "Arknights Endfield RTX 3060 CachyOS performance"
onSteam: true
website: "https://endfield.gryphline.com/"
steamAppId: 4732690
protondbTier: "platinum"
steamUrl: "https://store.steampowered.com/app/4732690/"
tags: ["arknights-endfield", "gacha"]
---

:::tip[Now on Steam]
Arknights: Endfield launched on **Steam** on 14 October 2026, which makes it the easiest way to play on Linux — no separate installer and no manual Wine prefix. See the news post: [Arknights: Endfield is now on Steam](/news/arknights-endfield-now-on-steam/).
:::

<iframe width="100%" height="315" src="https://www.youtube.com/embed/sG_UFq9HhbI" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

Arknights: Endfield is a **3D real-time strategy RPG** from Hypergryph, published by Gryphline. You play as the Endministrator of Endfield Industries, explore the planet **Talos-II**, build and defend your factories, and fight in real-time parties. It is free to play, cross-platform, and — since October 2026 — available natively on Steam.

On Linux it runs well through Proton. The recommended path is the **Steam** version with **Dawn Wine Proton (DW-Proton)**. If you would rather not use Steam, the older method — the official Windows client through Heroic — still works.

## What you need

| Item | Notes |
|------|-------|
| **Arknights: Endfield** | Free from [Steam](https://store.steampowered.com/app/4732690/) (recommended) or the [official site](https://endfield.gryphline.com/) |
| **[ProtonPlus](https://flathub.org/en/apps/com.vysp3r.ProtonPlus)** | Flathub; used to download Dawn Wine Proton |
| **[Heroic Games Launcher](https://flathub.org/en/apps/com.heroicgameslauncher.hgl)** | Only for the manual (non-Steam) method |

## Method 1: Steam (recommended)

1. Install **[ProtonPlus](https://flathub.org/en/apps/com.vysp3r.ProtonPlus)** from Flathub and open it once.
2. Select **Steam**, choose **Dawn Wine Proton (DW-Proton)** and download the latest version.
3. Close Steam completely (tray icon → **Exit Steam**, or `killall steam`), then start it again so it sees the new build.
4. Install **Arknights: Endfield** from Steam.
5. Open the game's **Properties → Compatibility**, tick **Force the use of a specific Steam Play compatibility tool** and pick the latest **Dawn Wine Proton**.
6. Launch, log in and let the game download its resources.

Dawn Wine Proton is the build most likely to work. If it fails, other Proton versions usually will not help — the cause is more often game files, permissions or drivers.

## Method 2: Heroic + official client (manual)

1. Open Heroic once so it initialises, then open **ProtonPlus**.
2. Select Heroic (or Steam), choose **DW-Proton** and download the latest version. Restart the app if it does not show as installed.
3. In Heroic press **Add Game** and type the game name.
4. Press **Show Wine settings** and set **Wine version** to the latest DW-Proton.
5. Press **Run installer first**, select the `.exe` you downloaded and install in English to the default location (`C:\Program Files`).
6. Close the installer, then press the folder icon next to **Select executable** and choose the launcher in `drive_c/Program Files/` (Gryphline).
7. Press **Finish**, then play the launcher from Heroic and download the game.
8. Log in. The game may ask you to restart; open it again from the launcher.

## Screenshots

<div class="shot-grid">
  <img src="/images/arknights-endfield/shot-1.webp" alt="Arknights: Endfield overview map and UI" loading="lazy" />
  <img src="/images/arknights-endfield/shot-2.webp" alt="Arknights: Endfield exploration" loading="lazy" />
  <img src="/images/arknights-endfield/shot-3.webp" alt="Arknights: Endfield combat" loading="lazy" />
  <img src="/images/arknights-endfield/shot-4.webp" alt="Arknights: Endfield world" loading="lazy" />
</div>

<a class="store-shot" href="https://store.steampowered.com/app/4732690/" target="_blank" rel="noopener">
  <img src="/images/arknights-endfield/store-capsule.webp" alt="Arknights: Endfield on Steam" loading="lazy" />
</a>

## Troubleshooting

- **It does not launch on Steam:** make sure the game is actually using **Dawn Wine Proton** (Properties → Compatibility) and that Steam was restarted after downloading the runner.
- **Black screen or crash on first launch:** update your GPU drivers and Vulkan packages, then try a fresh prefix (delete the game's `compatdata` folder and relaunch).
- **Launcher shows a blank window (Heroic method):** re-check that the executable points at the Gryphline launcher inside `drive_c/Program Files/`, not the installer.

## Gameplay

<div class="gameplay-grid"><figure><iframe src="https://www.youtube.com/embed/4XKm32BHpR0" title="Arknights Endfield RTX 3060 CachyOS performance" loading="lazy" allowfullscreen></iframe><figcaption>Arknights Endfield RTX 3060 CachyOS performance</figcaption></figure></div>

## Frequently asked questions

**Do I need Windows to play this on Linux?**  
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**Is my progress shared between PC, mobile and Steam?**  
Arknights: Endfield uses a **Gryphline account**, so your progress is tied to your account, not the platform or your operating system.

**The game does not start. What should I try first?**  
Update your GPU drivers and Vulkan packages, make sure Dawn Wine Proton is selected, and create a fresh prefix if the old one may be corrupted.

**Is it free?**  
Yes. Arknights: Endfield is free to play on Steam, PC, mobile and PlayStation.
