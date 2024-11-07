from Data.Main import data
from Data.Main import room
from Functions.CreateRoom import CreateRoom

room[0] = {}
room[0]["maxX"] = 17
room[0]["maxY"] = 13
room[0]["spawn0X"] = 4
room[0]["spawn0Y"] = 4
room[0]["spawn1X"] = 15
room[0]["spawn1Y"] = 10

if data["init"] == False:
    CreateRoom(0,room[0]["maxX"],room[0]["maxY"])

for x in range(17):
    for y in range(13):
        room[0][f"state-{str(x)}-{str(y)}"] = 1
        room[0][f"0-{str(x)}-{str(y)}"] = "color-white"

for i in range(17):
    room[0][f"0-{str(i)}-0"] = "color-orange"
    room[0][f"0-{str(i)}-12"] = "color-orange"
    room[0][f"state-{str(i)}-0"] = 2
    room[0][f"state-{str(i)}-12"] = 2

for i in range(13):
    room[0][f"0-0-{str(i)}"] = "color-orange"
    room[0][f"0-16-{str(i)}"] = "color-orange"
    room[0][f"state-0-{str(i)}"] = 2
    room[0][f"state-16-{str(i)}"] = 2

room[0]["send-0-X"] = 16
room[0]["send-0-Y"] = 10
room[0]["send-0-room"] = 1
room[0]["send-0-spawn"] = 0
room[0]["0-16-10"] = "color-black"
room[0]["state-16-10"] = 3

