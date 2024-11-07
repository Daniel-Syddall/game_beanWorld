from Imports.Data import *
from Game.Main.Grid.Runtime.OffsetArrayDisplacement import *

def Grid_RenderGridFromRoom():

    if grid["lockXL"] == False and grid["lockXR"] == False:
        if player["roomX"]%16 <= 8: StartX = math.floor(player["roomX"]/16) - 9
        elif player["roomX"]%16 >= 9: StartX = math.floor(player["roomX"]/16) - 8
    else:
        if grid["lockXL"] == True: StartX = 0
        elif grid["lockXR"] == True: StartX = room[grid["room"]]["maxX"] - 17

    if grid["lockYL"] == False and grid["lockYR"] == False:
        StartY = math.floor(player["roomY"]/16) - 7
    else:
        if grid["lockYL"] == True: StartY = 0
        elif grid["lockYR"] == True: StartY = room[grid["room"]]["maxY"] - 13


    for x in range(display["grid"]["width"]+1):
        for y in range(display["grid"]["height"]+1):
            for l in range(5):
                grid[str(l)+"_"+str(x)+"_"+str(y)] = room[grid["room"]][str(l)+"_"+str(x+StartX)+"_"+str(y+StartY)]