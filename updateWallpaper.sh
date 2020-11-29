#!/bin/bash
cd /home/fallstop/Documents/projects/process-wallpaper/
echo "Creating wallpaper..."
touch asdkjasbd

top -b -n 1 > top.out
nice python3 generateWallpaper.py

echo "Updating Desktop"
WALLPAPER_PATH="$/home/fallstop/Documents/projects/process-wallpaper/wallpaper.png"


