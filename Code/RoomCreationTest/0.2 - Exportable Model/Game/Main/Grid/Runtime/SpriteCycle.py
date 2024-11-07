from Imports.Data import *

def Grid_SpriteCycle():
    if controller["sprint"] == True: SpriteCycle_FrameCapMultiplier = 2
    elif controller["sprint"] == False: SpriteCycle_FrameCapMultiplier = 1

    if controller["up"][0] == True or controller["up"][1] == True or controller["down"][0] == True or controller["down"][1] == True or controller["left"][0] == True or controller["left"][1] == True or controller["right"][0] == True or controller["right"][1] == True:
        if player["spriteMoving"] == False:
            player["spriteMoving"] = True
            player["spriteFrames"] = 0
            player["spriteState"] = 2
            player["spriteToLeft"] = True
            player["spriteToRight"] = False
        else:
            player["spriteFrames"] += 1
            if player["spriteFrames"] >= math.floor( 4 / SpriteCycle_FrameCapMultiplier ):
                player["spriteFrames"] = 0

                if player["spriteState"] == 2: 
                    player["spriteState"] += 1
                    player["spriteToRight"] = True
                    player["spriteToLeft"] = False
                elif player["spriteState"] == 3 and player["spriteToLeft"] == True: player["spriteState"] -= 1
                elif player["spriteState"] == 3 and player["spriteToRight"] == True: player["spriteState"] += 1
                elif player["spriteState"] == 4: 
                    player["spriteState"] -= 1
                    player["spriteToRight"] = False
                    player["spriteToLeft"] = True

    else:
        if player["spriteMoving"] == True:
                player["spriteMoving"] = False
                player["spriteFrames"] = 0
                player["spriteState"] = 0
        else:
            player["spriteFrames"] += 1
            if player["spriteFrames"] >= math.floor( 8 / SpriteCycle_FrameCapMultiplier ):
                player["spriteFrames"] = 0
                if player["spriteState"] == 0: player["spriteState"] = 1
                else: player["spriteState"] = 0