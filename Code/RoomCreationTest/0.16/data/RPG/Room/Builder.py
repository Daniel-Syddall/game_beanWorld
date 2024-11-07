import math
from random import randint as random
from asyncio.windows_events import NULL

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_GetLowAndHigh(StartX,StartY,EndX,EndY):
    if StartX <= EndX:
        LowX = StartX
        HighX = EndX
    elif EndY < StartX:
        LowX = EndY
        HighX = StartY
    if StartY <= EndY:
        LowY = StartY
        HighY = EndY
    elif EndY < StartY:
        LowY = EndY
        HighY = StartY
    return LowX,HighX,LowY,HighY

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_Build(self,RoomName,RoomWidth,RoomHeight,Fill,Border):
    self.room[RoomName] = {}
    self.room[RoomName]["sendCount"] = 0
    self.room[RoomName]["eventCount"] = 0
    self.room[RoomName]["maxX"] = RoomWidth
    self.room[RoomName]["maxY"] = RoomHeight
    for i in range(6): self.room[RoomName]["hue_"+str(i)] = "0_0_0_0"
    for x in range(RoomWidth+1):
        for y in range(RoomHeight+1):
            self.room[RoomName][f"state_{str(x)}_{str(y)}"] = ""
            for l in range(6):
                self.room[RoomName][f"{str(l)}_{str(x)}_{str(y)}"] = ""
    for x in range(RoomWidth-2):
        for y in range(RoomHeight-2):
            self.room[RoomName][f"state_{str(x+1)}_{str(y+1)}"] = "pass"
            if Fill != "": self.room[RoomName][f"1_{str(x+1)}_{str(y+1)}"] = Fill
    for x in range(RoomWidth):
        self.room[RoomName][f"state_{str(x)}_0"] = ""
        if Border != "": self.room[RoomName][f"1_{str(x)}_0"] = Border
        self.room[RoomName][f"state_{str(x)}_{str(RoomHeight-1)}"] = ""
        if Border != "": self.room[RoomName][f"1_{str(x)}_{str(RoomHeight-1)}"] = Border
    for y in range(RoomHeight):
        self.room[RoomName][f"state_0_{str(y)}"] = ""
        if Border != "": self.room[RoomName][f"1_0_{str(y)}"] = Border
        self.room[RoomName][f"state_{str(RoomWidth-1)}_{str(y)}"] = ""
        if Border != "": self.room[RoomName][f"1_{str(RoomWidth-1)}_{str(y)}"] = Border
    for x in range(RoomWidth+1):
        self.room[RoomName][f"state_{str(x)}_{str(RoomHeight)}"] = ""
        self.room[RoomName][f"1_{str(x)}_{str(RoomHeight)}"] = ""
    for y in range(RoomHeight+1):
        self.room[RoomName][f"state_{str(RoomWidth)}_{str(y)}"] = ""
        self.room[RoomName][f"1_{str(RoomWidth)}_{str(y)}"] = ""

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_SetGround(self,RoomName,StartX,StartY,EndX,EndY,Ground1,Ground2):
    LowX,HighX,LowY,HighY = Room_GetLowAndHigh(StartX,StartY,EndX,EndY)

    if Ground1 != "":
        for x in range((HighX-LowX)+1):
            self.room[RoomName][f"1_{str(x+LowX)}_{str(LowY)}"] = "tile_ground_"+Ground1+"_full"
            self.room[RoomName][f"1_{str(x+LowX)}_{str(HighY)}"] = "tile_ground_"+Ground1+"_full"
        for y in range((HighY-LowY)+1):
            self.room[RoomName][f"1_{str(LowX)}_{str(y+LowY)}"] = "tile_ground_"+Ground1+"_full"
            self.room[RoomName][f"1_{str(HighX)}_{str(y+LowY)}"] = "tile_ground_"+Ground1+"_full"
    if HighX - LowX >= 2 and HighY - LowY >= 2:
        for x in range((HighX-LowX)-1):
            for y in range((HighY-LowY)-1): self.room[RoomName][f"1_{str(x+1+LowX)}_{str(y+1+LowY)}"] = ""

    self.room[RoomName][f"2_{str(LowX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_left+up"
    self.room[RoomName][f"2_{str(HighX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_up+right"
    self.room[RoomName][f"2_{str(HighX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_right+down"
    self.room[RoomName][f"2_{str(LowX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_down+left"

    for x in range((HighX-LowX-1)): self.room[RoomName][f"2_{str(x+1+LowX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_up"
    for y in range((HighY-LowY-1)): self.room[RoomName][f"2_{str(HighX)}_{str(y+1+LowX)}"] = "tile_ground_"+Ground2+"_right"
    for x in range((HighX-LowX-1)): self.room[RoomName][f"2_{str(x+1+LowX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_down"
    for y in range((HighY-LowY-1)): self.room[RoomName][f"2_{str(LowX)}_{str(y+1+LowX)}"] = "tile_ground_"+Ground2+"_left"
    for x in range((HighX-LowX)-1):
        for y in range((HighY-LowY)-1): self.room[RoomName][f"2_{str(x+1+LowX)}_{str(y+1+LowY)}"] = "tile_ground_"+Ground2+"_full"

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_SetEdge(self,RoomName,StartX,StartY,EndX,EndY,Edge,Ground):
    LowX,HighX,LowY,HighY = Room_GetLowAndHigh(StartX,StartY,EndX,EndY)

    if HighX - LowX >= 2 and HighY - LowY >= 2:
        for x in range((HighX-LowX)-1):
            for y in range((HighY-LowY)-1): self.room[RoomName][f"1_{str(x+1+LowX)}_{str(y+1+LowY)}"] = ""

    self.room[RoomName][f"1_{str(LowX)}_{str(LowY)}"] = "tile_edge_"+Ground+"_left+up"
    self.room[RoomName][f"1_{str(HighX)}_{str(LowY)}"] = "tile_edge_"+Ground+"_up+right"
    self.room[RoomName][f"1_{str(HighX)}_{str(HighY)}"] = "tile_edge_"+Ground+"_right+down-0"
    self.room[RoomName][f"1_{str(LowX)}_{str(HighY)}"] = "tile_edge_"+Ground+"_down-0+left"

    for x in range((HighX-LowX-1)): self.room[RoomName][f"1_{str(x+1+LowX)}_{str(LowY)}"] = "tile_edge_"+Edge+"_up"
    for y in range((HighY-LowY-1)): self.room[RoomName][f"1_{str(HighX)}_{str(y+1+LowX)}"] = "tile_edge_"+Edge+"_right"
    for x in range((HighX-LowX-1)): self.room[RoomName][f"1_{str(x+1+LowX)}_{str(HighY)}"] = "tile_edge_"+Edge+"_down-0"
    for y in range((HighY-LowY-1)): self.room[RoomName][f"1_{str(LowX)}_{str(y+1+LowX)}"] = "tile_edge_"+Edge+"_left"

    if HighY < self.room[RoomName]["maxY"]-1: 
        for x in range((HighX-LowX-1)): self.room[RoomName][f"1_{str(x+1+LowX)}_{str(HighY+1)}"] = "tile_edge_"+Edge+"_down-1"
        self.room[RoomName][f"1_{str(HighX)}_{str(HighY+1)}"] = "tile_edge_"+Ground+"_right+down-1"
        self.room[RoomName][f"1_{str(LowX)}_{str(HighY+1)}"] = "tile_edge_"+Ground+"_down-1+left"
    

    self.room[RoomName][f"2_{str(LowX)}_{str(LowY)}"] = "tile_ground_"+Ground+"_left+up"
    self.room[RoomName][f"2_{str(HighX)}_{str(LowY)}"] = "tile_ground_"+Ground+"_up+right"
    self.room[RoomName][f"2_{str(HighX)}_{str(HighY)}"] = "tile_ground_"+Ground+"_right+down"
    self.room[RoomName][f"2_{str(LowX)}_{str(HighY)}"] = "tile_ground_"+Ground+"_down+left"

    for x in range((HighX-LowX-1)): self.room[RoomName][f"2_{str(x+1+LowX)}_{str(LowY)}"] = "tile_ground_"+Ground+"_up"
    for y in range((HighY-LowY-1)): self.room[RoomName][f"2_{str(HighX)}_{str(y+1+LowX)}"] = "tile_ground_"+Ground+"_right"
    for x in range((HighX-LowX-1)): self.room[RoomName][f"2_{str(x+1+LowX)}_{str(HighY)}"] = "tile_ground_"+Ground+"_down"
    for y in range((HighY-LowY-1)): self.room[RoomName][f"2_{str(LowX)}_{str(y+1+LowX)}"] = "tile_ground_"+Ground+"_left"
    for x in range((HighX-LowX)-1):
        for y in range((HighY-LowY)-1): self.room[RoomName][f"2_{str(x+1+LowX)}_{str(y+1+LowY)}"] = "tile_ground_"+Ground+"_full"

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_GroundDisturbance(self,RoomName,StartX,StartY,EndX,EndY,Ground1,Ground2):
    LowX,HighX,LowY,HighY = Room_GetLowAndHigh(StartX-1,StartY-1,EndX+1,EndY+1)

    if Ground1 != "":
        for x in range((HighX-LowX)+1):
            self.room[RoomName][f"1_{str(x+LowX)}_{str(LowY)}"] = "tile_ground_"+Ground1+"_full"
            self.room[RoomName][f"1_{str(x+LowX)}_{str(HighY)}"] = "tile_ground_"+Ground1+"_full"
        for y in range((HighY-LowY)+1):
            self.room[RoomName][f"1_{str(LowX)}_{str(y+LowY)}"] = "tile_ground_"+Ground1+"_full"
            self.room[RoomName][f"1_{str(HighX)}_{str(y+LowY)}"] = "tile_ground_"+Ground1+"_full"
    if HighX - LowX >= 2 and HighY - LowY >= 2:
        for x in range((HighX-LowX)-1):
            for y in range((HighY-LowY)-1): self.room[RoomName][f"1_{str(x+1+LowX)}_{str(y+1+LowY)}"] = ""

    self.room[RoomName][f"2_{str(LowX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_downRight"
    self.room[RoomName][f"2_{str(HighX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_downLeft"
    self.room[RoomName][f"2_{str(HighX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_upLeft"
    self.room[RoomName][f"2_{str(LowX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_upRight"

    for x in range((HighX-LowX-1)): 
        self.room[RoomName][f"2_{str(x+1+LowX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_down"
        self.room[RoomName][f"2_{str(x+1+LowX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_up"

    for y in range((HighY-LowY-1)): 
        self.room[RoomName][f"2_{str(HighX)}_{str(y+1+LowY)}"] = "tile_ground_"+Ground2+"_left"
        self.room[RoomName][f"2_{str(LowX)}_{str(y+1+LowY)}"] = "tile_ground_"+Ground2+"_right"
        
    for x in range((HighX-LowX)-1):
        for y in range((HighY-LowY)-1): self.room[RoomName][f"3_{str(x+1+LowX)}_{str(y+1+LowY)}"] = ""

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_BuildGroupDecor(self,RoomName,layer,x,width,y,height,decorName):
    for w in range(width):
        for h in range(height):
            self.room[RoomName][f"{str(layer)}_{str(x+w)}_{str(y+h)}"] = "tile_decor_"+decorName+"-"+str(w)+"-"+str(h)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_ChangeLayerHue(self,RoomName,layer,hue): self.room[RoomName]["hue_"+str(layer)] = hue

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_ChangeState(self,RoomName,state,StartX,StartY,EndX,EndY):
    LowX,HighX,LowY,HighY = Room_GetLowAndHigh(StartX,StartY,EndX,EndY)
    for x in range((HighX-LowX)+1):
        for y in range((HighY-LowY)+1):
            self.room[RoomName][f"state_{str(x+LowX)}_{str(y+LowY)}"] = state

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_CreateWall(self,RoomName,layer,StartX,StartY,EndX,EndY,WallFill,WallState):
    LowX,HighX,LowY,HighY = Room_GetLowAndHigh(StartX,StartY,EndX,EndY)
    for x in range((HighX-LowX)+1):
        for y in range((HighY-LowY)+1):
            self.room[RoomName][f"{str(layer)}_{str(x+LowX)}_{str(y+LowY)}"] = WallFill
            if WallState != "na": self.room[RoomName][f"state_{str(x+LowX)}_{str(y+LowY)}"] = WallState

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_CreateBlock(self,RoomName,layer,x,y,BlockFill,BlockState):
    self.room[RoomName][f"{str(layer)}_{str(x)}_{str(y)}"] = BlockFill
    if BlockState != "na": self.room[RoomName][f"state_{str(x)}_{str(y)}"] = BlockState

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_CreateSend(self,SendRoom,SendX,SendY,SpawnRoom,SpawnX,SpawnY):
    SendID = str(self.room[SendRoom]["sendCount"])
    self.room[SendRoom][f"state_{str(SendX)}_{str(SendY)}"] = "send"
    self.room[SendRoom][f"send_{str(SendID)}_x"] = SendX
    self.room[SendRoom][f"send_{str(SendID)}_y"] = SendY
    self.room[SendRoom][f"spawn_{str(SendID)}_room"] = SpawnRoom
    self.room[SendRoom][f"spawn_{str(SendID)}_x"] = SpawnX
    self.room[SendRoom][f"spawn_{str(SendID)}_y"] = SpawnY
    self.room[SendRoom]["sendCount"] += 1

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_CreateEvent(self,RoomName,Event,triggerType):
    EventID = str(self.room[RoomName]["eventCount"])
    self.room[RoomName][f"event_{EventID}"] = Event
    self.room[RoomName][f"event_{EventID}_triggerType"] = triggerType
    self.room[RoomName]["eventCount"] += 1

    """
    # PASSIVE EVENT TEMPLATE#

    class test0_event_0:
        def __init__(self,Self):
            self.rpg = Self
        def Run(self):
            pass

    Room_CreateEvent(self,"test0",test0_event_0(self),0,"passive")
    """

    """
    # TRIGGER EVENT TEMPLATE#
    class test0_event_0:
        def __init__(self,Self):
            self.rpg = Self
        def Run(self):
            pass
        def Check(self):
            pass
    """

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #