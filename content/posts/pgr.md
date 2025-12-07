+++
title = "Punishing Gray Raven on Linux"
date =  "2025-12-04"
+++
LAUNCHER TUTORIAL




### 1. Install BBE

How to install bbe

bbe is a program that is used to edit binary files, it is specifically used to edit the launcher executable in the tutorial.

Download bbe 0.2.2.1 to your downloads folder from https://archive.org/download/archlinux_pkg_bbe
bbe-0.2.2-1-x86_64.pkg.tar.xz

### 2. Extract binary
``` bash
mkdir -p ~/bbe-temp
cd ~/bbe-temp
bsdtar -xf ~/Downloads/bbe-0.2.2-1-x86_64.pkg.tar.xz
```

### 3. Copy to user path
```bash
mkdir -p ~/bin
cp usr/bin/bbe ~/bin/
```

### 4. Add ~/bin to your path (if it isn't already)

```bash
nano ~/.bashrc
```
Use **down arrow key** to go bottom of the file and copy the below text
```bash
export PATH="$HOME/bin:$PATH"
```
Press **Ctrl + X**, then **Y** to save, and **Enter** to save the file.

```bash
"source ~/.bashrc"
```
### 5. Verify BBE is installed
Verify bbe is installed, and ~/bin has been added to your path
```bash
bbe --version
```
If you are on CachyOS or another distro that uses 
```bash
bash
```
Wait for bash prompt then 
```bash
bbe --version
```

### 6. Patching the Launcher

Locate where the PGR launcher got installed, it should usually be in ~/.wine/drive_c/Program Files/Punishing Gray Raven/x.y.z.w/ (x.y.z.w is current launcher version)

Open a terminal inside that directory (should be the version directory where the name is a version number)
Paste this command in:
```bash
mv launcher_main.dll launcher_main.dll.bak
bbe -e "s/\x12AllowsTransparency/\x09IsEnabled\x1bA\x00\x03AAAAA/" launcher_main.dll.bak > launcher_main.dll
```

  
This does not alter the game in any way! 
It simply disables Transparency inside the launcher to allow the launcher to render. 

Run the launcher_main.exe with proton not wine.

## YOU WILL NEED TO RE-PATCH THE LAUNCHER EVERYTIME IT UPDATES!!

## AS OF 4.0 IT IS REQUIRED YOU USE PROTON-CACHYOS!!!!
