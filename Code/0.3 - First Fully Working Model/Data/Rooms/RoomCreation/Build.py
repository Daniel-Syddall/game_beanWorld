from Data.Variables import *
from Data.Assets import *

def Build(RoomName,RoomWidth,RoomHeight,Fill,Border):
    room[RoomName] = {}
    room[RoomName]["maxX"] = RoomWidth
    room[RoomName]["maxY"] = RoomHeight

    for x in range(RoomWidth+1):
        for y in range(RoomHeight+1):
            room[RoomName][f"state_{str(x)}_{str(y)}"] = ""
            for l in range(4):
                room[RoomName][f"{str(l)}_{str(x)}_{str(y)}"] = ""

    for x in range(RoomWidth-2):
        for y in range(RoomHeight-2):
            room[RoomName][f"state_{str(x+1)}_{str(y+1)}"] = "pass"
            room[RoomName][f"0_{str(x+1)}_{str(y+1)}"] = Fill

    for x in range(RoomWidth):
        room[RoomName][f"state_{str(x)}_0"] = ""
        room[RoomName][f"0_{str(x)}_0"] = Border
        room[RoomName][f"state_{str(x)}_{str(RoomHeight-1)}"] = ""
        room[RoomName][f"0_{str(x)}_{str(RoomHeight-1)}"] = Border
    for y in range(RoomHeight):
        room[RoomName][f"state_0_{str(y)}"] = ""
        room[RoomName][f"0_0_{str(y)}"] = Border
        room[RoomName][f"state_{str(RoomWidth-1)}_{str(y)}"] = ""
        room[RoomName][f"0_{str(RoomWidth-1)}_{str(y)}"] = Border

    for x in range(RoomWidth+1):
        room[RoomName][f"state_{str(x)}_{str(RoomHeight)}"] = ""
        room[RoomName][f"0_{str(x)}_{str(RoomHeight)}"] = ""

    for y in range(RoomHeight+1):
        room[RoomName][f"state_{str(RoomWidth)}_{str(y)}"] = ""
        room[RoomName][f"0_{str(RoomWidth)}_{str(y)}"] = ""