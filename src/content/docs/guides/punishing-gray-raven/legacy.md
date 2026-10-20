---
title: "Punishing Gray Raven on Linux: standalone launcher + bbe fix (legacy)"
description: "Archived guide for the old Punishing Gray Raven standalone launcher on Linux and its bbe transparency fix. Use the Steam release if you can."
sidebar:
  label: "Legacy: standalone launcher (bbe)"
tags: ["pgr", "bbe", "heroic", "gacha"]
head: [{"tag": "meta", "attrs": {"name": "keywords", "content": "Punishing Gray Raven Linux launcher transparent fix, bbe launcher_main.dll, PGR legacy method"}}]
---

> **Archived / legacy method.** Use the **[Steam release guide](/guides/punishing-gray-raven/)** instead — it is easier and needs no patches. Keep this page only if you are stuck on the old standalone launcher.

The older method uses the standalone launcher installed with a Proton/Wine runner. The launcher renders transparent under Wine/Proton, so it needs a small patch with **bbe** (Binary Block Editor).

<iframe width="100%" height="315" src="https://www.youtube.com/embed/bBcmhq-0EZE" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

## What you need

| Item | Used for |
|------|----------|
| **bbe** | Patches the launcher so it renders correctly |
| Terminal access | Running the install and patch commands |
| Punishing Gray Raven installed with a Proton/Wine runner | The game itself (older method only) |

## Step 1: Install bbe

### Ubuntu / Debian based distros

For Linux Mint, Ubuntu, Debian, Pop!_OS, PikaOS, Zorin and similar:

```bash
sudo apt update
sudo apt install bbe
```

### Arch based distros (AUR)

For Arch, CachyOS, EndeavourOS and similar (not Steam Deck). The package comes from the Arch User Repository: <https://aur.archlinux.org/packages/bbe>

```bash
sudo pacman -S yay
yay -S bbe
```

### Fedora based distros (COPR)

For Fedora, Nobara and similar. This uses the COPR package: <https://copr.fedorainfracloud.org/coprs/adrianl40/bbe/>

```bash
sudo dnf copr enable adrianl40/bbe
sudo dnf install bbe
```

### Confirm bbe is installed

```bash
bbe --version
```

## Step 2: Fix the transparent launcher

After installing the game with a Proton/Wine runner, the launcher can appear transparent. Open a terminal inside the game's version directory (the folder whose name is a version number) and run:

```bash
mv launcher_main.dll launcher_main.dll.bak
bbe -e "s/\x12AllowsTransparency/\x09IsEnabled\x1bA\x00\x03AAAAA/" launcher_main.dll.bak > launcher_main.dll
```

### The same fix with full paths

This is the same command split up. You have to put in the path to `launcher_main.dll` yourself.

```bash
mv "/path/to/Punishing Gray Raven/#.#.#.#/launcher_main.dll" "/path/to/Punishing Gray Raven/#.#.#.#/launcher_main.dll.bak"

bbe -e "s/\x12AllowsTransparency/\x09IsEnabled\x1bA\x00\x03AAAAA/" "/path/to/Punishing Gray Raven/#.#.#.#/launcher_main.dll.bak" > "/path/to/Punishing Gray Raven/#.#.#.#/launcher_main.dll"
```

> **This does not alter the game in any way.** It only disables transparency inside the launcher so the launcher can render.

## Frequently asked questions

**Why is the Punishing Gray Raven launcher transparent on Linux?**
The launcher uses window transparency, which does not render under Wine/Proton. Patching `launcher_main.dll` with bbe disables transparency in the launcher only.

**Is the bbe patch safe?**
Yes. It does not change the game. It only disables transparency in the launcher, and the original file is kept as `launcher_main.dll.bak`.

**Does this work on Steam Deck?**
Steam Deck needs a different guide. The Discord server has one using the Universal Method.
