from Imports.SubData import *
from Imports.Widgets import *

class gameState_CreateRoom:
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def __init__(self):

        data["fps"] = 30
        self.state = "CreateRoom"
        
        self.roomName = ""
        self.roomName_edit = False
        self.roomWidth = ""
        self.roomWidth_edit = False
        self.roomHeight = ""
        self.roomHeight_edit = False

        window.surface.fill(color["grey"])
        self.label_createRoom = Widget_Label("p","Create Room","orange",w(0),w(6),h(0),h(2),False,"black","black")
        self.label_createRoom.blit()
        self.label_roomName = Widget_Label("h1","Room Name","black",w(15),w(45),h(10),h(20),False,"black","black")
        self.label_roomName.blit()
        self.button_roomName = Widget_Button("h2",self.roomName,"black","black",w(55),w(85),h(10),h(20),"white","white","black","orange")
        self.label_roomWidth = Widget_Label("h1","Room Width","black",w(15),w(45),h(25),h(35),False,"black","black")
        self.label_roomWidth.blit()
        self.button_roomWidth = Widget_Button("h2",self.roomWidth,"black","black",w(55),w(85),h(25),h(35),"white","white","black","orange")
        self.label_roomHeight = Widget_Label("h1","Room Height","black",w(15),w(45),h(40),h(50),False,"black","black")
        self.label_roomHeight.blit()
        self.button_roomHeight = Widget_Button("h2",self.roomHeight,"black","black",w(55),w(85),h(40),h(50),"white","white","black","orange")
        self.button_create = Widget_Button("h1","Create","black","black",w(15),w(85),h(55),h(65),"white","white","black","orange")
        self.Button_goBack = Widget_Button("h2","Go Back","black","black",w(80),w(95),h(91),h(95),"white","white","black","orange")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Runtime(self):
        if self.button_roomName.click == True: self.roomName_edit = True
        elif self.button_roomName.miss == True: self.roomName_edit = False
        if self.roomName_edit == True: 
            if controller["backspace"] == True: self.roomName = self.roomName[:-1]
            else: self.roomName += controller["type"]

        if self.button_roomWidth.click == True: self.roomWidth_edit = True
        elif self.button_roomWidth.miss == True: self.roomWidth_edit = False
        if self.roomWidth_edit == True: 
            if controller["backspace"] == True: self.roomWidth = self.roomWidth[:-1]
            else: self.roomWidth += controller["type"]

        if self.button_roomHeight.click == True: self.roomHeight_edit = True
        elif self.button_roomHeight.miss == True: self.roomHeight_edit = False
        if self.roomHeight_edit == True: 
            if controller["backspace"] == True: self.roomHeight = self.roomHeight[:-1]
            else: self.roomHeight += controller["type"]

        if self.Button_goBack.click == True: data["gameState"] = "Select"

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Render(self):
        self.button_roomName.update_text(self.roomName)
        self.button_roomWidth.update_text(self.roomWidth)
        self.button_roomHeight.update_text(self.roomHeight)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Blit(self):
        self.button_roomName.blit()
        self.button_roomWidth.blit()
        self.button_roomHeight.blit()
        self.button_create.blit()
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