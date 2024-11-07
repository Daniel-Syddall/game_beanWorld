from Imports.Data import *
from Functions.LoadNewRoom import *
from Functions.RenderMap import *
from Functions.SpriteCycle import *

def Move():

    def Move_grid():
        if data["map"]["lockXL"] == False and data["map"]["lockXR"] == False: data["player"]["gridX"] = 137
        elif data["map"]["lockXL"] == True: data["player"]["gridX"] = (data["map"]["maxX"])-(data["map"]["maxX"] - data["player"]["roomX"])
        elif data["map"]["lockXR"] == True: data["player"]["gridX"] = (display["map"]["width"]*16)-((data["map"]["maxX"]*16)-data["player"]["roomX"])
        if data["map"]["lockYL"] == False and data["map"]["lockYR"] == False: data["player"]["gridY"] = (105+(math.floor(data["player"]["spriteHeight"]/2)))
        elif data["map"]["lockYL"] == True: data["player"]["gridY"] = (data["map"]["maxY"])-(data["map"]["maxY"] - data["player"]["roomY"])
        elif data["map"]["lockYR"] == True: data["player"]["gridY"] = (display["map"]["height"]*16)-((data["map"]["maxY"]*16)-data["player"]["roomY"])

    if data["init"] == False:
        Move_grid()
    else:

        moving = False

        if data["controller"]["up0"] == True or data["controller"]["up1"] == True:
            moving = True
            data["player"]["spriteDirection"] = "up"
            if room[data["map"]["room"]]["state-"+str(math.floor(data["player"]["roomX"]/16))+"-"+str(math.floor(((data["player"]["roomY"]-(data["player"]["movementSpeed"]+data["player"]["hitboxSize"]))/16)))] != 2:
                data["player"]["roomY"] = data["player"]["roomY"] - data["player"]["movementSpeed"]
                if room[data["map"]["room"]]["state-"+str(math.floor(data["player"]["roomX"]/16))+"-"+str(math.floor(((data["player"]["roomY"]-(data["player"]["movementSpeed"]+data["player"]["hitboxSize"]))/16)))] == 3:
                    LoadNewRoom(data["map"]["room"],math.floor((data["player"]["roomX"])/16),math.floor((data["player"]["roomY"])/16)-1)

        if data["controller"]["down0"] == True or data["controller"]["down1"] == True:
            moving = True
            data["player"]["spriteDirection"] = "down"
            if room[data["map"]["room"]]["state-"+str(math.floor(data["player"]["roomX"]/16))+"-"+str(math.floor(((data["player"]["roomY"]+(data["player"]["movementSpeed"]+data["player"]["hitboxSize"]))/16)))] != 2:
                data["player"]["roomY"] = data["player"]["roomY"] + data["player"]["movementSpeed"]
                if room[data["map"]["room"]]["state-"+str(math.floor(data["player"]["roomX"]/16))+"-"+str(math.floor(((data["player"]["roomY"]+(data["player"]["movementSpeed"]+data["player"]["hitboxSize"]))/16)))] == 3:
                    LoadNewRoom(data["map"]["room"],math.floor((data["player"]["roomX"])/16),math.floor((data["player"]["roomY"])/16)+1)

        if data["controller"]["left0"] == True or data["controller"]["left1"] == True:
            moving = True
            data["player"]["spriteDirection"] = "left"
            if room[data["map"]["room"]]["state-"+str(math.floor((data["player"]["roomX"]-(data["player"]["movementSpeed"]+data["player"]["hitboxSize"]+(math.floor(data["player"]["spriteWidth"]/2))))/16))+"-"+str(math.floor((data["player"]["roomY"]/16)))] != 2:
                data["player"]["roomX"] = data["player"]["roomX"] - data["player"]["movementSpeed"]
                if room[data["map"]["room"]]["state-"+str(math.floor((data["player"]["roomX"]-(data["player"]["movementSpeed"]+data["player"]["hitboxSize"]+(math.floor(data["player"]["spriteWidth"]/2))))/16))+"-"+str(math.floor((data["player"]["roomY"]/16)))] == 3:
                    LoadNewRoom(data["map"]["room"],math.floor((data["player"]["roomX"])/16)-1,math.floor((data["player"]["roomY"])/16))

        if data["controller"]["right0"] == True or data["controller"]["right1"] == True:
            moving = True
            data["player"]["spriteDirection"] = "right"
            if room[data["map"]["room"]]["state-"+str(math.floor((data["player"]["roomX"]+(data["player"]["movementSpeed"]+data["player"]["hitboxSize"]+(math.floor(data["player"]["spriteWidth"]/2))))/16))+"-"+str(math.floor((data["player"]["roomY"]/16)))] != 2:
                data["player"]["roomX"] = data["player"]["roomX"] + data["player"]["movementSpeed"]
                if room[data["map"]["room"]]["state-"+str(math.floor((data["player"]["roomX"]+(data["player"]["movementSpeed"]+data["player"]["hitboxSize"]+(math.floor(data["player"]["spriteWidth"]/2))))/16))+"-"+str(math.floor((data["player"]["roomY"]/16)))] == 3:
                    LoadNewRoom(data["map"]["room"],math.floor((data["player"]["roomX"])/16)+1,math.floor((data["player"]["roomY"])/16))

        if room[data["map"]["room"]]["state-"+str(math.floor((data["player"]["roomX"])/16))+"-"+str(math.floor((data["player"]["roomY"]/16)))] == 3: LoadNewRoom(data["map"]["room"],math.floor((data["player"]["roomX"])/16),math.floor((data["player"]["roomY"])/16))
        else: RenderMap(data["map"]["room"],False,0)

        Move_grid()

        SpriteCycle(moving)
