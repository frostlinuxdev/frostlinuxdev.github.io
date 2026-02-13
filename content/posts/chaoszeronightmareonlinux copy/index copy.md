+++
title = "Chaos Zero Nightmare on Linux"
date  = "2026-01-30"
+++


# Youtube Guide
{{< youtube YBVMvz0JN8A>}}
## What you’ll need for this guide

| Item                        | Description                                           | Download link |
|-----------------------------|-------------------------------------------------------|---------------|
| **Stove Client**            | Official client to play the game on Linux.           | [Download here](https://store.onstove.com/en/download) |
| **Microsoft Edge WebView2** | Runtime required by Stove (provides the web‑view component). | [Get it from Microsoft here](https://developer.microsoft.com/en-us/microsoft-edge/webview2?form=MA13LH) |
| **Heroic Games Launcher**   | Front‑end for installing and launching games on Linux. | [Install via Flathub](https://flathub.org/en/apps/com.heroicgameslauncher.hgl) |

> *Important:*  
> Download the Evergreen Bootstrapper for Microsoft Edge WebView2 and save it to your `Downloads` folder 
![Heroic Settings](images/czn/webview1.png)
> Download the Stove Client use link above or search engine
![Heroic Settings](images/czn/stovedl.png)

First open Fugaus Luancher
then go to settinsg ,Porotn Mnager and donwload th elatets Poroton aviable so (faugus does not donwload it everytime )
![Graphics Tab](images/czn2/image9.png)
![Graphics Tab](images/czn2/image10.png)

then press the plus button
![Graphics Tab](images/czn2/image1.png)
Add the name of the game
then press the search icon and locate your stove exe you downloaded earlier

![Graphics Tab](images/czn2/image2.png)
 set the proton to the verrsion you downloaded then press ok


 then press play and install stove should be fast accepts terms and defaults


/home/frost/Faugus/czn2/drive_c/ProgramData/Smilegate/STOVE/STOVE.exe
/home/frost/Faugus/czn2

![X11 Configuration](images/czn2/image3.png)

then right lcick edit your czn game then press run adn locate yoru microsoft evie ewebview evergreen boostrapper exe.

![Wine Install](images/czn2/image4.png)
![Graphics Tab](images/czn2/image5.png)
![Graphics Tab](images/czn2/image6.png)

now once that is installed you want to do one of the two fixes
if you are most fo you should just use wine wayland fix copy thee below command(unless  you are on linux mint or x11)
![Graphics Tab](images/czn2/image7.png)
for x11 users /linux mint or you just want to us ethis method press winecfg
![Graphics Tab](images/czn2/image8.png)




## 4️⃣  Launch the game

Start Chaos Zero Nightmare from Heroic (or whatever launcher you use).  
The installation‑freeze bug should no longer appear.

If you need to revert the changes, simply uncheck the “Emulate virtual desktop” box or disable Wine Wayland again.



```bash
PROTON_ENABLE_WAYLAND=1
```

3. Press OK and you are good to go to open Stove and install CZN

