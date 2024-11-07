from Data.Variables import *

color = {

    "black" : (0,0,0),
    "white" : (255,255,255),
    "orange" : (250,130,10),
    "brown" : (84,47,20),
    "grey" : (122,122,122),
    "shrekGreen0" : (17,102,0),
    "shrekGreen1" : (9,51,0)

}

DirectionArray = ["up","down","left","right"]
ColorAssetTestArray = [(240,113,10),(196,93,8),(148,49,19),(173,51,14),(224,68,20)]
for d in range(4):
    for s in range(5):
        color["orange_"+DirectionArray[d]+"_"+str(s)] = ColorAssetTestArray[s]


asset["sprite"] = {}

for s in range(len(spriteNameArray)):
    for d in range(len(DirectionArray)):
        for i in range(5):
            asset["sprite"][f"{spriteNameArray[s]}_{DirectionArray[d]}_{str(i)}"] = pygame.image.load(f"./Assets/sprite/{spriteNameArray[s]}_{DirectionArray[d]}_{str(i)}.png")

asset["merge"] = {}

for m in range(len(mergeNameArray)):
    for x in range(mergeNameArray[m][1]):
        for y in range(mergeNameArray[m][2]):
            asset["merge"][f"{mergeNameArray[m][0]}_{str(x)}_{str(y)}"] = pygame.image.load(f"./Assets/merge/{mergeNameArray[m][0]}_{str(x)}_{str(y)}.png")