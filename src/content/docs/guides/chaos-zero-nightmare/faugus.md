---
title: "Chaos Zero Nightmare on Linux: Faugus Launcher Guide (Stove + WebView2)"
description: "Play Chaos Zero Nightmare on Linux with Faugus Launcher. Add Stove and WebView2 to a Wine prefix, then fix the install freeze and crashpad_handler.exe."
sidebar:
  label: "Faugus Launcher"
image: "/images/czn2/hero.webp"
tags: ["chaos-zero-nightmare", "faugus", "stove", "gacha"]
---

:::note
This is the **[Faugus Launcher](https://flathub.org/en/apps/io.github.Faugus.faugus-launcher)** method. The shared prerequisites (Stove, WebView2 and downloads), the install-freeze fix and the crashpad fix live on the [Chaos Zero Nightmare overview](/guides/chaos-zero-nightmare/).
:::

Faugus Launcher is the recommended method now — [Heroic](https://flathub.org/en/apps/com.heroicgameslauncher.hgl) has had issues after the Season 2 update.

## Add Chaos Zero Nightmare to Faugus

1. Open **Faugus Launcher**.
2. Go to **Settings > Proton Manager** and download the latest available Proton.

   ![Faugus Launcher settings with Proton Manager](/images/czn2/image9.webp)
   ![Faugus Launcher downloading the latest Proton](/images/czn2/image10.webp)

3. Click the **+** button, enter the name of the game, click the search icon and locate the `STOVE.exe` you downloaded earlier.

   ![Faugus Launcher add game dialog](/images/czn2/image1.webp)
   ![Faugus Launcher selecting STOVE.exe](/images/czn2/image2.webp)
   ![Faugus Launcher game settings](/images/czn2/image3.webp)

4. Set Proton to the version you downloaded and press **OK**.
5. Click **Play**. Stove installs quickly, so accept the terms and defaults.

   ![Stove installer running in Faugus Launcher](/images/czn2/image11.webp)
   ![Stove installation finishing in Faugus Launcher](/images/czn2/image12.webp)

6. Once Stove has finished installing, right-click the Chaos Zero Nightmare entry in Faugus Launcher, choose **Edit**, click **Run** and locate your Microsoft Edge WebView evergreen bootstrapper executable.

   ![Faugus Launcher edit menu to run the WebView2 bootstrapper](/images/czn2/image4.webp)
   ![Selecting the WebView2 evergreen bootstrapper executable](/images/czn2/image6.webp)

### Launch Stove from Faugus

Copy the prefix path you used when installing Stove and paste it into the **Prefix** box. Then click **Search** and locate your `STOVE.exe`. It looks like this:

```text
/home/user/Faugus/prefix_name/drive_c/ProgramData/Smilegate/STOVE/STOVE.exe
```

For example, if the user is `frost` and the prefix is called `czn2`:

```text
/home/user/Faugus/czn2/drive_c/ProgramData/Smilegate/STOVE/STOVE.exe
```

![Faugus Launcher prefix box for Stove](/images/czn2/image14.webp)
![Locating STOVE.exe inside the Faugus prefix](/images/czn2/image15.webp)

Once the executable is found, click **Run** to start Stove.

## Troubleshooting

- **Install freezes:** see [Fix: install freeze](/guides/chaos-zero-nightmare/#fix-install-freeze-wayland-or-x11).
- **Stove will not launch afterwards:** see [crashpad_handler.exe](/guides/chaos-zero-nightmare/#stove-not-launching-crashpad_handlerexe).
