from Imports.Data import *

def RenderMap(Room,Spawn,SpawnArea):
    if Spawn == True:
        data["map"]["room"] = Room
        data["player"]["roomX"] = (room[data["map"]["room"]]["spawn"+str(SpawnArea)+"X"]*16)+9
        data["player"]["roomY"] = (room[data["map"]["room"]]["spawn"+str(SpawnArea)+"Y"]*16)+9
        data["map"]["maxX"] = room[data["map"]["room"]]["maxX"]
        data["map"]["maxY"] = room[data["map"]["room"]]["maxY"]

    def Render(x2,y2):
        for x1 in range(18):
            for y1 in range(14):
                data["map"]["state-"+str(x1)+"-"+str(y1)] = room[data["map"]["room"]]["state-"+str(x1+x2)+"-"+str(y1+y2)]
                for l in range(4):
                    data["map"][str(l)+"-"+str(x1)+"-"+str(y1)] = room[data["map"]["room"]][str(l)+"-"+str(x1+x2)+"-"+str(y1+y2)]

    if data["player"]["roomX"] <= 136 or data["map"]["maxX"] == 17: 
        data["map"]["lockXL"] = True
        x = 0
        data["map"]["offsetX"] = 0
    else: data["map"]["lockXL"] = False

    if data["player"]["roomX"] >= ((data["map"]["maxX"]*16)-135): 
        data["map"]["lockXR"] = True
        x = data["map"]["maxX"] - 17
        data["map"]["offsetX"] = 0
    else: data["map"]["lockXR"] = False

    if data["player"]["roomY"] <= (104+(math.floor(data["player"]["spriteHeight"]/2))) or data["map"]["maxY"] == 13:
        data["map"]["lockYL"] = True
        y = 0
        data["map"]["offsetY"] = 0
    else: data["map"]["lockYL"] = False

    if data["player"]["roomY"] >= ((data["map"]["maxY"]*16)-(103-(math.floor(data["player"]["spriteHeight"]/2)))): 
        data["map"]["lockYR"] = True
        y = data["map"]["maxY"] - 13
        data["map"]["offsetY"] = 0
    else: data["map"]["lockYR"] = False

    OffsetArray = [-9,-10,-11,-12,-13,-14,-15,-16,-1,-2,-3,-4,-5,-6,-7,-8]

    if data["map"]["lockXL"] == False and data["map"]["lockXR"] == False:
        data["map"]["offsetX"] = OffsetArray[data["player"]["roomX"]%16]
        if data["player"]["roomX"]%16 <= 8:
            x = math.floor(data["player"]["roomX"]/16) - 9
        elif data["player"]["roomX"]%16 >= 9:
            x = math.floor(data["player"]["roomX"]/16) - 8
    
    if data["map"]["lockYL"] == False and data["map"]["lockYR"] == False:
        data["map"]["offsetY"] = OffsetArray[data["player"]["roomY"]%16]
        if data["player"]["roomY"]%16 <= 8:
            y = math.floor(data["player"]["roomY"]/16) - 7
        elif data["player"]["roomY"]%16 >= 9:
            y = math.floor(data["player"]["roomY"]/16) - 6

    Render(x,y)