from Imports.Data import *

def Menu_ImportRoom_DataEntry():
    if dataEntry["menu_importRoom"]["busy"] == True:
        if dataEntry["menu_importRoom"]["check_fileName"] == True:
            if controller["enter"] == True:
                dataEntry["menu_importRoom"]["check_fileName"] = False
                dataEntry["menu_importRoom"]["busy"] = False
            else:
                dataEntry["menu_importRoom"]["store_fileName"] += controller["type"]
                if controller["backspace"] == True: dataEntry["menu_importRoom"]["store_fileName"] = dataEntry["menu_importRoom"]["store_fileName"][:-1]