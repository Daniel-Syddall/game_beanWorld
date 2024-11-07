from Data.Const import *

data = {}

data["dataInit"] = False
data["init"] = False
data["fps"] = 60
data["GameState"] = "Overworld"
gameState = NULL

controller = {
    "mouse" : pygame.mouse.get_pos(),
    "click" : False,
    "backspace" : False,
    "type" : ""
}

color = {}
asset = {}

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = = #

# Custom Variables #

custom = {}

from Game.Main.Func.RPG.Main import RPG
rpg = RPG()
rpg.Run()

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = = #