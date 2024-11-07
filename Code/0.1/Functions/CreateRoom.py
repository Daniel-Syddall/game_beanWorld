from Imports.Data import *

def CreateRoom(roomNum,maxX,maxY):
    for x in range(maxX+1):
        for y in range(maxY+1):
            room[roomNum][f"state-{str(x)}-{str(y)}"] = 0
            for l in range(4):
                room[roomNum][f"{str(l)}-{str(x)}-{str(y)}"] = ""
    for x in range(maxX+1):
        room[roomNum][f"0-{str(x)}-{str(maxY)}"] = "color-black"
    for y in range(maxY+1):
        room[roomNum][f"0-{str(maxX)}-{str(y)}"] = "color-black"