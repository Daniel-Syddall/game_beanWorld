from Imports.Data import *
from Functions.RenderMap import *
from Functions.Move import *

def LoadNewRoom(CurrentRoom,roomX,roomY):
    spawnFound = False
    sendValue = 0
    count = 0

    while spawnFound == False:
        if room[CurrentRoom]["send-"+str(count)+"-X"] == roomX and room[CurrentRoom]["send-"+str(count)+"-Y"] == roomY:
            spawnFound = True
            sendValue = count
        else:count += 1

    data["map"]["room"] = room[CurrentRoom]["send-"+str(sendValue)+"-room"]
    data["map"]["maxX"] = room[sendValue]["maxX"]
    data["map"]["maxY"] = room[sendValue]["maxY"]

    RenderMap(data["map"]["room"],True,room[CurrentRoom]["send-"+str(sendValue)+"-spawn"])