from Imports.Data import *
from Game.Main.Menu.ImportRoom.Runtime.ButtonCheck import *
from Game.Main.Menu.ImportRoom.Runtime.DataEntry import *

def Menu_ImportRoom_Runtime():
    if data["init"] == False: pass
    else:
        Menu_importRoom_ButtonCheck()
        Menu_ImportRoom_DataEntry()