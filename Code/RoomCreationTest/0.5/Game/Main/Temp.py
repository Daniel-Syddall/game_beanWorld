from Imports.SubData import *
from Imports.Widgets import *

class gameState_Temp:
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def __init__(self):

        data["fps"] = 30
        self.state = "Temp"
        self.count = 0

        window.surface.fill(color["white"])

        self.label = {}
        self.label["example"] = Widget_Label("h1","Example","black",w(25),w(75),h(5),h(45),False,"black","black")
        self.label["example"].blit()

        self.button = {}
        self.button["example"] = Widget_Button("h2","Exampe","black","white",w(25),w(75),h(55),h(95),"white","grey","black","black")
        self.button["quit"] = Widget_Button("p","Quit","black","black",w(90),w(99),h(95),h(99),"white","white","black","grey")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Runtime(self):

        if self.button["quit"].click == True: 
            pygame.quit()
            quit()
        self.count += 1

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Render(self):

        self.button["quit"].update_text("Quit : "+str(self.count))

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def Blit(self):

        self.button["example"].blit()
        self.button["quit"].blit()

        #print("Temp")

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