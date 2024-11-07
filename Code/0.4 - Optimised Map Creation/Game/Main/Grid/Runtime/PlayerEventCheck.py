from Imports.Data import *
from Game.Main.Grid.Runtime.TileEvent import *

def Grid_PlayerEventCheck():

    if controller["sprint"] == True: player["movementSpeed"] = 2
    elif controller["sprint"] == False: player["movementSpeed"] = 1

    if controller["up"][0] == True or controller["up"][1] == True:
        player["spriteDirection"] = "up"
        Grid_TileEvent(player["roomX"],player["roomY"] - (player["movementSpeed"] + player["hitboxSize"] ),"up")

    if controller["down"][0] == True or controller["down"][1] == True:
        player["spriteDirection"] = "down"
        Grid_TileEvent(player["roomX"],player["roomY"] + (player["movementSpeed"] + player["hitboxSize"] ),"down")

    if controller["left"][0] == True or controller["left"][1] == True:
        player["spriteDirection"] = "left"
        Grid_TileEvent(player["roomX"] - (player["movementSpeed"] + player["hitboxSize"] + ( math.floor( player["spriteWidth"] / 2 ) ) ),player["roomY"],"left")

    if controller["right"][0] == True or controller["right"][1] == True:
        player["spriteDirection"] = "right"
        Grid_TileEvent(player["roomX"] + (player["movementSpeed"] + player["hitboxSize"] + ( math.floor( player["spriteWidth"] / 2 ) ) ),player["roomY"],"right")