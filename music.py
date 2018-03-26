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


class Results:
    results = []

    # def __init__(self):

    def add_result(self, song, operation):
        self.results.append(song.description() + " " + operation)
