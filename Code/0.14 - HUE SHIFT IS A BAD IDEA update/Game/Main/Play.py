from Imports.SubData import *
from Imports.Widgets import *

class gameState_Play:
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def __init__(self):

        data["fps"] = 60
        self.state = "Play"
        self.textBox = Widget_Label("h2","","black",w(20),w(80),h(80),h(97),True,"white","black")
        rpg.BlitBorder(window.surface,w(0),h(0),window.width,window.height)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Runtime(self):
        rpg.Run()
        if rpg.textBox != "": self.textBox.update_text(rpg.textBox)


# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Render(self):
        pass

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Blit(self):
        temp_surfaceX,temp_surfaceY,temp_surfaceWidth,temp_surface_height = rpg.Blit(window.surface,math.floor((w(100)-((window.height/13)*17))/2),h(0),(window.height/13)*17,window.height)
        if rpg.textBox != "":
            self.textBox.update_dimentions(temp_surfaceX+w(5),temp_surfaceX+temp_surfaceWidth-w(5),temp_surfaceY+h(85),temp_surfaceY+temp_surface_height-h(3))
            self.textBox.blit()

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