from random import randint as random

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
    self.room[RoomName]["eventCount"] = 0
    self.room[RoomName]["maxX"] = RoomWidth
    self.room[RoomName]["maxY"] = RoomHeight
    for x in range(RoomWidth+1):
        for y in range(RoomHeight+1):
            self.room[RoomName][f"state_{str(x)}_{str(y)}"] = ""
            for l in range(5):
                self.room[RoomName][f"{str(l)}_{str(x)}_{str(y)}"] = ""
    for x in range(RoomWidth-2):
        for y in range(RoomHeight-2):
            self.room[RoomName][f"state_{str(x+1)}_{str(y+1)}"] = "pass"
            self.room[RoomName][f"0_{str(x+1)}_{str(y+1)}"] = Fill
    for x in range(RoomWidth):
        self.room[RoomName][f"state_{str(x)}_0"] = ""
        self.room[RoomName][f"0_{str(x)}_0"] = Border
        self.room[RoomName][f"state_{str(x)}_{str(RoomHeight-1)}"] = ""
        self.room[RoomName][f"0_{str(x)}_{str(RoomHeight-1)}"] = Border
    for y in range(RoomHeight):
        self.room[RoomName][f"state_0_{str(y)}"] = ""
        self.room[RoomName][f"0_0_{str(y)}"] = Border
        self.room[RoomName][f"state_{str(RoomWidth-1)}_{str(y)}"] = ""
        self.room[RoomName][f"0_{str(RoomWidth-1)}_{str(y)}"] = Border
    for x in range(RoomWidth+1):
        self.room[RoomName][f"state_{str(x)}_{str(RoomHeight)}"] = ""
        self.room[RoomName][f"0_{str(x)}_{str(RoomHeight)}"] = ""
    for y in range(RoomHeight+1):
        self.room[RoomName][f"state_{str(RoomWidth)}_{str(y)}"] = ""
        self.room[RoomName][f"0_{str(RoomWidth)}_{str(y)}"] = ""

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_SetGround(self,RoomName,StartX,StartY,EndX,EndY,Ground1,Ground2):
    LowX,HighX,LowY,HighY = Room_GetLowAndHigh(StartX,StartY,EndX,EndY)

    if Ground1 != "":
        for x in range((HighX-LowX)+1):
            self.room[RoomName][f"0_{str(x+LowX)}_{str(LowY)}"] = "tile_ground_"+Ground1+"_full"
            self.room[RoomName][f"0_{str(x+LowX)}_{str(HighY)}"] = "tile_ground_"+Ground1+"_full"
        for y in range((HighY-LowY)+1):
            self.room[RoomName][f"0_{str(LowX)}_{str(y+LowY)}"] = "tile_ground_"+Ground1+"_full"
            self.room[RoomName][f"0_{str(HighX)}_{str(y+LowY)}"] = "tile_ground_"+Ground1+"_full"
    if HighX - LowX >= 2 and HighY - LowY >= 2:
        for x in range((HighX-LowX)-1):
            for y in range((HighY-LowY)-1): self.room[RoomName][f"0_{str(x+1+LowX)}_{str(y+1+LowY)}"] = ""

    self.room[RoomName][f"1_{str(LowX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_left+up"
    self.room[RoomName][f"1_{str(HighX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_up+right"
    self.room[RoomName][f"1_{str(HighX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_right+down"
    self.room[RoomName][f"1_{str(LowX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_down+left"

    for x in range((HighX-LowX-1)): self.room[RoomName][f"1_{str(x+1+LowX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_up"
    for y in range((HighY-LowY-1)): self.room[RoomName][f"1_{str(HighX)}_{str(y+1+LowX)}"] = "tile_ground_"+Ground2+"_right"
    for x in range((HighX-LowX-1)): self.room[RoomName][f"1_{str(x+1+LowX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_down"
    for y in range((HighY-LowY-1)): self.room[RoomName][f"1_{str(LowX)}_{str(y+1+LowX)}"] = "tile_ground_"+Ground2+"_left"
    for x in range((HighX-LowX)-1):
        for y in range((HighY-LowY)-1): self.room[RoomName][f"1_{str(x+1+LowX)}_{str(y+1+LowY)}"] = "tile_ground_"+Ground2+"_full"

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_GroundDisturbance(self,RoomName,StartX,StartY,EndX,EndY,Ground1,Ground2):
    StartX -= 1
    StartY -= 1
    EndX += 1
    EndY += 1
    LowX,HighX,LowY,HighY = Room_GetLowAndHigh(StartX,StartY,EndX,EndY)

    if Ground1 != "":
        for x in range((HighX-LowX)+1):
            self.room[RoomName][f"0_{str(x+LowX)}_{str(LowY)}"] = "tile_ground_"+Ground1+"_full"
            self.room[RoomName][f"0_{str(x+LowX)}_{str(HighY)}"] = "tile_ground_"+Ground1+"_full"
        for y in range((HighY-LowY)+1):
            self.room[RoomName][f"0_{str(LowX)}_{str(y+LowY)}"] = "tile_ground_"+Ground1+"_full"
            self.room[RoomName][f"0_{str(HighX)}_{str(y+LowY)}"] = "tile_ground_"+Ground1+"_full"
    if HighX - LowX >= 2 and HighY - LowY >= 2:
        for x in range((HighX-LowX)-1):
            for y in range((HighY-LowY)-1): self.room[RoomName][f"0_{str(x+1+LowX)}_{str(y+1+LowY)}"] = ""

    self.room[RoomName][f"1_{str(LowX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_downRight"
    self.room[RoomName][f"1_{str(HighX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_downLeft"
    self.room[RoomName][f"1_{str(HighX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_upLeft"
    self.room[RoomName][f"1_{str(LowX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_upRight"

    for x in range((HighX-LowX-1)): 
        self.room[RoomName][f"1_{str(x+1+LowX)}_{str(LowY)}"] = "tile_ground_"+Ground2+"_down"
        self.room[RoomName][f"1_{str(x+1+LowX)}_{str(HighY)}"] = "tile_ground_"+Ground2+"_up"

    for y in range((HighY-LowY-1)): 
        self.room[RoomName][f"1_{str(HighX)}_{str(y+1+LowY)}"] = "tile_ground_"+Ground2+"_left"
        self.room[RoomName][f"1_{str(LowX)}_{str(y+1+LowY)}"] = "tile_ground_"+Ground2+"_right"
        
    for x in range((HighX-LowX)-1):
        for y in range((HighY-LowY)-1): self.room[RoomName][f"1_{str(x+1+LowX)}_{str(y+1+LowY)}"] = ""

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
            self.room[RoomName][f"state_{str(x+LowX)}_{str(y+LowY)}"] = WallState

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_CreateBlock(self,RoomName,layer,x,y,BlockFill,BlockState):
    self.room[RoomName][f"{str(layer)}_{str(x)}_{str(y)}"] = BlockFill
    self.room[RoomName][f"state_{str(x)}_{str(y)}"] = BlockState

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_CreateSend(self,SendRoom,SendID,SendX,SendY,SendFillLayer,SendFill,SpawnRoom,SpawnID):
    self.room[SendRoom][f"{str(SendFillLayer)}_{str(SendX)}_{str(SendY)}"] = SendFill
    self.room[SendRoom][f"state_{str(SendX)}_{str(SendY)}"] = "send"
    self.room[SendRoom][f"send_{str(SendID)}_X"] = SendX
    self.room[SendRoom][f"send_{str(SendID)}_Y"] = SendY
    self.room[SendRoom][f"send_{str(SendID)}_room"] = SpawnRoom
    self.room[SendRoom][f"send_{str(SendID)}_spawn"] = SpawnID

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_CreateSpawn(self,SpawnRoom,SpawnID,SpawnX,SpawnY):
    self.room[SpawnRoom][f"spawn_{str(SpawnID)}_X"] = SpawnX
    self.room[SpawnRoom][f"spawn_{str(SpawnID)}_Y"] = SpawnY

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Room_CreateEvent(self,RoomName,Event,EventID,triggerType):
    self.room[RoomName]["eventCount"] += 1
    self.room[RoomName][f"event_{EventID}"] = Event
    self.room[RoomName][f"event_{EventID}_triggerType"] = triggerType

    """
    # EVENT TEMPLATE

    class test0_event_0:
        def __init__(self,Self):
            self.rpg = Self
        def Run(self):
            pass

    Room_CreateEvent(self,"test0",test0_event_0(self),0,"passive")
    """

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #