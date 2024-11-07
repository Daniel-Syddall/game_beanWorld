import pygame
import math

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

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

data = {

    "varInit" : False,
    "init" : False,
    "game" : "grid"

}

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

grid = {

    "room" : "test0",
    "lockXL" : False,
    "lockXR" : False,
    "lockYL" : False,
    "lockYR" : False,
    "offsetX" : 0,
    "offsetY" : 0,

}

for x in range(display["grid"]["width"]+1):
    for y in range(display["grid"]["height"]+1):
        for l in range(4):
            grid[f"{str(l)}_{str(x)}_{str(y)}"] = ""

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

player = {

"sprite" : "asset_sprite_default", #"asset_sprite_default" #"color_orange"
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
    "sprint" : False

}

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

color = {}
asset = {}

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

room = {}
room["test0"] = {}
room["test1"] = {}
room["test2"] = {}

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

spriteNameArray = ["default"]
mergeNameArray = [["louis",2,2]]

OffsetArray = [-8,-9,-10,-11,-12,-13,-14,-15,-16,-1,-2,-3,-4,-5,-6,-7]

# - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #