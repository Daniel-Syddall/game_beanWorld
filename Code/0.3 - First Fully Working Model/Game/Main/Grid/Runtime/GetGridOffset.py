from Imports.Data import *
from Game.Main.Grid.Runtime.OffsetArrayDisplacement import *

def Grid_GetGridOffset():

    OffsetArrayY = Grid_OffsetArrayDisplacement(math.floor(player["spriteHeight"]/2))

    if grid["lockXL"] == False and grid["lockXR"] == False: grid["offsetX"] = OffsetArray[player["roomX"]%16]
    else: grid["offsetX"] = 0
    
    if grid["lockYL"] == False and grid["lockYR"] == False: grid["offsetY"] = OffsetArrayY[player["roomY"]%16]
    else: grid["offsetY"] = 0