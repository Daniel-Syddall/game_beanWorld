from Imports.Data import *

def Menu_CreateRoom_DataEntry():
    if dataEntry["menu_createRoom"]["busy"] == True:
        if dataEntry["menu_createRoom"]["check_roomName"] == True:
            if controller["enter"] == True:
                dataEntry["menu_createRoom"]["check_roomName"] = False
                dataEntry["menu_createRoom"]["busy"] = False
            else:
                dataEntry["menu_createRoom"]["store_roomName"] += controller["type"]
                if controller["backspace"] == True: dataEntry["menu_createRoom"]["store_roomName"] = dataEntry["menu_createRoom"]["store_roomName"][:-1]

        if dataEntry["menu_createRoom"]["check_maxX"] == True:
            if controller["enter"] == True:
                dataEntry["menu_createRoom"]["check_maxX"] = False
                dataEntry["menu_createRoom"]["busy"] = False
            else:
                dataEntry["menu_createRoom"]["store_maxX"] += controller["type"]
                if controller["backspace"] == True: dataEntry["menu_createRoom"]["store_maxX"] = dataEntry["menu_createRoom"]["store_maxX"][:-1]

        if dataEntry["menu_createRoom"]["check_maxY"] == True:
            if controller["enter"] == True:
                dataEntry["menu_createRoom"]["check_maxY"] = False
                dataEntry["menu_createRoom"]["busy"] = False
            else:
                dataEntry["menu_createRoom"]["store_maxY"] += controller["type"]
                if controller["backspace"] == True: dataEntry["menu_createRoom"]["store_maxY"] = dataEntry["menu_createRoom"]["store_maxY"][:-1]