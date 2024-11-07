from Imports.Data import *

from Game.Main.Grid.Runtime.Runtime import *
Grid_Runtime()
from Game.Main.Grid.Render import *
Grid_Render()
from Game.Main.Grid.Blit import *

from Game.Main.GridEditor.Runtime.Runtime import *
GridEditor_Runtime()
from Game.Main.GridEditor.Render import *
GridEditor_Render()
from Game.Main.GridEditor.Blit import *

from Game.Main.Menu.CreateRoom.Runtime.Runtime import *
Menu_CreateRoom_Runtime()
from Game.Main.Menu.CreateRoom.Render import *
Menu_CreateRoom_Render()
from Game.Main.Menu.CreateRoom.Blit import *

from Game.Main.Menu.ImportRoom.Runtime.Runtime import *
Menu_ImportRoom_Runtime()
from Game.Main.Menu.ImportRoom.Render import *
Menu_ImportRoom_Render()
from Game.Main.Menu.ImportRoom.Blit import *

from Game.Main.Menu.Select.Runtime.Runtime import *
Menu_Select_Runtime()
from Game.Main.Menu.Select.Render import *
Menu_Select_Render()
from Game.Main.Menu.Select.Blit import *

def Update():
    
    if data["game"] == "grid":
        Grid_Runtime()
        Grid_Render()
        Grid_Blit()
        GridEditor_Runtime()
        GridEditor_Render()
        GridEditor_Blit()

    elif data["game"] == "menu_select":
        Menu_Select_Runtime()
        Menu_Select_Render()
        Menu_Select_Blit()

    elif data["game"] == "menu_createRoom":
        Menu_CreateRoom_Runtime()
        Menu_CreateRoom_Render()
        Menu_CreateRoom_Blit()

    elif data["game"] == "menu_importRoom":
        Menu_ImportRoom_Runtime()
        Menu_ImportRoom_Render()
        Menu_ImportRoom_Blit()

    pygame.display.update()