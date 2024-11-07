from Imports.Data import *

def Menu_ImportRoom_Runtime():
    if data["init"] == False: pass
    else:
        if button["menu_importRoom"]["goBack"] == True:
            data["game"] = "menu_select"
            button["menu_importRoom"]["goBack"] = False