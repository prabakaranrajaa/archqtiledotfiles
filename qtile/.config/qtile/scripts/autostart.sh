#!/bin/bash
dunst &
xrandr --output eDP-1 --same-as HDMI-1 &
xinput set-button-map 15 3 2 1 &
picom --config ~/.config/picom/picom.conf &
#feh --bg-scale ~/Pictures/Wallpapers/kill.jpeg &

