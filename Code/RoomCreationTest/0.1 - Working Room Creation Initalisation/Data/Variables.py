from asyncio.windows_events import NULL
import pygame
import math
import sys
import glob
import os

pygame.init()

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

display = {

    "window" : {},

    "grid" : {

        "tileSize" : 16,
        "width" : 17,
        "height" : 13,
        "scale" : 4,
    },

}

display["window"]["width"] = ( ( display["grid"]["width"] ) * display["grid"]["tileSize"] ) * display["grid"]["scale"]
display["window"]["height"] = ( ( display["grid"]["height"] ) * display["grid"]["tileSize"] ) * display["grid"]["scale"]

Window = pygame.display.set_mode((display["window"]["width"],display["window"]["height"]))
Grid = pygame.Surface((((display["grid"]["width"])*display["grid"]["tileSize"]),((display["grid"]["height"])*display["grid"]["tileSize"])))
h1 = pygame.font.Font('freesansbold.ttf', 24)
h2 = pygame.font.Font('freesansbold.ttf', 20)
p = pygame.font.Font('freesansbold.ttf', 16)

render = {}
button = {}
dataEntry = {}

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

data = {

    "varInit" : False,
    "init" : False,
    "game" : "menu_select"

}

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

grid = {

    "room" : "",
    "lockXL" : False,
    "lockXR" : False,
    "lockYL" : False,
    "lockYR" : False,
    "offsetX" : 0,
    "offsetY" : 0,

}

for x in range(display["grid"]["width"]+1):
    for y in range(display["grid"]["height"]+1):
        for l in range(5):
            grid[f"{str(l)}_{str(x)}_{str(y)}"] = ""

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

player = {

"sprite" : "", #"asset_sprite_default" #"color_orange"
"spriteWidth" : 0,
"spriteHeight" : 0,
"spriteColorWidth" : 16,
"spriteColorHeight" : 22,
"spriteState" : 0,
"spriteFrames" : 0,
"spriteDirection" : "down",
"spriteMoving" : False,
"spriteToLeft" : False,
"spriteToRight" : False,
"roomX" : 0,
"roomY" : 0,
"gridX" : 0,
"gridY" : 0,
"hitboxSize" : 1,
"movementSpeed" : 1

}

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

controller = {

    "mouse" : pygame.mouse.get_pos(),
    "click" : False,
    "up" : {0:False,1:False},
    "down" : {0:False,1:False},
    "left" : {0:False,1:False},
    "right" : {0:False,1:False},
    "sprint" : False,
    "enter" : False,
    "backspace" : False,
    "type" : ""

}

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

if data["varInit"] == False:

    f = open("./Txt/player.txt","r")
    temp_Variables_fileStore = f.readline()
    temp_Variables_fileStore = temp_Variables_fileStore.split(":")

    for i in range(len(temp_Variables_fileStore)-1):

        temp_Variables_varStore = temp_Variables_fileStore[i]
        temp_Variables_varStore = temp_Variables_varStore.split("-")
        if temp_Variables_varStore[0] == "sprite": player["sprite"] = temp_Variables_varStore[1]
        elif temp_Variables_varStore[0] == "room": grid["room"] = temp_Variables_varStore[1]
        elif temp_Variables_varStore[0] == "roomX": player["roomX"] = ((int(temp_Variables_varStore[1]))*16)+9
        elif temp_Variables_varStore[0] == "roomY": player["roomY"] = ((int(temp_Variables_varStore[1]))*16)+9

    f.close()
        
# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

color = {}
asset = {}
room = {}

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

DirectionArray = ["up","down","left","right"]
OffsetArray = [-8,-9,-10,-11,-12,-13,-14,-15,-16,-1,-2,-3,-4,-5,-6,-7]

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #