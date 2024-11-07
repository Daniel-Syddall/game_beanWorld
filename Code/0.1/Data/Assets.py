from Data.Main import *

from Data.Main import data
from Data.Main import color
from Data.Main import asset

color["white"] = (255,255,255)
color["black"] = (0,0,0)
color["orange"] = (250,130,10)

DirectionArray = ["up","down","left","right"]

colorStateArrayThingy = [(240,113,10),(196,93,8),(148,49,19),(173,51,14),(224,68,20)]
for i in range(4):
    for s in range(5):
        color["orange_"+DirectionArray[i]+"_"+str(s)] = colorStateArrayThingy[s]

spriteNameArray = ["default"]

asset["sprite"] = {}

for s in range(len(spriteNameArray)):
    for d in range(len(DirectionArray)):
        for i in range(5):
            asset["sprite"][f"{spriteNameArray[s]}-{DirectionArray[d]}-{str(i)}"] = pygame.image.load(f"./Assets/sprite/{spriteNameArray[s]}-{DirectionArray[d]}-{str(i)}.png")