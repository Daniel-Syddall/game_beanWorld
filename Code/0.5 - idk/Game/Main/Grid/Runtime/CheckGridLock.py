from Imports.Data import *

def Grid_CheckGridLock():
    
    if player["roomX"] <= 136 or room[grid["room"]]["maxX"] == 17: 
        grid["lockXL"] = True
        grid["lockXR"] = False
    elif player["roomX"] >= ((room[grid["room"]]["maxX"]*16)-135): 
        grid["lockXR"] = True
        grid["lockXL"] = False
    else: 
        grid["lockXL"] = False
        grid["lockXR"] = False

    if player["roomY"] <= (104+(math.floor(player["spriteHeight"]/2))) or room[grid["room"]]["maxY"] == 13:
        grid["lockYL"] = True
        grid["lockYR"] = False
    elif player["roomY"] >= ((room[grid["room"]]["maxY"]*16)-(103-(math.floor(player["spriteHeight"]/2)))): 
        grid["lockYR"] = True
        grid["lockYL"] = False
    else:
        grid["lockYL"] = False
        grid["lockYR"] = False