#!/bin/bash

. ./settings/playlistdir.sh

if [ $# -gt 1 ]; then
	echo "usage: $0  OR  $0 --update"
	exit 1
elif [ $# -eq 1 ] && [ "$1" == "--update" ]; then
	python get_youtube_playlist.py > ${PLAYLIST_DIR}/playlist.json
fi

# readonly PLAYLIST_DIR=playlist

playlist=`cat ${PLAYLIST_DIR}/playlist.json`
videoTitle=$(echo ${playlist} | jq -r '.[].videoTitle' | peco)

if [ $? -ne 0 ]; then
	exit 1
fi

videoId=$(echo ${playlist} | jq -r --arg title "${videoTitle}" '.[] | select(.videoTitle == $title) | .videoId')

# echo "videoId:" ${videoId}

mpv "https://www.youtube.com/watch?v=${videoId}"

