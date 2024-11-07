from Imports.SubData import *
from Imports.Widgets import *

class gameState_Overworld:
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def __init__(self):

        data["fps"] = 60
        self.state = "Overworld"
        
        rpg.BlitBorder(window.surface,w(0),h(0),window.width,window.height)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Runtime(self):
        rpg.Run()

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Render(self):
        pass

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Blit(self):
        rpg.Blit(window.surface,math.floor((w(100)-((window.height/13)*17))/2),h(0),(window.height/13)*17,window.height)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#
#   - = To create a new Game State, follow the steps below: = -
#
#
#       1a. Go to ./Game/Main
#
#       1b. Copy this File and paste it into ./Game/Main
#
#       1c. Select an appropriate name for this new Game State
#
#       1d. Within the coppied file, replace any instance of "Temp" with the Name of the new Game state
#                                     (THIS IS INCLUDES THE FILE NAME)
#
#
#       2a. Go to ./Imports/MainData.py
#
#       2b. Copy Line 10 and Paste it on the next avalible line
#
#       2c. On the new coppied lines, replace any instance of the word "Temp" with the Name of the new Game State
#
#
#       3a. Go to ./Main/Update.py
#
#       3b. Copy Line 10 and Paste it on the next avalible line
#
#       3c. On the new coppied lines, replace any instance of the word "Temp" with the Name of the new Game State
#