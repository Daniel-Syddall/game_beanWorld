from Data.Variables import *
from Data.Assets import *

if data["varInit"] == False:

    temp_fileNames = os.listdir("./Txt/Rooms/")
    
    for r in range(len(temp_fileNames)):

        temp_roomName = temp_fileNames[r]
        temp_roomName = temp_roomName.split(".")
        temp_roomName = temp_roomName[0]
        room[temp_roomName] = {}

        f = open("./Txt/Rooms/"+temp_fileNames[r],"r")

        temp_lineStore = f.readline()
        temp_lineStore = temp_lineStore.split(":")
        for d in range(len(temp_lineStore)-1):
            temp_varStore = temp_lineStore[d]
            temp_varStore = temp_varStore.split("-")
            room[temp_roomName][temp_varStore[0]] = int(temp_varStore[1])

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