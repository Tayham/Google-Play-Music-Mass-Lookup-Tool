import io
import os
import sys

import music
from api import GooglePlayMusic
from settings import Settings

# VARIABLES
settings = Settings()
use_this_directory = False

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


#  GET LOGIN INFORMATION AND LOGIN
if settings.check_for_login_path():  # If there is a specified login path in settings.ini
    login_path = settings.section('Login')['loginpath']
    with io.open(login_path, "r") as login_file:
        credentials = login_file.readlines()
        g_music = GooglePlayMusic(credentials)
    login_file.close()
else:
    credentials = [settings.section('Login')['username'], settings.section('Login')['password']]
    g_music = GooglePlayMusic(credentials)

# IMPORT MUSIC TO AN ARRAY
if settings.check_for_music_path():  # If there is a specified login path in settings.ini
    music_path = settings.section('Directory')['musicpath']
else:
    music_path = os.path.join(sys.path[0], "music.txt")

with io.open(music_path, "r") as music_file:
    music_list = music_file.readlines()
    print(music_list)
    print("Amount of Songs to look-up: " + str(len(music_list)))
login_file.close()

# NORMALIZE
if yes_or_no("Try to normalize the input data?"):
    for i in range(0, len(music_list)):
        music_list[i] = music.normalize(music_list[i])

for i in range(0, len(music_list)):
    song_list = g_music.song_search(music_list[i])
    # PICK WHICH SONG FROM RESULTS TO STREAM
    song_to_add = 1  # Reset songToAdd
    while song_to_add != 0:
        song_to_add = int(input_number("What song to play? 0 to cancel\n", len(song_list)))
        if song_to_add != 0:
            s = song_list[song_to_add - 1]
            print(s.description())
            s.open_link()
            if yes_or_no("Add to library?"):
                g_music.add_store_tracks(s.storeId)

    # TODO: SAVE ADDED SONGS TO A TEXT FILE FOR TRACKING

print("~~~ Finished ~~~")
print("Logging Out...")
print('Logged in: ' + str(g_music.logout()))  # True if successful logout
