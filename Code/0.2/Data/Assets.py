from Data.Variables import *

color = {

    "black" : (0,0,0),
    "white" : (255,255,255),
    "orange" : (250,130,10)

}

DirectionArray = ["up","down","left","right"]
ColorAssetTestArray = [(240,113,10),(196,93,8),(148,49,19),(173,51,14),(224,68,20)]
for d in range(4):
    for s in range(5):
        color["orange_"+DirectionArray[d]+"_"+str(s)] = ColorAssetTestArray[s]


spriteNameArray = ["default"]
asset["sprite"] = {}

for s in range(len(spriteNameArray)):
    for d in range(len(DirectionArray)):
        for i in range(5):
            asset["sprite"][f"{spriteNameArray[s]}_{DirectionArray[d]}_{str(i)}"] = pygame.image.load(f"./Assets/sprite/{spriteNameArray[s]}_{DirectionArray[d]}_{str(i)}.png")