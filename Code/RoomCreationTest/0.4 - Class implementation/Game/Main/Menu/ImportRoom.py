from Imports.SubData import *
from Imports.Widgets import *

class gameState_ImportRoom:
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def __init__(self):

        data["fps"] = 30
        self.state = "ImportRoom"
        
        self.fileName = ""
        self.fileName_edit = False

        window.surface.fill(color["grey"])
        self.label_importRoom = Widget_Label("p","Import Room","orange",w(0),w(6),h(0),h(2),False,"black","black")
        self.label_importRoom.blit()
        self.label_fileName = Widget_Label("h1","File Name (Without .txt)","black",w(15),w(45),h(10),h(20),False,"black","black")
        self.label_fileName.blit()
        self.button_fileName = Widget_Button("h2",self.fileName,"black","black",w(55),w(85),h(10),h(20),"white","white","black","orange")
        self.button_import = Widget_Button("h1","Import","black","black",w(15),w(85),h(22),h(33),"white","white","black","orange")
        self.Button_goBack = Widget_Button("h2","Go Back","black","black",w(80),w(95),h(91),h(95),"white","white","black","orange")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Runtime(self):
        if self.button_fileName.click == True: self.fileName_edit = True
        elif self.button_fileName.miss == True: self.fileName_edit = False
        if self.fileName_edit == True: 
            if controller["backspace"] == True: self.fileName = self.fileName[:-1]
            else: self.fileName += controller["type"]

        if self.Button_goBack.click == True: data["gameState"] = "Select"

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Render(self):
        self.button_fileName.update_text(self.fileName)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Blit(self):
        self.button_fileName.blit()
        self.button_import.blit()
        self.Button_goBack.blit()

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