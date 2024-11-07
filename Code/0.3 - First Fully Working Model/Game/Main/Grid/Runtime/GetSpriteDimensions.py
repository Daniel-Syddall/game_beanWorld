from Imports.Data import *

def Grid_GetSpriteDimensions():

    playerSprite = player["sprite"]
    playerSprite = playerSprite.split("_")

    if playerSprite[0] == "color":
        player["spriteWidth"] = 14
        player["spriteHeight"] = 17
        
    elif playerSprite[0] == "asset":
        player["spriteWidth"] = asset[playerSprite[1]][playerSprite[2]+"_"+player["spriteDirection"]+"_"+str(player["spriteState"])].get_width()
        player["spriteHeight"] = asset[playerSprite[1]][playerSprite[2]+"_"+player["spriteDirection"]+"_"+str(player["spriteState"])].get_height()