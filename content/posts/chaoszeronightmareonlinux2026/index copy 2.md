+++
title = "Chaos Zero Nightmare on Linux"
date  = "2026-01-30"
+++



# YouTube Guide
{{< youtube YBVMvz0JN8A >}}

## What you’ll need

| Item                        | Description                                          | Download link |
|-----------------------------|------------------------------------------------------|---------------|
| **Stove Client**            | Official client to play the game on Linux.           | [Download here](https://store.onstove.com/en/download) |
| **Microsoft Edge WebView2** | Runtime required by Stove (provides the web‑view component). | [Get it from Microsoft here](https://developer.microsoft.com/en-us/microsoft-edge/webview2?form=MA13LH) |
| **Heroic Games Launcher**   | Front‑end for installing and launching games on Linux. | [Install via Flathub](https://flathub.org/en/apps/com.heroicgameslauncher.hgl) |

> **Important**  
> Download the evergreen bootstrapper for Microsoft Edge WebView2 and save it to your `Downloads` folder.  
> Then download the Stove client using the link above or a search engine.

![Heroic Settings](images/czn/webview1.png)

---

## 1️⃣ Fuagus Launcher Version

1. Open **Fugaus Launcher**.  
2. Go to *Settings* → *Proton Manager* and download the latest available Proton.  

   ![Graphics Tab](images/czn2/image9.png)  
   ![Graphics Tab](images/czn2/image10.png)

3. Click the **+** button, add the name of the game, then click the search icon and locate the `STOVE.exe` you downloaded earlier.

   ![Add Game](images/czn2/image1.png)  








![X11 Configuration](images/czn2/image3.png)
5. Set Proton to the version you downloaded, then press **OK**.  
6. Click **Play** – Stove will install quickly, accepting terms and defaults.



![Graphics Tab](images/czn2/image11.png)
![Graphics Tab](images/czn2/image12.png)

Once Stoe finished installing.
Right‑click the CZN entry ON Faugus Launcher, choose **Edit**, then click **Run** and locate your Microsoft Edge WebView evergreen bootstrapper executable.

![Wine Install](images/czn2/image4.png)
![Graphics Tab](images/czn2/image6.png)







Once you  Webview  is installed you’ll need to apply one of two fixes:

* For most users (Wayland): set the environment variable

  ```bash
  PROTON_ENABLE_WAYLAND=1
  ```

  ![Winecfg – Wayland](images/czn2/image7.png)


## Alternate method instead of enabvle wayland – for X11/Linux Mint( but any distro can do this method aswell)

If you’re running an X11 session (i3, XFCE, Qtile, dwm, Linux Mint, etc.) the following steps apply:

1. Open **Tools → WINECFG** (Wine configuration).  
2. Click **Install** to open the configuration window.  
3. Go to the **Graphics** tab.  
4. Check **Emulate virtual desktop** and adjust the size if desired.  
5. Click **Apply**, then **OK**.

  ![Winecfg – Wayland](images/czn2/image8.png)
![Wine Install](images/czn/image4.webp)
![Graphics Tab](images/czn/image5.webp)



## 4️⃣  Launch the Stove and you can Install it and play





