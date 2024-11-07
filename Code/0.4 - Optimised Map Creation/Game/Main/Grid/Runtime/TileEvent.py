from Imports.Data import *

def Grid_TileEvent(x,y,direction):

    if room[grid["room"]]["state_"+str(math.floor(x/16))+"_"+str(math.floor((y/16)))] != "":

        if direction == "up" and y >= 0: player["roomY"] = y + ( player["hitboxSize"] )
        elif direction == "down": player["roomY"] = y - ( player["hitboxSize"] )
        elif direction == "left" and x >= 0: player["roomX"] = x + ( player["hitboxSize"] + ( math.floor ( player["spriteWidth"] / 2 ) ) )
        elif direction == "right": player["roomX"] = x - ( player["hitboxSize"] + ( math.floor ( player["spriteWidth"] / 2 ) ) )

    #elif room[grid["room"]]["state_"+str(math.floor(x/16))+"_"+str(math.floor((y/16)))] == "send":
    #    send_found = False
    #    send_count = 0
    #    while send_found == False:
    #        if room[grid["room"]]["send_"+str(send_count)+"_X"] == math.floor(x/16) and room[grid["room"]]["send_"+str(send_count)+"_Y"] == math.floor(y/16):
    #            send_found = True
    #        else: send_count += 1

    #    send_spawn = room[grid["room"]]["send_"+str(send_count)+"_spawn"]
    #    grid["room"] = room[grid["room"]]["send_"+str(send_count)+"_room"]
    #    player["roomX"] = (room[grid["room"]]["spawn_"+str(send_spawn)+"_X"]*16)+10
    #    player["roomY"] = (room[grid["room"]]["spawn_"+str(send_spawn)+"_Y"]*16)+10