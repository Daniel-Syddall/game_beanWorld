from Imports.Data import *
from Game.Main.Menu.CreateRoom.Runtime.ButtonCheck import *
from Game.Main.Menu.CreateRoom.Runtime.DataEntry import *

def Menu_CreateRoom_Runtime():
    if data["init"] == False: pass
    else:
        Menu_CreateRoom_ButtonCheck()
        Menu_CreateRoom_DataEntry()