#!/bin/bash

if [ $# -gt 1 ]; then
	echo "usage: $0  OR  $0 --update"
	exit 1
elif [ $# -eq 1 ] && [ "$1" == "--update" ]; then
	python get_youtube_playlist.py > playlist.json
fi

playlist=`cat playlist.json`
videoTitle=$(echo ${playlist} | jq -r '.[].videoTitle' | peco)

# echo ${playlist}

# echo "videoTitle:" ${videoTitle}

if [ $? -ne 0 ]; then
	exit 1
fi

videoId=$(echo ${playlist} | jq -r --arg title "${videoTitle}" '.[] | select(.videoTitle == $title) | .videoId')

# echo "videoId:" ${videoId}

mpv "https://www.youtube.com/watch?v=${videoId}"

