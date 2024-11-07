from Imports.Data import *
from Game.Main.Menu.ImportRoom.Runtime.FileToRoom import *
from Game.Main.Menu.ImportRoom.Runtime.PlayerToRoom import *

def Menu_importRoom_ButtonCheck():
    if button["menu_importRoom"]["click_dataEntry_fileName"] == True and dataEntry["menu_importRoom"]["busy"] == False:
        dataEntry["menu_importRoom"]["check_fileName"] = True
        dataEntry["menu_importRoom"]["busy"] = True
        button["menu_importRoom"]["click_dataEntry_fileName"] = False
    else: 
        if button["menu_importRoom"]["misClick_dataEntry_fileName"] == True and dataEntry["menu_importRoom"]["check_fileName"] == True:
            dataEntry["menu_importRoom"]["check_fileName"] = False
            dataEntry["menu_importRoom"]["busy"] = False
            button["menu_importRoom"]["misClick_dataEntry_fileName"] = False

    if button["menu_importRoom"]["import"] == True:
        Menu_ImportRoom_FileToRoom()
        Menu_ImportRoom_PlayerToRoom()
        data["game"] = "grid"
        button["menu_importRoom"]["import"] = False

    if button["menu_importRoom"]["goBack"] == True:
        data["game"] = "menu_select"
        button["menu_importRoom"]["goBack"] = False