import os
import sys
import configparser


class Settings:
    # Settings file for program
    settings = configparser.ConfigParser()

    def __init__(self):
        Settings.settings.read(os.path.join(sys.path[0], 'settings.ini'))

    def section(self, section):
        dictionary = {}
        options = Settings.settings.options(section)
        for option in options:
            try:
                dictionary[option] = self.settings.get(section, option)
                if dictionary[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dictionary[option] = None
        return dictionary

    def check_for_attribute(self, section, attribute):
        if self.section(section)[attribute]:  # if LoginPath is not blank
            return True
        else:
            return False
