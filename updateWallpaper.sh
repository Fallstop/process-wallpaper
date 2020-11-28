#!/bin/bash
cd /home/fallstop/Documents/projects/process-wallpaper/
echo "Creating wallpaper..."
touch asdkjasbd

top -b -n 1 > top.out
nice python3 generateWallpaper.py

echo "Updating Desktop"
WALLPAPER_PATH="$/home/fallstop/Documents/projects/process-wallpaper/wallpaper.png"

qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops(); print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = "org.kde.slideshow";d.currentConfigGroup = Array("Wallpaper", "org.kde.slideshow", "General");d.writeConfig("SlidePaths", "'${WALLPAPER_PATH}'")}'
