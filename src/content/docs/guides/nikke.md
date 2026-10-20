---
title: "How to Play NIKKE: Goddess of Victory on Linux (Proton + Heroic Guide)"
description: "Run NIKKE: Goddess of Victory on Linux with DW-Proton and Heroic. Step-by-step setup with screenshots, plus fixes for launch problems and old GPUs."
game: "NIKKE: Goddess of Victory"
sidebar:
  label: "NIKKE: Goddess of Victory"
image: "/images/nikke/thumb.webp"
status: "works"
launcher: "heroic"
protonVersion: ""
onSteam: false
website: "https://nikke-en.com/"
tags: ["nikke", "heroic", "proton", "gacha"]
---

NIKKE: Goddess of Victory can be played on Linux using **Heroic Games Launcher** and a **DW-Proton** runner installed with **ProtonPlus**. This guide walks through the whole process in one place: installing the tools, adding the game to Heroic, installing it, and the extra settings that make it launch consistently.

<iframe width="100%" height="315" src="https://www.youtube.com/embed/NOErdc0z1qU" title="YouTube video player" loading="lazy" allowfullscreen></iframe>

## What you need

| Item | What it is for | Where to get it |
|------|----------------|-----------------|
| **ProtonPlus** | Installs the DW-Proton runner | [Flathub](https://flathub.org/en/apps/com.vysp3r.ProtonPlus) or search your app store |
| **Heroic Games Launcher** | Runs the NIKKE installer and the game | [Flathub](https://flathub.org/en/apps/com.heroicgameslauncher.hgl) or search your app store |
| **NIKKE installer (.exe)** | The official installer from the game's website | [nikke-en.com](https://nikke-en.com/) |

> Install Heroic and ProtonPlus first, and make sure the NIKKE installer `.exe` is in your Downloads folder before you start.

## Part 1: Install DW-Proton with ProtonPlus

1. Open **ProtonPlus**.
2. Download the latest **DW-Proton**. You can install it for Steam or for Heroic, it does not matter which.

   ![ProtonPlus with DW-Proton selected for NIKKE on Linux](/images/nikke/nikkeproton1.webp)
   ![ProtonPlus downloading the latest DW-Proton](/images/nikke/nikkeproton2.webp)

> **Steam or Heroic not in the dropdown?** Open Steam or Heroic once so they can initialise, then open ProtonPlus again and they should appear.

If you already have DW-Proton installed, skip to Part 2. Make sure it is up to date.

## Part 2: Add and install NIKKE in Heroic Games Launcher

### Step 1: Add a new game
Open Heroic Games Launcher, go to your Library and click **ADD GAME** at the top.

![Heroic Games Launcher Library with the Add Game button](/images/nikke/game46img1.webp)

### Step 2: Name the game and open Wine settings
Give the game a title such as "Nikke", then scroll down and click the **Show Wine settings** drop-down arrow to expand the advanced options.

![Heroic Add Game menu with the Show Wine settings option](/images/nikke/game46img2.webp)

### Step 3: Select DW-Proton as the Wine version
Under the expanded Wine settings, open the **Wine version** dropdown and select your custom runner, `DW-Proton-Latest`. This step is crucial for getting the game to launch properly.

![Heroic Wine version dropdown with DW-Proton selected](/images/nikke/nikkeimg1.webp)

### Step 4: Run the installer
Instead of clicking Finish, scroll down and click the blue **RUN INSTALLER FIRST** button. Heroic will set up the environment and prepare to run the Windows setup file.

![Heroic Run Installer First button](/images/nikke/nikkegame5.webp)

### Step 5: Select the installer
A file browser opens. Go to your Downloads folder (or wherever you saved it) and select the official NIKKE installer `.exe` (for example `nikkeminiloader_...exe`), then click **Select**.

![Selecting the NIKKE installer exe in Heroic](/images/nikke/game46img5.webp)

### Step 6: Install the game
When the setup window appears, keep the default install location `C:\NIKKE` (Heroic maps this into your Wine prefix) and click **INSTALL**.

![NIKKE installer screen with the default install directory](/images/nikke/game46img6.webp)

### Step 7: Wait for the download to finish
The launcher downloads the game files. When you see **"Download complete!"**, close this window so you can finish the Heroic configuration.

![NIKKE launcher showing download complete](/images/nikke/game46img7.webp)

### Step 8: Select the installed executable
Back in the Add Game menu, find the **Select Executable** field at the bottom and click the **folder icon**.

![Heroic select executable folder icon](/images/nikke/nikkeimg2.webp)

### Step 9: Point Heroic to nikke_launcher.exe
Browse inside your Wine prefix to `drive_c` > `NIKKE` > `Launcher`, highlight **`nikke_launcher.exe`** and click **Choose**.

![Selecting nikke_launcher.exe inside the Wine prefix](/images/nikke/game46img9.webp)

### Step 10: Finish
Click the green **FINISH** button in the bottom right to add NIKKE to your library, then continue with the extra settings below.

![Heroic Finish button to add NIKKE to the library](/images/nikke/nikkeimg5.webp)

## Part 3: Settings that make NIKKE launch reliably

The game may take a few stops and starts to get working. These settings reduce that.

### Disable Esync and Fsync
1. Open the game's settings and go to the **WINE** tab.
2. Scroll down and make sure both **Enable Esync** and **Enable Fsync** are **unchecked**.

![Heroic Wine tab with Esync and Fsync disabled](/images/nikke/extraimage1.webp)

### Disable GameMode
1. Open the **OTHER** tab.
2. Make sure **Use GameMode** is **unchecked**.

![Heroic Other tab with GameMode disabled](/images/nikke/extraimage2.webp)

### Set the environment variable
In the **ADVANCED** tab, scroll to **Environment Variables**, add the variable below and click the green **+** button.

```bash
PROTON_USE_NTSYNC=0
```

![Heroic Advanced tab environment variables](/images/nikke/extraimage3.webp)

You can now launch NIKKE from Heroic.

## Troubleshooting

### Older hardware (for example Intel HD 4000 graphics)
Add this environment variable the same way as above:

```bash
PROTON_DXVK_SAREK=1
```

If that does not work, try this instead:

```bash
PROTON_USE_WINED3D=1
```

### Nvidia GPU and video not showing
Add this environment variable:

```bash
GST_PLUGIN_FEATURE_RANK=nvh264dec:0,nvdec:0,nvh265dec:0
```

## Frequently asked questions

**Can you play NIKKE: Goddess of Victory on Linux?**
Yes. This guide uses Heroic Games Launcher with DW-Proton to run the official PC installer on Linux.

**Which Proton version should I use for NIKKE?**
Use the latest DW-Proton, installed through ProtonPlus. Selecting it as the Wine version in Heroic is required for the game to launch properly.

**Do I need Steam?**
No. This method uses Heroic Games Launcher. Steam only appears as an optional place to install the DW-Proton runner.

**Why does NIKKE not launch the first time?**
It can take a few attempts. Disable Esync, Fsync and GameMode and set `PROTON_USE_NTSYNC=0` as shown in Part 3.

**Does this work on old graphics cards?**
Often yes. Try `PROTON_DXVK_SAREK=1`, and if that fails `PROTON_USE_WINED3D=1`.
