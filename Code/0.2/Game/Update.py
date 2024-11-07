from Imports.Data import *
from Game.Controller import *

from Game.Main.Grid.Runtime.Runtime import *
Grid_Runtime()
from Game.Main.Grid.Render import *
Grid_Render()
from Game.Main.Grid.Blit import *

def Update():
    Controller()
    
    if data["game"] == "grid":
        Grid_Runtime()
        Grid_Render()
        Grid_Blit()

    pygame.display.update()