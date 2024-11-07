from Data.Variables import *
from Data.Assets import *

def Room_CreateWall(RoomName,layer,StartX,StartY,EndX,EndY,WallFill):
    if StartX <= EndX:
        LowX = StartX
        HighX = EndX
    elif EndY < StartX:
        LowX = EndY
        HighX = StartY
    if StartY <= EndY:
        LowY = StartY
        HighY = EndY
    elif EndY < StartY:
        LowY = EndY
        HighY = StartY


    for x in range((HighX-LowX)+1):
        for y in range((HighY-LowY)+1):
            room[RoomName][f"{str(layer)}_{str(x+LowX)}_{str(y+LowY)}"] = WallFill
