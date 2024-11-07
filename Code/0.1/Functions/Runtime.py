from Imports.Data import *
from Functions.Init import *
from Functions.Move import *
from Display.Update import *

if data["init"] == False:
    Init()

def Runtime():
    Move()
    Update()
    pygame.display.update()
    #pygame.time.delay(1000*5)