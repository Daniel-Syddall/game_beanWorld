from Data.Variables import *

if data["varInit"] == False:

    # - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

    f = open("./Txt/color.txt","r")
    temp_Assets_fileStore = f.readline()
    temp_Assets_fileStore = temp_Assets_fileStore.split(":")
    temp_Assets_fileStore = temp_Assets_fileStore[0]
    temp_Assets_fileStore = temp_Assets_fileStore.split("-")

    for _ in range(int(temp_Assets_fileStore[1])):
        temp_Assets_fileStore = f.readline()
        temp_Assets_fileStore = temp_Assets_fileStore.split(":")
        temp_Assets_fileStore = temp_Assets_fileStore[0]
        temp_Assets_fileStore = temp_Assets_fileStore.split("-")
        color[temp_Assets_fileStore[0]] = (int(temp_Assets_fileStore[1]),int(temp_Assets_fileStore[2]),int(temp_Assets_fileStore[3]))

    f.close()

    # - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #

    f = open("./Txt/asset.txt","r")

    temp_Assets_fileStore = f.readline()
    temp_Assets_fileStore = temp_Assets_fileStore.split(":")
    temp_Assets_subStore = temp_Assets_fileStore[0]
    temp_Assets_subStore = temp_Assets_subStore.split("-")
    temp_Assets_spriteCount = temp_Assets_subStore[1]
    temp_Assets_subStore = temp_Assets_fileStore[1]
    temp_Assets_subStore = temp_Assets_subStore.split("-")
    temp_Assets_tileCount = temp_Assets_subStore[1]

    asset["sprite"] = {}

    for _ in range(int(temp_Assets_spriteCount)):
        temp_Assets_fileStore = f.readline()
        temp_Assets_fileStore = temp_Assets_fileStore.split(":")
        for d in range(len(DirectionArray)):
            for i in range(5):
                asset["sprite"][f"{temp_Assets_fileStore[0]}_{DirectionArray[d]}_{str(i)}"] = pygame.image.load(f"./Assets/sprite/{temp_Assets_fileStore[0]}_{DirectionArray[d]}_{str(i)}.png")

    asset["tile"] = {}

    for _ in range(int(temp_Assets_tileCount)):
        temp_Assets_fileStore = f.readline()
        temp_Assets_fileStore = temp_Assets_fileStore.split(":")
        asset["tile"][temp_Assets_fileStore[0]] = pygame.image.load(f"./Assets/tile/{temp_Assets_fileStore[0]}.png")

    f.close()

    # - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - = = - - #