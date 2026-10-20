---
title: "How to Play Punishing Gray Raven on Linux (Steam + DW-Proton)"
description: "Play Punishing Gray Raven on Linux with the Steam release. Install DW-Proton through ProtonPlus, force it in Steam and launch. The old method is archived."
game: "Punishing Gray Raven"
sidebar:
  label: "Punishing Gray Raven"
image: "/images/pgr/thumb.webp"
heroImage: "/images/pgr/hero.webp"
status: "works"
launcher: "steam"
protonVersion: "DW-Proton (Dawn Winery) latest"
onSteam: true
steamUrl: "https://store.steampowered.com/app/4125930/"
steamAppId: 4125930
website: "https://pgr.kurogames.com/"
tags: ["pgr", "steam", "proton", "gacha"]
---

<iframe width="100%" height="315" src="https://www.youtube.com/embed/dbyDUBL29S4" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

Punishing Gray Raven now has a **Steam release**, and on Linux it just works with a community Proton build. Install **DW-Proton (Dawn Winery)** with **[ProtonPlus](https://flathub.org/en/apps/com.vysp3r.ProtonPlus)**, point Steam at it, and launch — no launcher patches needed.

> **Old standalone-launcher method archived.** The older method (which needed the `bbe` transparency fix) is kept for reference only: [Standalone launcher + bbe fix (legacy)](/guides/punishing-gray-raven/legacy/).

## What you need

| Item | Notes |
|------|-------|
| **Steam** | Native or Flatpak |
| **ProtonPlus** | To download and install the runner |
| **DW-Proton (Dawn Winery) latest** | The runner this guide uses; install it to Steam so it appears as a compatibility tool |

## Steps

1. Install **Punishing Gray Raven** from Steam (app [4125930](https://store.steampowered.com/app/4125930/)).
2. Open **ProtonPlus** and install **DW-Proton (Dawn Winery) latest**. Install it to Steam so Steam can see it.
3. In Steam, right-click Punishing Gray Raven → **Properties** → **Compatibility** → tick **Force the use of a specific Steam Play compatibility tool**, and choose **DW-Proton**.
4. Launch the game and sign in.

## Troubleshooting

- **It does not launch:** confirm DW-Proton is selected for the game (step 3), then try **Proton-GE** as a fallback via ProtonPlus.
- **Old method users:** see the [legacy standalone-launcher guide](/guides/punishing-gray-raven/legacy/) if you are still on the non-Steam client.

## Frequently asked questions

**Can you play Punishing Gray Raven on Linux?**
Yes. The Steam release runs with DW-Proton and needs no extra setup.

**Do I need the bbe launcher fix?**
No. That fix was only for the old standalone launcher; the Steam release does not use it.

**Does this work on Steam Deck?**
The same Steam + DW-Proton setup applies. The Discord server also has a Universal Method guide.
