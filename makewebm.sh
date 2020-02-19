#!/bin/sh

[ "$#" -ne "1" ] && echo "Needs one argument!" >&2 && exit 1
! [ -d "$1" ] && echo "$1 is not a directory!" >&2 && exit 2

ffmpeg -framerate 20 -i "$1"/%05d.png -threads 16 "$1".webm
