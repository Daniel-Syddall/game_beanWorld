from Data.Variables import *

if data["varInit"] == False:

    # - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

    f = open("./Txt/color.txt","r")
    temp_Assets_fileStore = f.readline()
    temp_Assets_fileStore = temp_Assets_fileStore.split(":")

    for i in range(len(temp_Assets_fileStore)-1):
        varStore = temp_Assets_fileStore[i]
        varStore = varStore.split("-")
        color[varStore[0]] = (int(varStore[1]),int(varStore[2]),int(varStore[3]))

    f.close()

    # - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

    f = open("./Txt/asset.txt","r")
    temp_Assets_fileStore = f.readline()
    temp_Assets_fileStore = temp_Assets_fileStore.split(":")
    temp_Assets_fileStore.pop(0)
    asset["sprite"] = {}

    for s in range(len(temp_Assets_fileStore)-1):
        for d in range(len(DirectionArray)):
            for i in range(5):
                asset["sprite"][f"{temp_Assets_fileStore[s]}_{DirectionArray[d]}_{str(i)}"] = pygame.image.load(f"./Assets/sprite/{temp_Assets_fileStore[s]}_{DirectionArray[d]}_{str(i)}.png")

    temp_Assets_fileStore = f.readline()
    temp_Assets_fileStore = temp_Assets_fileStore.split(":")
    temp_Assets_fileStore.pop(0)
    asset["tile"] = {}

    for m in range(len(temp_Assets_fileStore)-1):
        asset["tile"][temp_Assets_fileStore[m]] = pygame.image.load(f"./Assets/tile/{temp_Assets_fileStore[m]}.png")

    f.close()

    # - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #