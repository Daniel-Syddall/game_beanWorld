from Imports.Data import *

def Grid_PlayerToGrid():

    if grid["lockXL"] == False and grid["lockXR"] == False: player["gridX"] = 137
    elif grid["lockXL"] == True: player["gridX"] = player["roomX"]
    elif grid["lockXR"] == True: player["gridX"] = (display["grid"]["width"]*16)-((room[grid["room"]]["maxX"]*16)-player["roomX"])

    if grid["lockYL"] == False and grid["lockYR"] == False: player["gridY"] = (105+(math.floor(player["spriteHeight"]/2)))
    elif grid["lockYL"] == True: player["gridY"] = player["roomY"]
    elif grid["lockYR"] == True: player["gridY"] = (display["grid"]["height"]*16)-((room[grid["room"]]["maxY"]*16)-player["roomY"])