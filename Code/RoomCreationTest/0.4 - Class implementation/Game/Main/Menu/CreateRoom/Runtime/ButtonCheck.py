from Imports.Data import *
from Game.Main.Menu.CreateRoom.Runtime.CreateRoom import *
from Game.Main.Menu.CreateRoom.Runtime.PlayerToRoom import *

def Menu_CreateRoom_ButtonCheck():
    if button["menu_createRoom"]["click_dataEntry_roomName"] == True and dataEntry["menu_createRoom"]["busy"] == False:
        dataEntry["menu_createRoom"]["check_roomName"] = True
        dataEntry["menu_createRoom"]["busy"] = True
        button["menu_createRoom"]["click_dataEntry_roomName"] = False
    else:
        if button["menu_createRoom"]["misClick_dataEntry_roomName"] == True and dataEntry["menu_createRoom"]["check_roomName"] == True:
            dataEntry["menu_createRoom"]["check_roomName"] = False
            dataEntry["menu_createRoom"]["busy"] = False
            button["menu_createRoom"]["misClick_dataEntry_roomName"] = False

    if button["menu_createRoom"]["click_dataEntry_maxX"] == True and dataEntry["menu_createRoom"]["busy"] == False:
        dataEntry["menu_createRoom"]["check_maxX"] = True
        dataEntry["menu_createRoom"]["busy"] = True
        button["menu_createRoom"]["click_dataEntry_maxX"] = False
    else:
        if button["menu_createRoom"]["misClick_dataEntry_maxX"] == True and dataEntry["menu_createRoom"]["check_maxX"] == True:
            dataEntry["menu_createRoom"]["check_maxX"] = False
            dataEntry["menu_createRoom"]["busy"] = False
            button["menu_createRoom"]["misClick_dataEntry_maxX"] = False

    if button["menu_createRoom"]["click_dataEntry_maxY"] == True and dataEntry["menu_createRoom"]["busy"] == False:
        dataEntry["menu_createRoom"]["check_maxY"] = True
        dataEntry["menu_createRoom"]["busy"] = True
        button["menu_createRoom"]["click_dataEntry_maxY"] = False
    else:
        if button["menu_createRoom"]["misClick_dataEntry_maxY"] == True and dataEntry["menu_createRoom"]["check_maxY"] == True:
            dataEntry["menu_createRoom"]["check_maxY"] = False
            dataEntry["menu_createRoom"]["busy"] = False
            button["menu_createRoom"]["misClick_dataEntry_maxY"] = False

    if button["menu_createRoom"]["create"] == True:
        Menu_CreateRoom_CreateRoom()
        Menu_CreateRoom_PlayerToRoom()
        data["game"] = "grid"
        button["menu_createRoom"]["create"] = False

    if button["menu_createRoom"]["goBack"] == True:
        data["game"] = "menu_select"
        button["menu_createRoom"]["goBack"] = False