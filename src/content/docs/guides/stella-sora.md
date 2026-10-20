---
title: "How to Play Stella Sora on Linux"
description: "Play Stella Sora on Linux: install it from Steam and run it with Proton. Heroic and the Nadare launcher are covered as alternatives."
wip: true
game: "Stella Sora"
sidebar:
  label: "Stella Sora"
image: "/images/stella-sora/thumb.webp"
heroImage: "/images/stella-sora/hero.webp"
status: "works"
launcher: "steam"
protonVersion: ""
hasGameplayVideo: true
onSteam: true
steamAppId: 4813850
steamUrl: "https://store.steampowered.com/app/4813850/"
nadare: true
tags: ["stella-sora", "gacha"]
---

:::tip[Now on Steam]
Stella Sora is on **Steam**, which makes it the easiest way to play on Linux: no separate installer and no manual Wine prefix. [Open the Steam page](https://store.steampowered.com/app/4813850/).
:::

<iframe width="100%" height="315" src="https://www.youtube.com/embed/VNB9F48Ykhg" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

Stella Sora runs on Linux through Proton. **Use the Steam version.** Steam handles the install, updates and the Proton prefix for you, and it should work out of the box. The Nadare launcher and a manual Heroic install below are alternatives for when you are not using Steam.

## What you need

| Item | Notes |
|------|-------|
| **Stella Sora** | Free from [Steam](https://store.steampowered.com/app/4813850/) |
| **[ProtonPlus](https://flathub.org/en/apps/com.vysp3r.ProtonPlus)** | Optional; Flathub; only needed if the default Proton does not work and you want DW-Proton, Proton-CachyOS or GE-Proton |

## Steam (recommended)

1. Install **Stella Sora** from Steam.
2. Launch it, log in and let the game download its resources.

It should work out of the box with Steam's default Proton, so there is nothing to configure. Your account is cross-platform, so progress is tied to your account and not your operating system.

### If it does not launch

Try a different Proton version, in this order. Install them with ProtonPlus, restart Steam, then pick one under the game's **Properties → Compatibility** by ticking **Force the use of a specific Steam Play compatibility tool**:

1. **DW-Proton (Dawn Wine Proton)**
2. **Proton-CachyOS**
3. **GE-Proton**

## Not using Steam?

You can install the official Windows client through Heroic Games Launcher instead. The method is the same as for Arknights, so follow the [Arknights guide](/guides/arknights/) and its [video](https://www.youtube.com/watch?v=IyEp4NrIGFU). Steam is simpler and is the better choice if you have a choice.

## Nadare (beta)

If you would rather not set anything up by hand and are not using Steam, **Nadare** can install and configure the non-Steam version for you in one click. It is a beta, so **prefer Steam** and treat Nadare as the fallback. [Learn more about Nadare](/nadare/).

## Troubleshooting

- **It does not launch on Steam:** try the Proton versions listed above, in order. Restart Steam after downloading a new runner.
- **Black screen or crash on first launch:** update your GPU drivers and Vulkan packages, then try a fresh prefix (delete the game's `compatdata` folder and relaunch).
- Keep your Proton version and GPU drivers up to date; that fixes most issues.

## Frequently asked questions

**Do I need Windows to play this on Linux?**  
No. The game runs through Proton or Wine, a compatibility layer for Windows games.

**Should I use Steam or Nadare?**  
Steam. It is the simplest and most reliable method. Nadare is a beta and is only needed if you are not using Steam.

**The game does not start. What should I try first?**  
Update your GPU drivers and Vulkan packages, try the newest Proton (Proton-CachyOS, DW-Proton or Proton-GE), and create a fresh prefix if the old one may be corrupted.
