from Imports.Data import *
from Game.Main.Grid.Runtime.GetSpriteDimensions import *
from Game.Main.Grid.Runtime.PlayerEventCheck import *
from Game.Main.Grid.Runtime.CheckGridLock import *
from Game.Main.Grid.Runtime.GetGridOffset import *
from Game.Main.Grid.Runtime.RenderGridFromRoom import *
from Game.Main.Grid.Runtime.PlayerToGrid import *
from Game.Main.Grid.Runtime.SpriteCycle import *

def Grid_Runtime():
    
    if data["init"] == False:

        #Get Room
        #Get Player Sprite Width & Height
        #Get Player Room Placement
        grid["room"] = "test0"
        Grid_GetSpriteDimensions()
        player["roomX"] = 126
        player["roomY"] = 104

    else:

        #Check for Player Movement [ And Trigger Tile Events if Nessesary ]
        Grid_PlayerEventCheck()
        
    #Determine Grid Lock
    #Determine Grid Offset
    #Render Grid from Room
    Grid_CheckGridLock()
    Grid_GetGridOffset()
    Grid_RenderGridFromRoom()

    #Determine Player Placement on Grid
    #Determine Player Sprite Cycle
    Grid_PlayerToGrid()
    Grid_SpriteCycle()