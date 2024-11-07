from Imports.Data import *

def Grid_TileEvent(x,y,direction):

    if direction == "up" and y >= 0 + ( math.floor ( player["spriteHeight"] ) ): player["roomY"] = y + ( player["hitboxSize"] )
    elif direction == "down" and y <= (room[grid["room"]]["maxY"]*16) - ( math.floor ( player["spriteHeight"] ) ): player["roomY"] =  y - ( player["hitboxSize"] )
    elif direction == "left" and x >= 0 + ( math.floor ( player["spriteWidth"] / 2 ) ): player["roomX"] = x + ( player["hitboxSize"] + ( math.floor ( player["spriteWidth"] / 2 ) ) )
    elif direction == "right" and x <= (room[grid["room"]]["maxX"]*16) - ( math.floor ( player["spriteWidth"] / 2 ) ): player["roomX"] = x - ( player["hitboxSize"] + ( math.floor ( player["spriteWidth"] / 2 ) ) )