#!/usr/bin/env python

# TODO: transfer video title to peco to select from it
#       add function of auto play

import httplib2
import os
import sys
import json
import subprocess

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

MY_PLAYLIST_ID = "PLdrDXAFDBAgozp9ts88xYpRz0PXB1W1N8"
MAX_RESULT = 50
CLIENT_SECRETS_FILE = os.path.join(os.path.expanduser("~"), ".config/googleapi/youtube/client_secrets.json")

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the Developers Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

# This OAuth 2.0 access scope allows for read-only access to the authenticated
# user's account, but not other types of account access.
YOUTUBE_READONLY_SCOPE = "https://www.googleapis.com/auth/youtube.readonly"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_youtube_playlist():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
      message=MISSING_CLIENT_SECRETS_MESSAGE,
      scope=YOUTUBE_READONLY_SCOPE)

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
      flags = argparser.parse_args()
      credentials = run_flow(flow, storage, flags)

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
      http=credentials.authorize(httplib2.Http()))

    # Retrieve the contentDetails part of the playlist resource for the
    # authenticated user's playlist.
    playlists_response = youtube.playlistItems().list(
      part="snippet",
      playlistId=MY_PLAYLIST_ID,
      maxResults=MAX_RESULT,
    ).execute()

    nextPageToken = playlists_response["nextPageToken"]
    myPlayListInfo = []

    nth=1

    for item in playlists_response["items"]:
        myPlayListInfo.append({"num": nth, "videoId": item["snippet"]["resourceId"]["videoId"], "videoTitle": item["snippet"]["title"]})
        nth += 1

    while nextPageToken is not None:
        playlists_response = youtube.playlistItems().list(
                part="snippet",
                playlistId=MY_PLAYLIST_ID,
                maxResults=MAX_RESULT,
                pageToken=nextPageToken,
                ).execute()
        if playlists_response.has_key("nextPageToken"):
            nextPageToken = playlists_response["nextPageToken"]
        else:
            nextPageToken = None
        for item in playlists_response["items"]:
            myPlayListInfo.append({"num": nth, "videoId": item["snippet"]["resourceId"]["videoId"], "videoTitle": item["snippet"]["title"]})
            nth += 1

        # subprocess.call(['mpv', "https://www.youtube.com/watch?v=%s" % videoIdList[30]])

    return json.dumps(myPlayListInfo)

def main():
    print get_youtube_playlist()

if __name__ == '__main__':
    main()

