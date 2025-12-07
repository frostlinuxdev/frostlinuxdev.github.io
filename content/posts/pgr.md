+++
title = "Punishing Gray Raven on Linux"
date =  "2025-12-04"
+++

### We need to get bbe installed on our Linux Desktops System

### Steam Deck users would need another video/guide but PGR official server does have a good guide and help section using the Universal Method.


# Install **bbe** on Ubuntu/Debian Distros

Using a  debian/ubuntu based distro (Linux Mint,Ubuntu,Debian,,PopOS,PikaOS,Zorin)

To install the Binary Block Editor (**bbe**) on Ubuntu, run:

```bash
sudo apt update
sudo apt install bbe
```
# Install bbe on Arch via yay
Using an Arch based distro(Arch,CachyOS,EndevourOS, I know you know you're on Arch) 

(not Steam Deck check PGR discord or Steam Deck/Univseral Guide that will covered soon if not already)

This package is installed form Arch User Repo

https://aur.archlinux.org/packages/bbe

```bash
sudo pacman -S yay
yay -S bbe
```
# Install bbe on Fedora via COPR

Using a Fedora based distro (Fedora,Nobara,ect)

Will be using this copr package to install BBE

https://copr.fedorainfracloud.org/coprs/adrianl40/bbe/

Enable the COPR repo:

```bash
sudo dnf copr enable adrianl40/bbe
sudo dnf install bbe
```


# Confirm BBE is installed

After installed confirm with:

```bash
bbe --version
```


#  Fixing the Launcher  to not be Transparent after installed with Proton/Wine Runner

Open a terminal inside that directory (should be the version directory where the name is a version number)
Paste this command in:
```bash

mv launcher_main.dll launcher_main.dll.bak
bbe -e "s/\x12AllowsTransparency/\x09IsEnabled\x1bA\x00\x03AAAAA/" launcher_main.dll.bak > launcher_main.dll
```



This is a the same as the command above just split up.
You have to add the path of the launcher_maill.dll yourself.
```bash
mv "/path/to/Punishing Gray Raven/#.#.#.#/launcher_main.dll" "/path/to/Punishing Gray Raven/#.#.#.#/launcher_main.dll.bak"

bbe -e "s/\x12AllowsTransparency/\x09IsEnabled\x1bA\x00\x03AAAAA/" "/path/to/Punishing Gray Raven/#.#.#.#/launcher_main.dll.bak" > "/path/to/Punishing Gray Raven/#.#.#.#/launcher_main.dll"
```

  
This does not alter the game in any way! 
It simply disables Transparency inside the launcher to allow the launcher to render. 

