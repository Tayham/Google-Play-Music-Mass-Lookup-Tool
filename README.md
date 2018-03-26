# Google Play Music Mass Lookup Tool
A command line tool written in Python to lookup a mass amount of songs on google play music to see if they are available on the service. Useful if you want to import a Youtube or Soundcloud playlists to Google Play Music. Made possible by Simon Weber and his awesome [Unofficial Google Play Music API](https://github.com/simon-weber/gmusicapi)
___
## Setup & Information
*This tool preforms **TEXT LOOK-UP ONLY** and does not preform audio matching.*
* ### settings.ini
   * #### Login
      * Replace ```MyUsername``` with your Google User Name
      * Replace ```MyPassword``` with your Google Password
      * If you want to put your login information in a text file in a different directory and not use the credentials in the settings.ini file add the text file path to the ```LoginPath: ``` attribute.
   * #### Directory
      * If you want to change the path from the default for the music.txt file add the text file path to the ```MusicPath: ``` attribute

## Text File Formatting
* ### login.txt
    * Replace ```GOOGLE USER NAME HERE``` with your Google User Name
    * Replace ```GOOGLE PASSWORD HERE``` with your Google Password
     
    
* ### music.txt
    * Add the text lookups you want to perform with each seperate music search query seperated by a newline.
## Packages Needed
* [Unofficial Google Play Music API](https://github.com/simon-weber/gmusicapi) - [Installation instructions](http://unofficial-google-music-api.readthedocs.io/en/latest/usage.html#usage)
 ```$ pip install gmusicapi```
___
### Written in Python 3
