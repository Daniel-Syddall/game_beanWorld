from Imports.Data import *
from Game.Main.Menu.CreateRoom.Runtime.CreateRoom import *
from Game.Main.Menu.CreateRoom.Runtime.PlayerToRoom import *

def Menu_CreateRoom_ButtonCheck():
    if button["menu_createRoom"]["dataEntry_roomName"] == True and dataEntry["menu_createRoom"]["busy"] == False:
        dataEntry["menu_createRoom"]["check_roomName"] = True
        dataEntry["menu_createRoom"]["busy"] = True
        button["menu_createRoom"]["dataEntry_roomName"] = False

    elif button["menu_createRoom"]["dataEntry_maxX"] == True and dataEntry["menu_createRoom"]["busy"] == False:
        dataEntry["menu_createRoom"]["check_maxX"] = True
        dataEntry["menu_createRoom"]["busy"] = True
        button["menu_createRoom"]["dataEntry_maxX"] = False

    elif button["menu_createRoom"]["dataEntry_maxY"] == True and dataEntry["menu_createRoom"]["busy"] == False:
        dataEntry["menu_createRoom"]["check_maxY"] = True
        dataEntry["menu_createRoom"]["busy"] = True
        button["menu_createRoom"]["dataEntry_maxY"] = False

    elif button["menu_createRoom"]["create"] == True:
        Menu_CreateRoom_CreateRoom()
        Menu_CreateRoom_PlayerToRoom()
        data["game"] = "grid"
        button["menu_createRoom"]["create"] = False

    elif button["menu_createRoom"]["goBack"] == True:
        data["game"] = "menu_select"
        button["menu_createRoom"]["goBack"] = False