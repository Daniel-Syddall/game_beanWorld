import pygame

data_init = False
from Imports.Data import *
data_init = True
from Functions.Controller import *
from Functions.Runtime import *
data["init"] = True

def Script():

    while True:
        pygame.time.delay(math.floor(1000/60))
        Controller()
        data["frames"] += 1
        if data["frames"] >= 1:
            data["frames"] = 0
            Runtime()