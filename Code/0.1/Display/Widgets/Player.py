from Imports.Data import *

def Widgets_Player():
    global map
    sprite = data["player"]["sprite"]
    sprite = sprite.split("-")


    playerCounterOffsetArrayThingy = [9,10,11,12,13,14,15,16,1,2,3,4,5,6,7,8]
    if data["map"]["lockXL"] == False and data["map"]["lockXR"] == False and data["map"]["maxX"] != 17: playerCounterOffsetX = playerCounterOffsetArrayThingy[data["player"]["roomX"]%16]
    else: playerCounterOffsetX = 0
    if data["map"]["lockYL"] == False and data["map"]["lockYR"] == False and data["map"]["maxY"] != 13: playerCounterOffsetY = playerCounterOffsetArrayThingy[data["player"]["roomY"]%16]
    else: playerCounterOffsetY = 0

    if sprite[0] == "color":
        pygame.draw.rect(map,color[sprite[1]+"_"+data["player"]["spriteDirection"]+"_"+str(data["player"]["spriteState"])],((playerCounterOffsetX+data["player"]["gridX"])-(math.floor(data["player"]["spriteWidth"]/2)),(playerCounterOffsetY+data["player"]["gridY"])-data["player"]["spriteHeight"],data["player"]["spriteWidth"],data["player"]["spriteHeight"]))
    elif sprite[0] == "asset":
        map.blit(asset[sprite[1]][sprite[2]+"-"+data["player"]["spriteDirection"]+"-"+str(data["player"]["spriteState"])],(((playerCounterOffsetX+data["player"]["gridX"])-(math.floor(data["player"]["spriteWidth"]/2))),(playerCounterOffsetY+data["player"]["gridY"]-data["player"]["spriteHeight"])))