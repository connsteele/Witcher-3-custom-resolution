# Witcher 3 Custom Resolution
Greetings, this is a python script that will set cutom resolutions for The Witcher 3: Wild Hunt on Steam Deck

# Usage
Run the script by executing the run.sh file included in this repo. If the .sh file will not run use "chmod +x run.sh" to make it executable.
When prompted by the program for an aspect ratio you may use: "16:10", "16:9", or "custom"
If you are not using a custom resolution you will be asked to then input a horizontal resolution (integer). An example input here would be 960.
A vertical resolution corresponding to your horizontal input will be calculated, in this case 600 for 16:10 and 540 for 16:9.
When using a custom resolution the program will ask you for a horizontal resolution (integer) then a vertical resolution (integer).
The new resolution will be written to The Witcher 3's user.settings file for the game to use. If you encounter any problems with this program, please contact me.

# For GOTY version users
The SETTINGS_LOCATION = '/home/deck/.local/share/Steam/steamapps/compatdata/292030/pfx/drive_c/users/steamuser/My Documents/The Witcher 3/user.settings' might be invalid for this version of the game.
If this is the case notify me, for the time being change "292030" to "499450" in the constant above found in the tw3_cr.py file.

# Testing
If you want to run the script and test it locally open tw3_cr.py and update the "settings_loc" variable to point to the file you wish to test it on.
For example: "settings_loc = "C:/Users/Bob/Desktop/TW3-CR/test/user.settings""
