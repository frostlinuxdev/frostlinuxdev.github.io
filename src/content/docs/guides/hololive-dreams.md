---
title: "How to Play hololive Dreams on Linux (Steam + DW-Proton Guide)"
description: "Play hololive Dreams on Linux with Steam and the DW-Proton (Dawn Winery) runner installed through ProtonPlus. Step-by-step setup for the hololive rhythm RPG."
wip: true
game: "hololive Dreams"
sidebar:
  label: "hololive Dreams"
image: "/images/hololive-dreams/thumb.webp"
heroImage: "/images/hololive-dreams/hero.webp"
status: "works"
launcher: "steam"
protonVersion: "DW-Proton (Dawn Winery) latest"
onSteam: true
steamUrl: "https://store.steampowered.com/app/4282500/"
steamAppId: 4282500
website: "https://www.hololive-dreams.com/"
tags: ["hololive-dreams", "steam", "proton", "rhythm"]
---

> **Works.** Tested on Linux with the **DW-Proton (Dawn Winery)** runner, installed through ProtonPlus.

hololive Dreams runs on Linux through **Steam** with the **DW-Proton (Dawn Winery)** compatibility tool. DW-Proton is installed with **ProtonPlus**, and you then tell Steam to use it for the game. This guide covers the full setup.

## What you need

| Item | What it is for |
|------|----------------|
| **Steam** | Installs and launches hololive Dreams |
| **hololive Dreams** | The game itself, free on Steam |
| **ProtonPlus** | Downloads the DW-Proton runner |

## Step 1: Install ProtonPlus

Install ProtonPlus from Flathub: <https://flathub.org/en/apps/com.vysp3r.ProtonPlus>, or search for **ProtonPlus** in your software or app manager.

## Step 2: Download DW-Proton

Open ProtonPlus and download the latest **DW-Proton (Dawn Winery)**. Make sure you are installing it for **Steam**, shown by the icon in the top right.

## Step 3: Set hololive Dreams to use DW-Proton

You can do this in ProtonPlus or directly in Steam. Either works.

### Option A: In ProtonPlus
Set hololive Dreams to use DW-Proton in the compatibility settings in ProtonPlus.

### Option B: In Steam
Open the game's properties in Steam, go to **Compatibility**, tick **Force the use of a specific Steam Play compatibility tool** and select **DW-Proton (Dawn Winery)**.

Then you can launch the game.

## Troubleshooting

**The game crashes or shows a black screen on launch**
Make sure DW-Proton is selected for hololive Dreams (not the default Proton). If it still fails, update DW-Proton in ProtonPlus — the newest build usually carries the latest upstream fixes.

**Rhythm notes feel off-sync or stutter**
Turn off the Steam overlay for the game and try borderless windowed mode. Rhythm games are sensitive to compositor frame pacing.

**No sound**
Check that PulseAudio/PipeWire is running and that the game is not muted in your mixer. Some Proton builds need the game restarted after a device change.

## Frequently asked questions

**Can you play hololive Dreams on Linux?**
Yes. Install it through Steam and set DW-Proton (Dawn Winery) as the compatibility tool, as shown above.

**Which Proton should I use for hololive Dreams?**
This guide uses the latest DW-Proton (Dawn Winery), installed with ProtonPlus.

**Do I need ProtonPlus?**
ProtonPlus is the easiest way to download DW-Proton for Steam. You can then select it in Steam's compatibility settings.

**Is hololive Dreams free?**
Yes — it is a free-to-play rhythm game and RPG on Steam.
