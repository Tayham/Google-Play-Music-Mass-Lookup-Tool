import io
import os
import sys

import music
from api import GooglePlayMusic
from settings import Settings

# TODO: DIRECT IMPORT TEXT FROM YOUTUBE / SOUNDCLOUD
# TODO: OPEN SONG STREAMS IN CONSOLE NOT IN BROWSER
# TODO: AUTOMATICALLY ADD LIKED SONGS TO LIBRARY FOR CERTAIN PLAYLIST FUNCTION
# TODO: SAVE ADDED SONGS TO A TEXT FILE FOR TRACKING

# VARIABLES
settings = Settings()
results = music.Results()


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
if settings.check_for_attribute('Login', 'loginpath'):  # If there is a specified login path in settings.ini
    login_path = settings.section('Login')['loginpath']
    with io.open(login_path, "r") as login_file:
        credentials = login_file.readlines()
    login_file.close()
else:
    credentials = [settings.section('Login')['username'], settings.section('Login')['password']]
if settings.check_for_attribute('Login', 'mobileid'):
    device_id = settings.section('Login')['mobileid']
elif len(credentials) == 3:
    device_id = credentials[2]
else:
    device_id = ''

g_music = GooglePlayMusic(credentials, device_id)

if g_music.is_logged_in():
    # IMPORT MUSIC TO AN ARRAY
    if settings.check_for_attribute('Directory', 'musicpath'):  # If there is a specified music path in settings.ini
        music_path = settings.section('Directory')['musicpath']
    else:
        music_path = os.path.join(sys.path[0], "music.txt")

    with io.open(music_path, "r") as music_file:
        music_list = music_file.readlines()
        print(music_list)
        print("Amount of Songs to look-up: " + str(len(music_list)))
    music_file.close()

    # NORMALIZE
    if yes_or_no("Try to normalize the input data?"):
        for i in range(0, len(music_list)):
            music_list[i] = music.normalize(music_list[i])

    for i in range(0, len(music_list)):
        song_list = g_music.song_search(music_list[i])
        if len(song_list) > 0:  # If there are search results
            # PICK WHICH SONG FROM RESULTS TO STREAM
            song_to_add = 1  # Reset songToAdd
            while song_to_add != 0:
                song_to_add = int(input_number("What song to select? 0 to cancel\n", len(song_list)))
                if song_to_add != 0:
                    s = song_list[song_to_add - 1]
                    if yes_or_no("Play song?"):
                        print("PLAYING: " + s.description())
                        s.open_link()
                    if yes_or_no("Add to library?"):
                        s.storeId = g_music.add_store_tracks(s.storeId)
                        print("Library Track ID: " + str(s.storeId))
                        results.add_result(s, "ADDED TO LIBRARY")
                        results.display_results()
                        song_to_add = 0
        else:
            print("NO RESULTS FOR THAT SEARCH... SEARCHING NEXT SONG\n")
    print("~~~ Finished ~~~")
    results.display_results()
    print("Logging Out...")
    print('Logged in: ' + str(g_music.logout()))  # True if successful logout
else:
    print("LOGIN FAILED")
