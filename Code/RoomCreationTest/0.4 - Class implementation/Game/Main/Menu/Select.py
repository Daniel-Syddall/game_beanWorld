from Imports.SubData import *
from Imports.Widgets import *

class gameState_Select:
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def __init__(self):

        data["fps"] = 30
        self.state = "Select"
        
        window.surface.fill(color["grey"])
        self.label_selectMenu = Widget_Label("p","Select Menu","orange",w(0),w(6),h(0),h(2),False,"grey","grey")
        self.label_selectMenu.blit()
        self.button_createRoom = Widget_Button("h1","Create Room","black","black",w(25),w(75),h(25),h(45),"white","white","black","orange")
        self.button_importRoom = Widget_Button("h1","Import Room","black","black",w(25),w(75),h(55),h(75),"white","white","black","orange")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Runtime(self):
        if self.button_createRoom.click == True:
            self.button_createRoom.click = False
            data["gameState"] = "CreateRoom"
        elif self.button_importRoom.click == True:
            self.button_importRoom.click = False
            data["gameState"] = "ImportRoom"

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Render(self):
        pass

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Blit(self):
        self.button_createRoom.blit()
        self.button_importRoom.blit()

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