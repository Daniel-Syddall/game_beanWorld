from Imports.Data import *

def Menu_Select_Runtime():
    if data["init"] == False: pass
    else:
        if button["menu_select"]["createRoom"] == True:
            data["game"] = "menu_createRoom"
            button["menu_select"]["createRoom"] = False

        elif button["menu_select"]["importRoom"] == True:
            data["game"] = "menu_importRoom"
            button["menu_select"]["importRoom"] = False