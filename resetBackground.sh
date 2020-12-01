#!/bin/bash
export "binpath=/home/fallstop/Documents/projects/process-wallpaper/"
"DISPLAY=:$(ls -1 /tmp/.X11-unix/X* | grep -oE "[0-9]*$" | sort -n | head -1)"
export "DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus"
(
    pushd "${binpath}" && cp backgroundImage.png wallpaper.png && ./setWallpaper.sh
    popd
) 2>&1 | logger -t "process-wallpaper"

