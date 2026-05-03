+++
title = "Umamusume: Pretty Derby on Linux"
date =  "2025-12-09"
showTableOfContents = true
featureimage = "/images/uma/thumb.jpg"
+++


{{< youtube _U5Pnpa8Xfg >}}

## 1. Install Steam for your distro then install Uma Musume and just try playing with default Steam Settings

This should work for most of you.
To install steam best advice is to search youtbe /search engine for how to install steam for your distro (or its preinstalled already).

Will add some guides here soon.

If the game does not launch move onto Step 2 (specifically for white screen fix).If something else is worng comment or ask in discord.
![Alt text](images/uma/uma2.gif )

## 2.Try the media encorder unlock to fix the white screen issue

Copy these commands into your Terminal/Konsole app

Either close you steam by right clciking then selecting exit Steam with the taskbar icon or  run this command
```bash
killall steam      
```

Once steam is closed or already closed run this command. It should launch steam for your with the corect settings. Only have to do this once on a new steam install.
Fixes other games if they were not working before.

```bash
steam steam://unlockh264/
```

Thats it and your Umamusame should no longer have a white screen.
WE CAN PLAY!!!!
![Alt text](images/uma/uma1.gif )
### If You’re Using the Flatpak Version of Steam (Most people are not using the steam flatpak)

If you get  *“steam: command not found.”*  then you probably have the flatpak for Steam
You can still unlock the codec with:

Either close you steam by right clciking the taskbar icon or 
```bash
flatpak kill com.valvesoftware.Steam     
```

Once steam is closed or already closed run this command. (Same explanation as above)
```bash
xdg-open steam://unlockh264/
```

> **Tip:** Unless you have a specific reason to use the Flatpak the native package for your distribution is what I recommend.

Once Steam has restarted (you’ll see the “Unlock H.264” dialog), launch the game again – the white‑screen issue should be resolved.



# 3. If none of that works just use Proton-GE instead 
Can follow the video guide


{{< youtube NFQopxdhVlM >}}

### ProtonPlus
Install ProtonPlus from Flathub or native package on:  
https://flathub.org/en/apps/com.vysp3r.ProtonPlus  
Or search for **ProtonPlus** in your software/app manager.




### Open ProtonPlus


![Alt text](images/uma/protonplus.png )Download the latest Proton-GE after selecting Steam in top left

### Set Umamusume to use Proton-GE Latest in Compatbility in ProtonPlus
![Alt text](images/uma/protonplus2.png)
Go on the Games section on ProtonPlus and set Uma to use Proton-GE
All done can play now with best compability settings


# Alternative Steps
Still had to have followed the steps to isntall Proton-GE on Steam first
### Set Umamusume to use Proton-GE Latest in Compatbility in Steam
![Alt text](images/uma/image2.png )Press the cog icon on your Steam for Uma Musame
![Alt text](images/uma/image3.png )Go into Compability and select Proton-GE

Can use Proton-CachyOS aswell


## If the game does not launch with Proton-GE 


If for some reason nothing works then try the last resort



## Enjoy the game

