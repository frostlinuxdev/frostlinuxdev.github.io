---
title: "Chaos Zero Nightmare on Linux: Heroic Games Launcher Guide (Stove + WebView2)"
description: "Play Chaos Zero Nightmare on Linux with Heroic. Pick the right Wine version, install Stove and WebView2, and fix the install freeze and Stove launch bug."
sidebar:
  label: "Heroic Games Launcher"
image: "/images/czn/hero.webp"
tags: ["chaos-zero-nightmare", "heroic", "stove", "gacha"]
---

:::note
This is the **[Heroic Games Launcher](https://flathub.org/en/apps/com.heroicgameslauncher.hgl)** method. The shared prerequisites (Stove, WebView2 and downloads), the install-freeze fix and the crashpad fix live on the [Chaos Zero Nightmare overview](/guides/chaos-zero-nightmare/). Heroic has had issues since the Season 2 update — use [Faugus](/guides/chaos-zero-nightmare/faugus/) if you are starting fresh.
:::

## Set up Chaos Zero Nightmare in Heroic

1. Stop the launcher in Heroic if you already ran into the bug.
2. Right-click the **Chaos Zero Nightmare** entry in Heroic and choose **Settings**.
3. In **Wine version**, pick **Proton-GE** (or Proton-CachyOS, both work).

   ![Heroic Wine version settings for Chaos Zero Nightmare](/images/czn/image1.webp)

4. Install WebView2 and Stove into the same prefix (see [What you need](/guides/chaos-zero-nightmare/#what-you-need) for the downloads), then launch the game from Heroic. If Stove will not launch, use the [crashpad fix](/guides/chaos-zero-nightmare/#stove-not-launching-crashpad_handlerexe).

## Troubleshooting

- **Install freezes:** see [Fix: install freeze](/guides/chaos-zero-nightmare/#fix-install-freeze-wayland-or-x11).
- **Stove will not launch afterwards:** see [crashpad_handler.exe](/guides/chaos-zero-nightmare/#stove-not-launching-crashpad_handlerexe).
