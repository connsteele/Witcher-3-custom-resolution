# Created By Connor Steele
from enum import Enum
from functools import total_ordering

@total_ordering
class AspectRatio(Enum):
    BY10 = 1
    BY9 = 2
    CUSTOM = 3
    def __eq__(self, other):
        return self.__class__ is other.__class__ and other.value == self.value
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

def main():
    print("This program will enter in a custom resolution for The Witcher 3: The Wild Hunt on Steam Deck")
    # The string below is the settings location for TW3 on Deck no matter where the game is installed
    settings_loc = '~./local/share/Steam/steamapps/compatdata/292030/pfx/drive_c/users/steamuser/My Documents/The Witcher 3/user.settings'
    test_loc = 'C:/Users/Connor/Desktop/TW3-CR/test/user.settings'
    # Make sure the settings file exists
    try:
        file = open(test_loc, 'r')
        filebuffer = file.readlines()
        file.close()
    except OSError:
        print("The \"user.settings\" file for The Witcher 3: Wild Hunt does not exist in the expected location")
        print("Make sure the game has been installed and run. If both are true contact the author of this code.")
        print("Exiting program")
        return -1

    # Ask the user for a aspect ratio
    aspect = get_aspect_ratio() 

    # Since we checked earlier the file must exist, overwrite it completley
    # might need to set fullscreen setting
    fw = open(test_loc, 'w')
    for line in filebuffer:
        linelist = line.split("=")
        if linelist[0] == 'Resolution':
            width = 1280
            height = 720
            if aspect == AspectRatio.CUSTOM:
                print('Enter horizontal resolution:')
                width = get_user_num()
                print('Enter vertical resolution:')
                height = get_user_num()
                print("New resoltion is:", width, 'x', height)
            else:
                print('Enter horizontal resolution:')
                width = get_user_num()
                if aspect == AspectRatio.BY10:
                    ratio = 10/16
                else:
                    ratio = 9/16
                height = int(width * ratio)
            print('New resolution is:', width, 'x', height)
            outline = 'Resolution=\"'+ str(width) + 'x' + str(height) + '\"\n'
            fw.write(outline)
        else:
            fw.write(line)
    fw.close()
    return 0

# Asks the user if they want 16:9, 16:10 or custom
def get_aspect_ratio():
    print('What aspect ratio do you want to use:\n16:10, 16:9 or Custom')
    usrratio = input().casefold()
    if (usrratio != '16:10' and usrratio != '16:9' and usrratio != 'custom'.casefold()):
        print('Invalid aspect ratio, please use: \"16:10\", \"16:9\" or \"Custom\"')
        return get_aspect_ratio()
    elif usrratio == '16:10':
        print('16:10 selected\n')
        return AspectRatio.BY10
    elif usrratio == '16:9':
        print('16:9 selected\n')
        return AspectRatio.BY9
    else:
        print('Custom selected\n')
        return AspectRatio.CUSTOM

def get_user_num():
    inum = input()
    if not inum.isnumeric():
        print('Invalid input, please use an integer (ex: 960)')
        return get_user_num()
    return int(inum)

if __name__ == "__main__":
    main()
