import pygame
import math

class RPG:
    def __init__(self):
        
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        self.local = "./Game/Main/Func/RPG/"

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        self.init = False
        self.displayData = {"tileSize" : 16,"width" : 17,"height" : 13}
        self.surface = pygame.Surface((self.displayData["width"]*self.displayData["tileSize"],self.displayData["height"]*self.displayData["tileSize"]))

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        self.gridData = {"room" : "test0","lockXL" : False,"lockXR" : False,"lockYL" : False,"lockYR" : False,"offsetX" : 0,"offsetY" : 0}
        self.player = {"sprite" : "default","spriteWidth" : 0,"spriteHeight" : 0,"spriteColorWidth" : 16,"spriteColorHeight" : 22,
        "spriteState" : 0,"spriteFrames" : 0,"spriteDirection" : "down","spriteMoving" : False, "spriteToLeft" : False,"spriteToRight" : False,
        "roomX" : 0,"roomY" : 0,"gridX" : 0,"gridY" : 0,"hitboxSize" : 1,"movementSpeed" : 1}
        self.controller = {"up" : False, "down" : False,"left" : False,"right" : False,"sprint" : False}
        self.color = {"black" : (0,0,0),"white" : (255,255,255),"orange" : (250,130,10),"brown" : (84,47,20),"grey" : (122,122,122),
        "shrekGreen0" : (17,102,0),"shrekGreen1" : (9,51,0)}
        self.OffsetArray = [-8,-9,-10,-11,-12,-13,-14,-15,-16,-1,-2,-3,-4,-5,-6,-7]

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        SpriteDirectionsArray = ["up","down","left","right"]
        spriteNamesArray = ["default"]
        tileNamesArray = ["louis-0-0","louis-1-0","louis-0-1","louis-1-1"]
        self.asset = {"sprite":{},"tile":{},"border":pygame.image.load(f"{self.local}/Assets/border.png")}
        for s in range(len(spriteNamesArray)):
            for d in range(len(SpriteDirectionsArray)):
                for i in range(5): self.asset["sprite"][f"{spriteNamesArray[s]}_{SpriteDirectionsArray[d]}_{str(i)}"] = pygame.image.load(f"{self.local}/Assets/Sprites/{spriteNamesArray[s]}_{SpriteDirectionsArray[d]}_{str(i)}.png")
        for i in range(len(tileNamesArray)): self.asset["tile"][f"{tileNamesArray[i]}"] = pygame.image.load(f"{self.local}/Assets/Tiles/{tileNamesArray[i]}.png")

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        self.grid = []
        for l in range(5):
            self.grid.append([])
            for x in range(self.displayData["width"]+1):
                self.grid[l].append([])
                for _ in range(self.displayData["height"]+1):
                    self.grid[l][x].append("")

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        def Room_Build(self,RoomName,RoomWidth,RoomHeight,Fill,Border):
            self.room[RoomName] = {}
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

        def Room_ChangeState(self,RoomName,state,StartX,StartY,EndX,EndY):
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
            for x in range((HighX-LowX)+1):
                for y in range((HighY-LowY)+1):
                    self.room[RoomName][f"state_{str(x+LowX)}_{str(y+LowY)}"] = state

        def Room_CreateWall(self,RoomName,layer,StartX,StartY,EndX,EndY,WallFill):
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
            for x in range((HighX-LowX)+1):
                for y in range((HighY-LowY)+1):
                    self.room[RoomName][f"{str(layer)}_{str(x+LowX)}_{str(y+LowY)}"] = WallFill

        def Room_CreateSend(self,SendRoom,SendID,SendX,SendY,SendFill,SpawnRoom,SpawnID):
            self.room[SendRoom][f"0_{str(SendX)}_{str(SendY)}"] = SendFill
            self.room[SendRoom][f"state_{str(SendX)}_{str(SendY)}"] = "send"
            self.room[SendRoom][f"send_{str(SendID)}_X"] = SendX
            self.room[SendRoom][f"send_{str(SendID)}_Y"] = SendY
            self.room[SendRoom][f"send_{str(SendID)}_room"] = SpawnRoom
            self.room[SendRoom][f"send_{str(SendID)}_spawn"] = SpawnID

        def Room_CreateSpawn(self,SpawnRoom,SpawnID,SpawnX,SpawnY):
            self.room[SpawnRoom][f"spawn_{str(SpawnID)}_X"] = SpawnX
            self.room[SpawnRoom][f"spawn_{str(SpawnID)}_Y"] = SpawnY

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        self.room = {}

        Room_Build(self,"test0",17,13,"color_white","color_orange")
        Room_CreateSend(self,"test0",0,16,10,"color_black","test1",0)
        Room_CreateSpawn(self,"test0",0,15,10)

        Room_Build(self,"test1",19,15,"color_white","color_orange")
        Room_CreateWall(self,"test1",0,4,4,14,4,"color_orange")
        Room_ChangeState(self,"test1","",4,4,14,4)
        Room_CreateWall(self,"test1",0,9,6,9,11,"color_orange")
        Room_ChangeState(self,"test1","",9,6,9,11)
        Room_CreateSend(self,"test1",0,0,2,"color_black","test0",0)
        Room_CreateSpawn(self,"test1",0,1,2)
        Room_CreateSend(self,"test1",1,16,14,"color_grey","test2",0)
        Room_CreateSpawn(self,"test1",1,16,13)
        Room_CreateSend(self,"test1",2,17,1,"color_brown","test1",3)
        Room_CreateSpawn(self,"test1",2,16,2)
        Room_CreateSend(self,"test1",3,1,13,"color_brown","test1",2)
        Room_CreateSpawn(self,"test1",3,2,12)

        Room_Build(self,"test2",30,30,"color_black","color_black")
        Room_CreateWall(self,"test2",0,2,27,4,27,"color_shrekGreen0")
        Room_ChangeState(self,"test2","",2,27,4,27)
        Room_CreateWall(self,"test2",0,3,26,3,24,"color_shrekGreen0")
        Room_ChangeState(self,"test2","",3,26,3,24)
        Room_CreateWall(self,"test2",0,3,24,3,24,"color_shrekGreen1")
        Room_CreateWall(self,"test2",0,3,27,3,27,"color_black")
        Room_ChangeState(self,"test2","pass",3,27,3,27)
        Room_ChangeState(self,"test2","",26,26,27,27)
        Room_CreateSend(self,"test2",0,27,0,"color_grey","test1",1)
        Room_CreateSpawn(self,"test2",0,27,1)
        Room_CreateWall(self,"test2",0,26,26,26,26,"tile_louis-0-0")
        Room_CreateWall(self,"test2",0,27,26,27,26,"tile_louis-1-0")
        Room_CreateWall(self,"test2",0,26,27,26,27,"tile_louis-0-1")
        Room_CreateWall(self,"test2",0,27,27,27,27,"tile_louis-1-1")

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    def Controller(self,event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP: self.controller["up"] = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN: self.controller["down"] = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT: self.controller["left"] = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT: self.controller["right"] = False
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: self.controller["sprint"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP: self.controller["up"] = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN: self.controller["down"] = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT: self.controller["left"] = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT: self.controller["right"] = True
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: self.controller["sprint"] = True

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    def Run(self):

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        def Run_GetSpriteDimensions(self):
            
            self.player["spriteWidth"] = self.asset["sprite"][self.player["sprite"]+"_"+self.player["spriteDirection"]+"_"+str(self.player["spriteState"])].get_width()
            self.player["spriteHeight"] = self.asset["sprite"][self.player["sprite"]+"_"+self.player["spriteDirection"]+"_"+str(self.player["spriteState"])].get_height()

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        def Run_PlayerEventCheck(self):

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            def Run_PlayerEventCheck_TileEvent(self,x,y,direction):

                if self.room[self.gridData["room"]]["state_"+str(math.floor(x/16))+"_"+str(math.floor((y/16)))] == "pass":

                    if direction == "up": y += ( self.player["hitboxSize"] )
                    elif direction == "down": y -= ( self.player["hitboxSize"] )
                    elif direction == "left": x += ( self.player["hitboxSize"] + ( math.floor ( self.player["spriteWidth"] / 2 ) ) )
                    elif direction == "right": x -= ( self.player["hitboxSize"] + ( math.floor ( self.player["spriteWidth"] / 2 ) ) )

                    self.player["roomX"] = x
                    self.player["roomY"] = y


                elif self.room[self.gridData["room"]]["state_"+str(math.floor(x/16))+"_"+str(math.floor((y/16)))] == "send":
                    send_found = False
                    send_count = 0
                    while send_found == False:
                        if self.room[self.gridData["room"]]["send_"+str(send_count)+"_X"] == math.floor(x/16) and self.room[self.gridData["room"]]["send_"+str(send_count)+"_Y"] == math.floor(y/16):
                            send_found = True
                        else: send_count += 1

                    send_spawn = self.room[self.gridData["room"]]["send_"+str(send_count)+"_spawn"]
                    self.gridData["room"] = self.room[self.gridData["room"]]["send_"+str(send_count)+"_room"]
                    self.player["roomX"] = (self.room[self.gridData["room"]]["spawn_"+str(send_spawn)+"_X"]*16)+10
                    self.player["roomY"] = (self.room[self.gridData["room"]]["spawn_"+str(send_spawn)+"_Y"]*16)+10

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            if self.controller["sprint"] == True: self.player["movementSpeed"] = 2
            elif self.controller["sprint"] == False: self.player["movementSpeed"] = 1

            if self.controller["up"] == True:
                self.player["spriteDirection"] = "up"
                Run_PlayerEventCheck_TileEvent(self,self.player["roomX"],self.player["roomY"] - (self.player["movementSpeed"] + self.player["hitboxSize"] ),"up")

            if self.controller["down"] == True:
                self.player["spriteDirection"] = "down"
                Run_PlayerEventCheck_TileEvent(self,self.player["roomX"],self.player["roomY"] + (self.player["movementSpeed"] + self.player["hitboxSize"] ),"down")

            if self.controller["left"] == True:
                self.player["spriteDirection"] = "left"
                Run_PlayerEventCheck_TileEvent(self,self.player["roomX"] - (self.player["movementSpeed"] + self.player["hitboxSize"] + ( math.floor( self.player["spriteWidth"] / 2 ) ) ),self.player["roomY"],"left")

            if self.controller["right"] == True or self.controller["right"] == True:
                self.player["spriteDirection"] = "right"
                Run_PlayerEventCheck_TileEvent(self,self.player["roomX"] + (self.player["movementSpeed"] + self.player["hitboxSize"] + ( math.floor( self.player["spriteWidth"] / 2 ) ) ),self.player["roomY"],"right")

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        def Run_CheckGridLock(self):
    
            if self.player["roomX"] <= 136 or self.room[self.gridData["room"]]["maxX"] == 17: 
                self.gridData["lockXL"] = True
                self.gridData["lockXR"] = False
            elif self.player["roomX"] >= ((self.room[self.gridData["room"]]["maxX"]*16)-135): 
                self.gridData["lockXR"] = True
                self.gridData["lockXL"] = False
            else: 
                self.gridData["lockXL"] = False
                self.gridData["lockXR"] = False

            if self.player["roomY"] <= (104+(math.floor(self.player["spriteHeight"]/2))) or self.room[self.gridData["room"]]["maxY"] == 13:
                self.gridData["lockYL"] = True
                self.gridData["lockYR"] = False
            elif self.player["roomY"] >= ((self.room[self.gridData["room"]]["maxY"]*16)-(103-(math.floor(self.player["spriteHeight"]/2)))): 
                self.gridData["lockYR"] = True
                self.gridData["lockYL"] = False
            else:
                self.gridData["lockYL"] = False
                self.gridData["lockYR"] = False

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        def Run_GetGridOffset(self):

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            def Run_GetGridOffset_OffsetArrayDisplacement(self,Displacement):

                ArrayDisplacementStart = -8

                for _ in range(Displacement):
                    ArrayDisplacementStart -= 1
                    if ArrayDisplacementStart == -17: ArrayDisplacementStart = -1

                DisplacementArray = []
                for _ in range(16):
                    ArrayDisplacementStart -= 1
                    if ArrayDisplacementStart == -17: ArrayDisplacementStart = -1
                    DisplacementArray.append(ArrayDisplacementStart)

                return DisplacementArray

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            OffsetArrayY = Run_GetGridOffset_OffsetArrayDisplacement(self,math.floor(self.player["spriteHeight"]/2))

            if self.gridData["lockXL"] == False and self.gridData["lockXR"] == False: self.gridData["offsetX"] = self.OffsetArray[self.player["roomX"]%16]
            else: self.gridData["offsetX"] = 0
            
            if self.gridData["lockYL"] == False and self.gridData["lockYR"] == False: self.gridData["offsetY"] = OffsetArrayY[self.player["roomY"]%16]
            else: self.gridData["offsetY"] = 0

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        def Run_RenderGridFromRoom(self):

            if self.gridData["lockXL"] == False and self.gridData["lockXR"] == False:
                if self.player["roomX"]%16 <= 8: StartX = math.floor(self.player["roomX"]/16) - 9
                elif self.player["roomX"]%16 >= 9: StartX = math.floor(self.player["roomX"]/16) - 8
            else:
                if self.gridData["lockXL"] == True: StartX = 0
                elif self.gridData["lockXR"] == True: StartX = self.room[self.gridData["room"]]["maxX"] - 17

            if self.gridData["lockYL"] == False and self.gridData["lockYR"] == False:
                StartY = math.floor(self.player["roomY"]/16) - 7
            else:
                if self.gridData["lockYL"] == True: StartY = 0
                elif self.gridData["lockYR"] == True: StartY = self.room[self.gridData["room"]]["maxY"] - 13

            for l in range(5):
                for x in range(self.displayData["width"]+1):
                    for y in range(self.displayData["height"]+1):
                        self.grid[l][x][y] = self.room[self.gridData["room"]][str(l)+"_"+str(x+StartX)+"_"+str(y+StartY)]

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        def Run_PlayerToGrid(self):

            if self.gridData["lockXL"] == False and self.gridData["lockXR"] == False: self.player["gridX"] = 137
            elif self.gridData["lockXL"] == True: self.player["gridX"] = self.player["roomX"]
            elif self.gridData["lockXR"] == True: self.player["gridX"] = (self.displayData["width"]*16)-((self.room[self.gridData["room"]]["maxX"]*16)-self.player["roomX"])

            if self.gridData["lockYL"] == False and self.gridData["lockYR"] == False: self.player["gridY"] = (105+(math.floor(self.player["spriteHeight"]/2)))
            elif self.gridData["lockYL"] == True: self.player["gridY"] = self.player["roomY"]
            elif self.gridData["lockYR"] == True: self.player["gridY"] = (self.displayData["height"]*16)-((self.room[self.gridData["room"]]["maxY"]*16)-self.player["roomY"])

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        def Run_SpriteCycle(self):
            if self.controller["sprint"] == True: SpriteCycle_FrameCapMultiplier = 2
            elif self.controller["sprint"] == False: SpriteCycle_FrameCapMultiplier = 1

            if self.controller["up"] == True or self.controller["down"] == True or self.controller["left"] == True or self.controller["right"] == True:
                if self.player["spriteMoving"] == False:
                    self.player["spriteMoving"] = True
                    self.player["spriteFrames"] = 0
                    self.player["spriteState"] = 2
                    self.player["spriteToLeft"] = True
                    self.player["spriteToRight"] = False
                else:
                    self.player["spriteFrames"] += 1
                    if self.player["spriteFrames"] >= math.floor( 4 / SpriteCycle_FrameCapMultiplier ):
                        self.player["spriteFrames"] = 0

                        if self.player["spriteState"] == 2: 
                            self.player["spriteState"] += 1
                            self.player["spriteToRight"] = True
                            self.player["spriteToLeft"] = False
                        elif self.player["spriteState"] == 3 and self.player["spriteToLeft"] == True: self.player["spriteState"] -= 1
                        elif self.player["spriteState"] == 3 and self.player["spriteToRight"] == True: self.player["spriteState"] += 1
                        elif self.player["spriteState"] == 4: 
                            self.player["spriteState"] -= 1
                            self.player["spriteToRight"] = False
                            self.player["spriteToLeft"] = True

            else:
                if self.player["spriteMoving"] == True:
                        self.player["spriteMoving"] = False
                        self.player["spriteFrames"] = 0
                        self.player["spriteState"] = 0
                else:
                    self.player["spriteFrames"] += 1
                    if self.player["spriteFrames"] >= math.floor( 8 / SpriteCycle_FrameCapMultiplier ):
                        self.player["spriteFrames"] = 0
                        if self.player["spriteState"] == 0: self.player["spriteState"] = 1
                        else: self.player["spriteState"] = 0

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        def Run_BlitSetup(self):

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            def Run_BlitSetup_RenderLayer(self,l):
                for x in range(self.displayData["width"]+1):
                    for y in range(self.displayData["height"]+1):
                        tile = self.grid[l][x][y]
                        tile = tile.split("_")
                        if tile[0] == "color":
                            pygame.draw.rect(self.surface,self.color[tile[1]],((x*self.displayData["tileSize"])+self.gridData["offsetX"],(y*self.displayData["tileSize"])+self.gridData["offsetY"],self.displayData["tileSize"],self.displayData["tileSize"]),0)
                        elif tile[0] == "tile":
                            self.surface.blit(self.asset["tile"][f"{tile[1]}"],((x*self.displayData["tileSize"])+self.gridData["offsetX"],(y*self.displayData["tileSize"])+self.gridData["offsetY"]))
            
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            def Run_BlitSetup_RenderPlayer(self): self.surface.blit(self.asset["sprite"][self.player["sprite"]+"_"+self.player["spriteDirection"]+"_"+str(self.player["spriteState"])],(((self.player["gridX"])-(math.floor(self.player["spriteWidth"]/2))),(self.player["gridY"]-self.player["spriteHeight"])))

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            Run_BlitSetup_RenderLayer(self,0)
            Run_BlitSetup_RenderLayer(self,1)
            Run_BlitSetup_RenderLayer(self,2)
            Run_BlitSetup_RenderPlayer(self)
            Run_BlitSetup_RenderLayer(self,3)
            Run_BlitSetup_RenderLayer(self,4)

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        if self.init == False:

            #Get Room
            #Get Player Sprite Width & Height
            #Get Player Room Placement
            self.player["room"] = "test0"
            Run_GetSpriteDimensions(self)
            self.player["roomX"] = 126
            self.player["roomY"] = 104
            self.init = True

        else:

            #Check for Player Movement [ And Trigger Tile Events if Nessesary ]
            Run_PlayerEventCheck(self)
            
        #Determine Grid Lock
        #Determine Grid Offset
        #Render Grid from Room
        Run_CheckGridLock(self)
        Run_GetGridOffset(self)
        Run_RenderGridFromRoom(self)

        #Determine Player Placement on Grid
        #Determine Player Sprite Cycle
        #Renders all Elements to the RPG surface, ready for Blitting
        Run_PlayerToGrid(self)
        Run_SpriteCycle(self)
        Run_BlitSetup(self)

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    def Blit(self,surface,x,y,width,height): surface.blit(pygame.transform.scale(self.surface,(width,height)),(x,y))
    
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    def BlitBorder(self,surface,x,y,width,height): surface.blit(pygame.transform.scale(self.asset["border"],(width,height)),(x,y))

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #