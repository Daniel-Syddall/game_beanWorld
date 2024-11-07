from Imports.MainData import *
data["dataInit"] = True
from Game.Controller import Controller
from Game.Update import *
data["init"] = True

def frame(): pygame.time.delay(math.floor(1000/data["fps"]))

def main():
    Controller()
    Update()