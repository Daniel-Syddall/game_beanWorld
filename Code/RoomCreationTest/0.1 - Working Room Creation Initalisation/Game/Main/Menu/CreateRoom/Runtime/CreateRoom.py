from Imports.Data import *

def Menu_CreateRoom_CreateRoom():
    room[dataEntry["menu_createRoom"]["store_roomName"]] = {}
    room[dataEntry["menu_createRoom"]["store_roomName"]]["maxX"] = int(dataEntry["menu_createRoom"]["store_maxX"])
    room[dataEntry["menu_createRoom"]["store_roomName"]]["maxY"] = int(dataEntry["menu_createRoom"]["store_maxY"])
    print(str(room[dataEntry["menu_createRoom"]["store_roomName"]]["maxX"])+","+str(room[dataEntry["menu_createRoom"]["store_roomName"]]["maxY"]))

    for x in range(room[dataEntry["menu_createRoom"]["store_roomName"]]["maxX"]+1):
        for y in range(room[dataEntry["menu_createRoom"]["store_roomName"]]["maxY"]+1):
            room[dataEntry["menu_createRoom"]["store_roomName"]][f"state_{str(x)}_{str(y)}"] = ""
            for l in range(5):
                room[dataEntry["menu_createRoom"]["store_roomName"]][f"{str(l)}_{str(x)}_{str(y)}"] = ""

    for x in range(room[dataEntry["menu_createRoom"]["store_roomName"]]["maxX"]):
        for y in range(room[dataEntry["menu_createRoom"]["store_roomName"]]["maxY"]):
            room[dataEntry["menu_createRoom"]["store_roomName"]][f"state_{str(x)}_{str(y)}"] = "pass"
            room[dataEntry["menu_createRoom"]["store_roomName"]][f"0_{str(x)}_{str(y)}"] = "color_white"