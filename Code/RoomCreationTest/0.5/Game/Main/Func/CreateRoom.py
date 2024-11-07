from Data.Const import *
from Data.Vars import *

def CreateRoom(RoomName,roomWidth,roomHeight):
    global roomName
    roomName = RoomName

    rpg.room[roomName] = {}
    rpg.room[roomName]["maxX"] = roomWidth
    rpg.room[roomName]["maxY"] = roomHeight
    rpg.room[roomName]["spawnCount"] = 0
    rpg.room[roomName]["sendCount"] = 0

    for x in range(rpg.room[roomName]["maxX"]+1):
        for y in range(rpg.room[roomName]["maxY"]+1):
            rpg.room[roomName][f"state_{str(x)}_{str(y)}"] = ""
            rpg.room[roomName][f"state_{str(x)}_{str(y)}"] = "pass"
            rpg.room[roomName][f"0_{str(x)}_{str(y)}"] = "color_white"
            for l in range(4):
                rpg.room[roomName][f"{str(l+1)}_{str(x)}_{str(y)}"] = ""


    rpg.gridData["room"] = roomName
    data["game"] = "Overworld"

#
#   - = To create a new Game Func, follow the steps below: = -
#
#
#       1a. Go to ./Game/Main/Func
#
#       1b. Copy this File and paste it into ./Game/Main/Func
#
#       1c. Select an appropriate name for this new Game State
#
#       1d. Within the coppied file, replace any instance of "Temp" with the Name of the new Game state
#                                     (THIS IS INCLUDES THE FILE NAME)
#
#
#       2a. Go to ./Imports/SubData.py
#
#       2b. Copy Line 10 and Paste it on the next avalible line
#
#       2c. On the new coppied lines, replace any instance of the word "Temp" with the Name of the new Game State
#