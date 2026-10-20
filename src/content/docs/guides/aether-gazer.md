---
title: "Aether Gazer on Linux: Fix Older GPU / DX11 Vulkan Errors (Proton-Sarek)"
description: "Aether Gazer won't launch on an older GPU? Fix DX11/Vulkan errors on Linux with Proton-Sarek from ProtonPlus, or use PROTON_USE_WINED3D=1 in Heroic."
game: "Aether Gazer"
sidebar:
  label: "Aether Gazer"
image: "/images/ag/thumb.webp"
status: "works"
launcher: "heroic"
protonVersion: ""
hasGameplayVideo: true
gameplay:
  - id: "IxZpi3wmYio"
    title: "Aether Gazer RTX 3060 12GB Linux CachyOS 1440p max settings gameplay"
onSteam: false
website: "https://aethergazer.com/"
tags: ["aether-gazer", "heroic", "proton", "old-gpu", "gacha"]
---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/j08YFuLEeD8" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

If **Aether Gazer** fails to launch on Linux because your GPU does not support the required DX11 or Vulkan version (when using **Proton-GE** or **Proton-CachyOS**), there are two fixes: install **Proton-Sarek**, or force Wine's DX9 renderer with an environment variable. This guide covers both using [Heroic Games Launcher](https://flathub.org/en/apps/com.heroicgameslauncher.hgl).

## Which fix should I use?

| Situation | Fix |
|-----------|-----|
| GPU is old but supports some Vulkan | [Install Proton-Sarek](#1-install-proton-sarek-from-protonplus) |
| GPU is older than Proton-Sarek supports | [Force Wine DX9 with `PROTON_USE_WINED3D=1`](#2-force-wine-dx9-with-an-environment-variable) |

## 1. Install Proton-Sarek from ProtonPlus

ProtonPlus bundles the newest Proton releases, including Proton-Sarek.

| Source | Link |
|--------|------|
| Flathub | <https://flathub.org/en/apps/com.vysp3r.ProtonPlus> |
| GitHub | <https://github.com/Vysp3r/protonplus> |

### Steps

1. **Download ProtonPlus.**
   - From Flathub, click the green Install button.
   - From GitHub, download the native package for your distribution (RPM for Fedora/Red Hat, DEB for Debian/Ubuntu, or an Arch package for Arch) and install it with your package manager.

2. **Open ProtonPlus** and select the launcher you use (Heroic in this case) in the top-left drop-down menu.
3. Click **Install Proton-Sarek Latest** with the download icon.

   ![ProtonPlus installing Proton-Sarek Latest for Heroic to fix Aether Gazer on old GPUs](/images/ag/hgl/image5.webp)

4. **Re-launch Heroic** and change Aether Gazer's Wine/Proton version to **Proton-Sarek Latest**.
5. Launch the game. It should now start normally.

   ![Heroic game settings with Proton-Sarek selected for Aether Gazer](/images/ag/hgl/image3.webp)
   ![Heroic Wine version dropdown for Aether Gazer](/images/ag/hgl/image4.webp)

6. Play and have fun.

## 2. Force Wine DX9 with an environment variable

If your hardware is older than what Proton-Sarek supports, you can fall back to Wine's DirectX 9 renderer.

### Steps

1. In Aether Gazer's settings in Heroic (right click, then **Settings**), go to **Advanced** and add this environment variable:

   ```text
   PROTON_USE_WINED3D=1
   ```

   Use the copy button on the code block when you hover over it.

   ![Heroic Advanced settings with the PROTON_USE_WINED3D environment variable](/images/ag/hgl/image6.webp)

2. Launch the game and play.

> **What does this do?** `PROTON_USE_WINED3D` tells Proton to use the OpenGL-based *wined3d* backend instead of the Vulkan-based DXVK for D3D10/D3D11.

## Gameplay

<div class="gameplay-grid"><figure><iframe src="https://www.youtube.com/embed/IxZpi3wmYio" title="Aether Gazer RTX 3060 12GB Linux CachyOS 1440p max settings gameplay" loading="lazy" allowfullscreen></iframe><figcaption>Aether Gazer RTX 3060 12GB Linux CachyOS 1440p max settings gameplay</figcaption></figure></div>

## Frequently asked questions

**Why does Aether Gazer not launch on my old GPU on Linux?**
The game needs DX11 support, and Proton-GE and Proton-CachyOS translate it to Vulkan through DXVK. If your GPU does not support the required Vulkan version, the game fails to start.

**What is Proton-Sarek?**
Proton-Sarek is a Proton build that adds better Vulkan support for older GPUs. You can install it from ProtonPlus.

**What does PROTON_USE_WINED3D=1 do?**
It makes Proton use the OpenGL-based wined3d renderer instead of the Vulkan-based DXVK for D3D10/D3D11, which helps on hardware that cannot run DXVK.

**Do I need Heroic Games Launcher?**
This guide uses Heroic, but the same Proton version and environment variable apply in other launchers that let you pick a Proton build and set variables.
