from asyncio.windows_events import NULL
import pygame
import math
import array
import time

display = {}
display["window"] = {}
display["window"]["width"] = 1088
display["window"]["height"] = 832
display["map"] = {}
display["map"]["tileSize"] = 16
display["map"]["width"] = 17
display["map"]["height"] = 13
display["map"]["scale"] = 4
window = pygame.display.set_mode((display["window"]["width"],display["window"]["height"]))
map = pygame.Surface(((display["map"]["width"]*display["map"]["tileSize"]),(display["map"]["height"]*display["map"]["tileSize"])))

data = {}
asset = {}
color = {}
room = {}

data["init"] = False
data["pause"] = False
data["display"] = "map"
data["frames"] = 0

data["map"] = {}
data["map"]["room"] = 0
for x in range(18):
    for y in range(14):
        data["map"][f"state-{str(x)}-{str(y)}"] = 0
        for l in range(4):
            data["map"][f"{str(l)}-{str(x)}-{str(y)}"] = ""
data["map"]["maxX"] = 0
data["map"]["maxY"] = 0
data["map"]["lockXL"] = False
data["map"]["lockXR"] = False
data["map"]["lockYL"] = False
data["map"]["lockYR"] = False
data["map"]["offsetX"] = 0
data["map"]["offsetY"] = 0

data["player"] = {}
data["player"]["sprite"] = "color-orange" #"asset-sprite-default" #"color-orange"
data["player"]["spriteWidth"] = 0
data["player"]["spriteHeight"] = 0
data["player"]["spriteColorWidth"] = 16
data["player"]["spriteColorHeight"] = 22
data["player"]["spriteState"] = 0
data["player"]["spriteFrames"] = 0
data["player"]["spriteDirection"] = "down"
data["player"]["spriteMoving"] = False
data["player"]["spriteToLeft"] = False
data["player"]["spriteToRight"] = False

data["player"]["roomX"] = 0
data["player"]["roomY"] = 0
data["player"]["gridX"] = 0
data["player"]["gridY"] = 0
data["player"]["hitboxSize"] = 1
data["player"]["movementSpeed"] = 1

data["controller"] = {}
data["controller"]["mouse"] = pygame.mouse.get_pos()
data["controller"]["click"] = False
data["controller"]["up0"] = False
data["controller"]["up1"] = False
data["controller"]["down0"] = False
data["controller"]["down1"] = False
data["controller"]["left0"] = False
data["controller"]["left1"] = False
data["controller"]["right0"] = False
data["controller"]["right1"] = False