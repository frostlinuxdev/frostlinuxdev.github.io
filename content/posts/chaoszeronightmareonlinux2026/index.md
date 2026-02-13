+++
title = "Chaos Zero Nightmare on Linux All Launcher Guides"
date  = "2026-01-30"
+++

### YouTube Guide (Heroic Games is having Issues after Season 2 update) – video will be replaced soon
{{< youtube YBVMvz0JN8A >}}

## What you’ll need

| Item                        | Description                                          | Download link |
|-----------------------------|------------------------------------------------------|---------------|
| **Stove Client**            | Official client to play the game on Linux.           | [Download here](https://store.onstove.com/en/download) |
| **Microsoft Edge WebView2** | Runtime required by Stove (provides the web‑view component). | [Get it from Microsoft here](https://developer.microsoft.com/en-us/microsoft-edge/webview2?form=MA13LH) |
| **Fuagus Launcher**         | Front‑end for installing and launching games on Linux. | [Install via Flathub](https://flathub.org/en/apps/io.github.Faugus.faugus-launcher) |

> **Important**  
> Download the evergreen bootstrapper for Microsoft Edge WebView2 and save it to your `Downloads` folder.  
> Then download the Stove client using the link above or a search engine.

![Heroic Settings](images/czn/webview1.png)

---

## 1️⃣ Fuagus Launcher: Quick Start

1. Open **Fuagus Launcher**.  
2. Go to *Settings* → *Proton Manager* and download the latest available Proton.  

   ![Graphics Tab](images/czn2/image9.png)  
   ![Graphics Tab](images/czn2/image10.png)

3. Click the **+** button, add the name of the game, then click the search icon and locate the `STOVE.exe` you downloaded earlier.

   ![Add Game](images/czn2/image1.png)  
   ![Add Game](images/czn2/image2.png)  
   ![X11 Configuration](images/czn2/image3.png)

5. Set Proton to the version you downloaded, then press **OK**.  
6. Click **Play** – Stove will install quickly, accepting terms and defaults.

   ![Graphics Tab](images/czn2/image11.png)
   ![Graphics Tab](images/czn2/image12.png)

Once Stove finished installing:
Right‑click the CZN entry in Fuagus Launcher, choose **Edit**, then click **Run** and locate your Microsoft Edge WebView evergreen bootstrapper executable.

   ![Wine Install](images/czn2/image4.png)
   ![Graphics Tab](images/czn2/image6.png)

---

## 2️⃣ Wayland‑Friendly Setup

After installing WebView, most users can simply enable Wayland by adding the following launch argument:

```bash
PROTON_ENABLE_WAYLAND=1
```

![Winecfg – Wayland](images/czn2/image7.png)

If you already enabled Wayland in your settings, skip to [Launch Stove from Fuagus (Click this text)](#launch)

---

## 3️⃣ X11 / Linux‑Mint Workaround

For users on an X11 session (i3, XFCE, Qtile, dwm, Linux Mint, etc.) follow these steps instead of enabling Wayland:

1. Open **Tools → WINECFG** (Wine configuration).  
2. Click **Install** to open the configuration window.  
3. Go to the **Graphics** tab.  
4. Check **Emulate virtual desktop** and adjust the size if desired.  
5. Click **Apply**, then **OK**.

   ![Winecfg – X11](images/czn2/image8.png)
   ![Wine Install](images/czn/image4.webp)
   ![Graphics Tab](images/czn/image5.webp)

---

## 4️⃣ Launch Stove from Fuagus {#launch}

Copy the prefix path you used when installing Stove and paste it into the **Prefix** box.  
Then click **Search** and locate your `STOVE.exe`. It will look something like:

```text
/home/user/Fuagus/prefix_name/drive_c/ProgramData/Smilegate/STOVE/STOVE.exe
```

For Example my user is frost and my prefix is called czn2:

```text
/home/frost/Faugus/czn2/drive_c/ProgramData/Smilegate/STOVE/STOVE.exe
```

   ![Wine Install](images/czn2/image14.png)  
   ![Graphics Tab](images/czn2/image15.png)

Once the executable is found, click **Run** to start Stove.

---

*Happy gaming!*