from Data.Const import *
from Data.Vars import *
"""
def ImportRoom(FileName):
    global roomName
    roomName = FileName

    rpg.room[roomName] = {}

    f = open("./Txt/Rooms/"+roomName+".txt","r")

    temp_lineStore = f.readline()
    temp_lineStore = temp_lineStore.split(":")
    for d in range(len(temp_lineStore)-1):
        temp_varStore = temp_lineStore[d]
        temp_varStore = temp_varStore.split("-")
        rpg.room[roomName][temp_varStore[0]] = int(temp_varStore[1])

    for l in range(6):

        temp_lineStore = f.readline()
        temp_lineStore = temp_lineStore.split(":")

        temp_tileIteration_Count = 1
        temp_tileIteration_Left = 0
        temp_tileIteration_Name = ""

        for x in range(room[temp_roomName]["maxX"]):
            for y in range(room[temp_roomName]["maxY"]):
                if temp_tileIteration_Left == 0:
                    temp_varStore = temp_lineStore[temp_tileIteration_Count]
                    temp_varStore = temp_varStore.split("-")
                    temp_tileIteration_Left = int(temp_varStore[0])
                    temp_tileIteration_Name = temp_varStore[1]
                    temp_tileIteration_Count += 1
                room[temp_roomName][f"{temp_lineStore[0]}_{str(x)}_{str(y)}"] = temp_tileIteration_Name
                temp_tileIteration_Left -= 1

        for x in range(room[temp_roomName]["maxX"]+1):
            room[temp_roomName][temp_lineStore[0]+"_"+str(x)+"_"+str(room[temp_roomName]["maxY"])] = ""
        for y in range(room[temp_roomName]["maxY"]+1):
            room[temp_roomName][temp_lineStore[0]+"_"+str(room[temp_roomName]["maxX"])+"_"+str(y)] = ""

    for s in range(room[temp_roomName]["spawnCount"]):
        temp_lineStore = f.readline()
        temp_lineStore = temp_lineStore.split(":")
        for d in range(len(temp_lineStore)-1):
            temp_varStore = temp_lineStore[d]
            temp_varStore = temp_varStore.split("-")
            if temp_varStore[0] == "spawnX": room[temp_roomName]["spawn_"+str(s)+"_X"] = int(temp_varStore[1])
            elif temp_varStore[0] == "spawnY": room[temp_roomName]["spawn_"+str(s)+"_Y"] = int(temp_varStore[1])
            room[temp_roomName][temp_varStore[0]] = int(temp_varStore[1])

    for s in range(room[temp_roomName]["sendCount"]):
        temp_lineStore = f.readline()
        temp_lineStore = temp_lineStore.split(":")
        for d in range(len(temp_lineStore)-1):
            temp_varStore = temp_lineStore[d]
            temp_varStore = temp_varStore.split("-")
            if temp_varStore[0] == "sendX": room[temp_roomName]["send_"+str(s)+"_X"] = int(temp_varStore[1])
            elif temp_varStore[0] == "sendX": room[temp_roomName]["send_"+str(s)+"_Y"] = int(temp_varStore[1])
            elif temp_varStore[0] == "sendRoom": room[temp_roomName]["send_"+str(s)+"_room"] = temp_varStore[1]
            elif temp_varStore[0] == "sendSpawn": room[temp_roomName]["send_"+str(s)+"_spawn"] = int(temp_varStore[1])

    f.close()

    grid["room"] = dataEntry["menu_createRoom"]["store_roomName"]
    data["game"] = "Overworld"

"""

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