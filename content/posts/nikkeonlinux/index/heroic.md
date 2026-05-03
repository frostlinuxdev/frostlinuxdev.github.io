+++
title = "Nikke on Linux Heroic Games Launcher Method"
date = "2026-03-01"
description = "A step-by-step guide to installing the game on Linux using Heroic Games Launcher and a custom Wine miniloader."


+++

# Heroic Games Installation Method

## Step 1: Add a New Game
Open your Heroic Games Launcher, navigate to your Library, and click the **ADD GAME** button at the top.

![Heroic Library Add Game](/images/nikke/game46img1.png)
*Figure 1: The Add Game button in the Heroic Library.*

---

## Step 2: Name the Game and Access Settings
Give your game a title (I put "Nikke G" so the image would generate but Nikke is fine). Then, look further down the menu and click the **Show Wine settings** drop-down arrow to expand the advanced options.

![Heroic Add Game Menu](/images/nikke/game46img2.png)
*Figure 2: Naming the shortcut and opening Wine settings.*

---

## Step 3: Select the Custom Wine Version
Under the expanded Wine settings, click the **Wine version** dropdown. Select your custom runner (in this case, `DW-Proton-Latest`). This idds crucial for getting the game to launch properly!

![Heroic Wine Version Selection](/images/nikke/nikkeimg1.png)
*Figure 3: Selecting the miniloader Wine version.*

---

## Step 4: Run the Installer
Instead of clicking Finish, scroll down and click the bright blue **RUN INSTALLER FIRST** button. This will tell Heroic to set up the environment and prepare to run the Windows setup file.

![Heroic Run Installer Button](/images/nikke/nikkegame5.png)
*Figure 4: Initiating the installer sequence.*

---

## Step 5: Select the Executable
A file browser window will pop up. Navigate to your Downloads folder (or wherever you saved it) and select the official installer `.exe` file (e.g., `nikkeminiloader_...exe`). Click Select to begin the installation process!

![Heroic Select EXE file](/images/nikke/game46img5.png)
*Figure 5: Selecting the downloaded installer file.*

---



## Step 6: Begin the Game Installation
After selecting the installer executable, the game's setup window will appear. Ensure the install location is set to the default `C:\NIKKE` (which Heroic maps to your Wine prefix) and click the large **INSTALL** button at the bottom.

![NIKKE Install Screen](/images/nikke/game46img6.png)
*Figure 6: Choosing the installation directory and starting the process.*

---

## Step 7: Wait for Download Completion
The launcher will now download the necessary game files. Once the progress bar finishes and you see the **"Download complete!"** message, you are ready to move on. You can close this window so we can finish the Heroic configuration.

![NIKKE Download Complete](/images/nikke/game46img7.png)
*Figure 7: The launcher confirming all files have been successfully downloaded.*

---


## Step 7: Select the Installed Executable
Now that the game is officially installed, we need to tell Heroic which file actually launches it. In the "Add Game" menu, look for the **Select Executable** field at the bottom and click the **Folder Icon**.

![Opening the file browser](/images/nikke/nikkeimg2.png)
*Figure 8: Navigating to the installed game's launcher file.*

---

## Step 8: Point to nikke_launcher.exe
A file browser will open inside your Wine prefix. Navigate through the folders (usually `drive_c` > `NIKKE` > `Launcher`) until you find **`nikke_launcher.exe`**. Highlight it and click the **Choose** button in the top right.

![Selecting the .exe](/images/nikke/game46img9.png)
*Figure 9: Selecting the correct executable to ensure the game boots properly.*

---

## Step 9: Finalize and Finish then do extra steps below
Click the green **FINISH** button in the bottom right corner to add the game to your library.

![Clicking Finish](/images/nikke/nikkeimg5.png)



Extra steps to help the game launch more consistently

### Step 1: Disable Esync and Fsync
1. Open the settings and navigate to the **WINE** tab.
2. Scroll down through the options.
3. Ensure that the checkboxes for both **Enable Esync** and **Enable Fsync** are completely **unchecked**.
![Clicking Finish](/images/nikke/extraimage1.png)

---

### Step 2: Disable GameMode
1. Switch over to the **OTHER** tab at the top of the settings window.
2. Locate the setting labeled **Use GameMode (Feral Game Mode needs to be installed)**.
3. Ensure that the checkbox next to this setting is **unchecked**. 

![Clicking Finish](/images/nikke/extraimage2.png)

---




### Step 3: Set Environment Variables
1. Scroll down to the **Environment Variables** in the **ADVANCED** tab.
2. Set the variable name and value exactly as follows (you can copy and paste the variable name below):

**Variable Name:**
```bash
PROTON_USE_NTSYNC=0
```
3. Click the green **+** (plus) button to the varaible.

![Clicking Finish](/images/nikke/extraimage3.png)
---


# You can now launch Nikke from Heroic and everything should be good.


---

### Extra enviroment variables for older hardware users

**Older hardware like intel hd 4000 graphics**
```bash
PROTON_DXVK_SAREK=1
```
**If that files tried this instead**
```bash
PROTON_USE_WINED3D=1
```
3. Click the green **+** (plus) button to the varaible.

![Clicking Finish](/images/nikke/extraimage3.png)

---


### If you have an Nvidia GPU and video is not showing try this

```bash
GST_PLUGIN_FEATURE_RANK=nvh264dec:0,nvdec:0,nvh265dec:0
```

<div style="margin-top: 40px; display: flex; justify-content: space-between; gap: 20px; flex-wrap: wrap;">
  <a href="../protonplus" style="padding: 12px 24px; background-color: #4b5563; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; text-align: center; flex: 1; min-width: 200px;">
    ⬅️ Back to Guide Menu
  </a>
  
  
</div>