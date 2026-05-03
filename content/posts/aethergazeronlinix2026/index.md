+++
title = "Aether Gazer on Linux – Older GPU Guide"
date  = "2026-03-01"
showTableOfContents = true
featureimage = "/images/ag/thumb.jpg"
+++



## GPU Related Issues

If *Aether Gazer* fails to launch because your GPU does not support the required DX11 or Vulkan version (when using **Proton‑GE** or **Proton‑CachyOS**), you can resolve the issue in one of two ways:

1. **Install Proton‑Sarek** – the latest official Proton build that adds better Vulkan support for older GPUs.  
2. **Force Wine DX9 via an environment variable** (`PROTON_USE_WINED3D=1`).

---

### 1. Install Proton‑Sarek from ProtonPlus

ProtonPlus bundles the newest Proton releases, including Proton‑Sarek.

| Source | Link |
|--------|------|
| Flathub | <https://flathub.org/en/apps/com.vysp3r.ProtonPlus> |
| GitHub  | <https://github.com/Vysp3r/protonplus> |

#### Steps
1. **Download ProtonPlus**  
   * From Flathub, click the green “Install” button.  
   * From GitHub, download the native package for your distribution (RPM for Fedora/Red Hat, DEB for Debian/Ubuntu, or an Arch‑PKG for Arch) and install it with your system’s package manager.

> **Coming soon:** A step‑by‑step Heroic installer guide will be added to this page. Stay tuned!

2. **Open ProtonPlus** and select the launcher you use (Heroic in this case) in the top‑left drop‑down menu.

3. Click **“Install Proton‑Sarek Latest”** by pressing the download icon.
![Graphics Tab](images/ag/hgl/image5.png)
4. **Re‑launch Heroic** and change *Aether Gazer*’s Wine/Proton version to **Proton‑Sarek Latest**.

5. Launch the game – it should now start normally.
![Graphics Tab](images/ag/hgl/image3.png)
![Graphics Tab](images/ag/hgl/image4.png)

6. Then Play and have fun!


---

### 2. Force Wine DX9 with an Environment Variable

If your hardware is older than what Proton‑Sarek supports, you can fall back to Wine’s DirectX 9 renderer.



#### Steps

1. In your Aether Gazer's Settings Page(right click then Settings) go to the **Advanced** settings and  add the following environment variable:


![Graphics Tab](images/ag/hgl/image3.png)

> **Note:**  
> Use the copy button on this guide when you hover 
   ```text
   PROTON_USE_WINED3D=1
   ```
  ![Graphics Tab](images/ag/hgl/image6.png)


2. Then Play and have fun!


> **Note:**  
> `PROTON_USE_WINED3D` tells Proton to use the OpenGL‑based *wined3d* backend instead of the Vulkan‑based DXVK for D3D10/D3D11.  
