from Imports.Data import *

def SpriteCycle(moving):
    if moving == True:
        if data["player"]["spriteMoving"] == False:
            data["player"]["spriteMoving"] = True
            data["player"]["spriteFrames"] = 0
            data["player"]["spriteState"] = 2
            data["player"]["spriteToLeft"] = True
            data["player"]["spriteToRight"] = False
        else:
            data["player"]["spriteFrames"] += 1
            if data["player"]["spriteFrames"] >= 4:
                data["player"]["spriteFrames"] = 0

                if data["player"]["spriteState"] == 2: 
                    data["player"]["spriteState"] += 1
                    data["player"]["spriteToRight"] = True
                    data["player"]["spriteToLeft"] = False
                elif data["player"]["spriteState"] == 3 and data["player"]["spriteToLeft"] == True: data["player"]["spriteState"] -= 1
                elif data["player"]["spriteState"] == 3 and data["player"]["spriteToRight"] == True: data["player"]["spriteState"] += 1
                elif data["player"]["spriteState"] == 4: 
                    data["player"]["spriteState"] -= 1
                    data["player"]["spriteToRight"] = False
                    data["player"]["spriteToLeft"] = True

    else:
        if data["player"]["spriteMoving"] == True:
                data["player"]["spriteMoving"] = False
                data["player"]["spriteFrames"] = 0
                data["player"]["spriteState"] = 0
        else:
            data["player"]["spriteFrames"] += 1
            if data["player"]["spriteFrames"] >= 8:
                data["player"]["spriteFrames"] = 0
                if data["player"]["spriteState"] == 0: data["player"]["spriteState"] = 1
                else: data["player"]["spriteState"] = 0