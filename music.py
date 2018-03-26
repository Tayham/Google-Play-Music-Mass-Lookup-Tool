import re
import webbrowser


def normalize(song_text):
    # print("ORIGINAL: " + song_text)
    song_text = re.sub("[(\[].*?[)\]]", "", song_text)  # Remove parentheses () and brackets []
    song_text = song_text.lstrip()  # Remove whitespace on left side
    song_text = song_text.rstrip()  # Remove whitespace on right side
    return song_text
    # print("NORMALIZED: " + song_text)


class Song:
    info: ""
    link: ""
    storeId: ""

    def description(self):
        return self.info

    def open_link(self):
        webbrowser.open(self.link)  # Open browser to song stream link

    def __init__(self, s):
        info = (s['artist'] + ' - ' + s['title'] + ' (' + s['album'] + ' - ' + s['albumArtist'] + ')')
        if s['explicitType'] == '1':
            info = info + " [EXPLICIT]"
        self.info = info
        self.storeId = s['storeId']


class Results:
    def __init__(self):
        self.results = []

    def add_result(self, song, operation):
        self.results.append(operation + ": " + song.description())

    def display_results(self):
        print(self.results)
