import io
import re
import webbrowser

import os

import sys
from gmusicapi import Mobileclient

api = Mobileclient()

class Song:
    info: ""
    link: ""
    storeId: ""

    def description(self):
        return self.info + self.link


def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False


def input_number(message, max_value):
    while True:
        try:
            user_input = int(input(message))
            if user_input > max_value:
                print("Int is out of range! Try again")
                continue
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return user_input


#  GET LOGIN INFORMATION FROM "login.txt" AND LOGIN
with io.open(os.path.join(sys.path[0], "login.txt"), "r") as login:
    credentials = login.readlines()
    print("Logged In: ")

    print(api.login(credentials[0], credentials[1],
                    Mobileclient.FROM_MAC_ADDRESS))  # True if successful login
login.close()

# IMPORT MUSIC TO AN ARRAY
with io.open(os.path.join(sys.path[0], "music.txt"), "r") as text_file:
    musicList = text_file.readlines()
    print(musicList)
    print("Amount of Songs to look-up: " + str(len(musicList)))
text_file.close()

# NORMALIZE
if yes_or_no("Try to normalize the input data?"):
    for i in range(0, len(musicList)):
        # print("ORIGINAL: " + musicList[i])
        musicList[i] = re.sub("[(\[].*?[)\]]", "", musicList[i])  # Remove parentheses () and brackets []
        musicList[i] = musicList[i].lstrip()  # Remove whitespace on left side
        musicList[i] = musicList[i].rstrip()  # Remove whitespace on right side
        # print("NORMALIZED: " + musicList[i])

# GET RESULTS FOR SONG
for i in range(0, len(musicList)):
    songList = []
    counter = 1
    print("SONG: " + musicList[i])
    print("~~~~~~ RESULTS ~~~~~~")
    searchResult = api.search(musicList[i], max_results=5)
    searchResultSongs = searchResult['song_hits']
    for track in searchResultSongs:
        trackInfo = track['track']
        x = Song()
        x.info = (trackInfo['artist'] + ' - ' + trackInfo['title'] + '\n')
        x.link = api.get_stream_url(trackInfo['storeId'], device_id=None, quality=u'hi')
        x.storeId = trackInfo['storeId']
        songList.append(x)
        print(str(counter) + ': ' + x.description())
        counter = counter + 1

    # PICK WHICH SONG FROM RESULTS TO STREAM
    songToAdd = 1  # Reset songToAdd
    while songToAdd != 0:
        songToAdd = int(input_number("What song to play? 0 to cancel\n", counter - 1))
        if songToAdd != 0:
            s = songList[songToAdd - 1]
            print(s.description())
            webbrowser.open(s.link)  # Go to song stream link
            if yes_or_no("Add to library?"):
                api.add_store_tracks(s.storeId)
    # TODO: SAVE ADDED SONGS TO A TEXT FILE FOR TRACKING
print("~~~ Finished ~~~")
print("Logged Out: ")
print(api.logout())  # True if successful logout
