from Imports.Data import *

from Display.Map.PlayerInteraction import *
from Display.Map.Render import *
Render_Map()
from Display.Map.Blit import *

def Update():
    if data["display"] == "map":
        PlayerInteraction_Map()
        Render_Map()
        pygame.draw.rect(window,color["black"],(0,0,display["window"]["width"],display["window"]["height"]))
        Blit_Map()