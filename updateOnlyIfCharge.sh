#!/bin/bash 
BatteryFile="/home/fallstop/Documents/projects/process-wallpaper/BatteryMode.temp"

if [ ! -e $BatteryFile ]; then
    ./run.sh
fi