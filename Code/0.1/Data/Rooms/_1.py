from Data.Main import data
from Data.Main import room
from Functions.CreateRoom import CreateRoom

room[1] = {}
room[1]["maxX"] = 21
room[1]["maxY"] = 17
room[1]["spawn0X"] = 1
room[1]["spawn0Y"] = 2

if data["init"] == False:
    CreateRoom(1,room[1]["maxX"],room[1]["maxY"])

for x in range(21):
    for y in range(17):
        room[1][f"state-{str(x)}-{str(y)}"] = 1
        room[1][f"0-{str(x)}-{str(y)}"] = "color-white"

for i in range(21):
    room[1][f"0-{str(i)}-0"] = "color-orange"
    room[1][f"0-{str(i)}-16"] = "color-orange"
    room[1][f"state-{str(i)}-0"] = 2
    room[1][f"state-{str(i)}-16"] = 2

for i in range(17):
    room[1][f"0-0-{str(i)}"] = "color-orange"
    room[1][f"0-20-{str(i)}"] = "color-orange"
    room[1][f"state-0-{str(i)}"] = 2
    room[1][f"state-20-{str(i)}"] = 2

room[1]["send-0-X"] = 0
room[1]["send-0-Y"] = 2
room[1]["send-0-room"] = 0
room[1]["send-0-spawn"] = 1
room[1]["0-0-2"] = "color-black"
room[1]["state-0-2"] = 3

