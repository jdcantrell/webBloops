# Goal
With this project I want to create an easy to setup and use music sharing
system. Music should be able to be streamed directly off the page using HTML5
and navigation should be done with an elegant cover flow style display.

# To Do
1. Index base folder
2. Create html prototype for navigation
3. Figure out how to serialize/store folders (thinking of creating html files)
4. Get the audio player in place
5. Start looking into how a playlist will work

# Nice to haves
* Instead of using flask, can we generate a static site?
* This would still use jinja and templating to create
* Look good on tv
* Work on ps3 (will probably need flash?)

# Progress
* Change MusicFolder into AlbumStructure
  - Needs to replace BASE PATH with BASE_WEB_PATH
  - Keep a list of directories to create, and then files to copy/sym link
* Change parse into build
  - it will first create the directories and sym link files
  - generate html files and save them to the correct location

