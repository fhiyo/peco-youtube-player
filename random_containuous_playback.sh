#!/bin/bash

. ./settings/playlist_dir.sh

readonly RAND_PLAYLIST_FILE="${PLAYLIST_DIR}/playlist_rand.txt"

if [ $# -gt 1 ]; then
	echo "usage: $0  OR  $0 --update"
	exit 1
elif [ $# -eq 1 ] && [ "$1" == "--update" ]; then
	python GetYoutubePlaylist.py > ${PLAYLIST_DIR}/playlist.json
fi

if [ -e ${RAND_PLAYLIST_FILE} ]; then
	rm ${RAND_PLAYLIST_FILE}
fi

playlist=`cat ${PLAYLIST_DIR}/playlist.json`
max_length=$( echo ${playlist} | jq 'length' )
length=${max_length}
for i in `seq 1 ${max_length}` ; do
	rand=$(jot -r 1 0 ${length})
	# echo "rand:" ${rand}
	selectVideo=$(echo ${playlist} | jq --argjson rnd ${rand} '.[$rnd]')
	selectVideoTitle=$(echo ${selectVideo} | jq '.videoTitle')
	selectVideoId=$(echo ${selectVideo} | jq -r '.videoId')

	# echo "selectVideoTitle:" ${selectVideoTitle}
	echo 'https://www.youtube.com/watch?v='${selectVideoId} >> ${RAND_PLAYLIST_FILE}

	playlist=$(echo ${playlist} | jq --argjson rnd "${rand}" 'del(.[$rnd])')
	length=$(( length - 1 ))
	# echo "playlist:" ${playlist}
done

# echo "playlist:" ${playlist}

mpv --playlist ${RAND_PLAYLIST_FILE}

