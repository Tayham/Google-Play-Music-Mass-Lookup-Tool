import io
import re
import webbrowser

import os

import sys
from gmusicapi import Mobileclient
from music import Song
from settings import Settings


class GooglePlayMusic:
    g_music = Mobileclient()

    def __init__(self, credentials):
        print("Logging In.... ")
        print('Logged in: ' + str(
            self.g_music.login(credentials[0], credentials[1], Mobileclient.FROM_MAC_ADDRESS)))  # True if successful

    # GET RESULTS FOR SONG
    def song_search(self, song):
        song_list = []
        counter = 1
        print("SONG: " + song)
        print("~~~~~~ RESULTS ~~~~~~")
        search_result = self.g_music.search(song, max_results=5)
        search_result_songs = search_result['song_hits']
        for track in search_result_songs:
            track_info = track['track']
            current_track = Song()
            current_track.info = (track_info['artist'] + ' - ' + track_info['title'])
            current_track.link = self.g_music.get_stream_url(track_info['storeId'], device_id=None, quality=u'hi')
            current_track.storeId = track_info['storeId']
            song_list.append(current_track)
            print(str(counter) + ': ' + current_track.description())
            counter = counter + 1
        return song_list

    def add_store_tracks(self, storeId):
        self.g_music.add_store_tracks(storeId)
