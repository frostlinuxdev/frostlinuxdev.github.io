+++
title = "Chaos Zero Nightmare on Linux2"
date  = "2026-01-13"
+++


# 1️⃣  Original guide – can be followed till from start till 6:00. Follow below if you cannot press Install 


{{< youtube WXE_aHProwo>}}

## 2️⃣  Open the Heroic Games Launcher
1. Stop the launcher on Heroic Game if you already encounted the bug
2. Right‑click the **Chaos Zero Nightmare** entry in Heroic and choose **Settings**.  
3. In *Wine version*, pick **Proton‑GE** (or Proton CachyOS – both work fine) if not done already.  

![Heroic Settings](images/czn/image1.png)


## 3️⃣  Enable Wine Wayland (fixes the “install frozen” bug)

> Try this fix first unless you know you are on X11 or Linux Mint.

![Wayland Switch](images/czn/image2.png)
Enable it by pressing the box then open the game should be fixed. 


### Alternate method – for X11/Linux Mint(not using Wayland)users

If you’re running an X11 session (i3, XFCE, Qtile, dwm, Linux Mint, etc.) the following steps apply:

1. Open **Settings → WINECFG** (Wine configuration).  
2. Click **Install** to open the configuration window.  
3. Go to the **Graphics** tab.  
4. Check **Emulate virtual desktop** and adjust the size if desired.  
5. Click **Apply**, then **OK**.

![X11 Configuration](images/czn/image3.webp)
![Wine Install](images/czn/image4.webp)
![Graphics Tab](images/czn/image5.webp)


## 4️⃣  Launch the game

Start Chaos Zero Nightmare from Heroic (or whatever launcher you use).  
The installation‑freeze bug should no longer appear.

If you need to revert the changes, simply uncheck the “Emulate virtual desktop” box or disable Wine Wayland again.


## 5️⃣  Lutris – enabling Wine Wayland

1. Open your Lutris settings for the game.  
2. Add the environment variable:

```bash
PROTON_ENABLE_WAYLAND=1
```

3. Save and launch.

![Lutris Wayland](images/czn/lutrisimage2.webp)


## 6️⃣  Lutris – enabling a virtual desktop

To get into Wine Config on Lutris just select the game and press the arrow to reveal the menu.Select wine configuration


…and then enable **Emulate virtual desktop** in the Wine configuration (same screenshots as step 3).

![Lutris Virtual Desktop](images/czn/lutrisimage1.webp)

