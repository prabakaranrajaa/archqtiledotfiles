#!/bin/bash

# Folder containing wallpapers
WALLPAPER_DIR="$HOME/Pictures/Wallpapers"

# Pick a random file from the folder
RANDOM_WALL=$(find "$WALLPAPER_DIR" -type f | shuf -n 1)

# Run swww with transition options
swww img "$RANDOM_WALL" \
  --transition-fps 255 \
  --transition-type outer \
  --transition-duration 0.8

