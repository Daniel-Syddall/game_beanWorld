from Imports.Data import *
from Functions.RenderMap import *
from Functions.Move import *

def Init():
    PlayerSprite = data["player"]["sprite"]
    PlayerSprite = PlayerSprite.split("-")
    if PlayerSprite[0] == "color":
        data["player"]["spriteWidth"] = data["player"]["spriteColorWidth"]
        data["player"]["spriteHeight"] = data["player"]["spriteColorHeight"]
    elif PlayerSprite[0] == "asset":
        data["player"]["spriteWidth"] = asset[PlayerSprite[1]][PlayerSprite[2]+"-"+data["player"]["spriteDirection"]+"-"+str(data["player"]["spriteState"])].get_width()
        data["player"]["spriteHeight"] = asset[PlayerSprite[1]][PlayerSprite[2]+"-"+data["player"]["spriteDirection"]+"-"+str(data["player"]["spriteState"])].get_height()
        print()

    RenderMap(data["map"]["room"],True,0)
    Move()
