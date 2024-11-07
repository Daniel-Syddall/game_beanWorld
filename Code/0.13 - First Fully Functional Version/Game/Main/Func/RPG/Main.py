from cmath import rect
from tkinter import Grid
import pygame
import math
from random import randint as random
from asyncio.windows_events import NULL
from Data.Const import window

class RPG:
    def __init__(self):
        
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Local of RPG File #

        self.local = "./Game/Main/Func/RPG/"

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Screen Creation #

        self.init = False
        self.displayData = {"tileSize" : 16,"width" : 17,"height" : 13}
        self.surface = pygame.Surface((self.displayData["width"]*self.displayData["tileSize"],self.displayData["height"]*self.displayData["tileSize"]))

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Other random shit #

        self.pauseEvent = NULL
        self.textBox = ""
        self.gridData = {"room" : "test0","lockXL" : False,"lockXR" : False,"lockYL" : False,"lockYR" : False,"offsetX" : 0,"offsetY" : 0}
        self.player = {"sprite" : "default","spriteWidth" : 0,"spriteHeight" : 0,"spriteColorWidth" : 16,"spriteColorHeight" : 22,
        "spriteState" : 0,"spriteFrames" : 0,"spriteDirection" : "down","spriteMoving" : False, "spriteToLeft" : False,"spriteToRight" : False,
        "roomX" : 0,"roomY" : 0,"gridX" : 0,"gridY" : 0,"hitboxSize" : 1,"movementSpeed" : 1}
        self.controller = {"select" : False, "up" : False, "down" : False,"left" : False,"right" : False,"sprint" : False}
        self.OffsetArray = [-8,-9,-10,-11,-12,-13,-14,-15,-16,-1,-2,-3,-4,-5,-6,-7]

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #


        # Colors #

        self.color = {"empty" : (0,0,0,0), "black" : (0,0,0),"white" : (255,255,255),"orange" : (250,130,10),"brown" : (84,47,20),"grey" : (122,122,122),
        "saturatedBrown" : (110,40,0)}


# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #


        # Asset Names #

        spriteNamesArray = ["default"]
        groundTileNamesArray = ["0","1","2","3"]
        edgeTileNamesArray = ["0"]
        
        tileNamesArray = ["louis-0-0","louis-1-0","louis-0-1","louis-1-1",
        "wigi-0-0","wigi-1-0","wigi-0-1","wigi-1-1","wigi-0-2","wigi-1-2"]
        pcoNamesArray = ["shadow"]

        
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #


        # Type Render #

        typeArray = {"pixelSans" : {
            "" : 0,
            "a" : 0,
            "b" : 0,
            "c" : 0,
            "d" : 0,
            "e" : 0,
            "f" : 0,
            "g" : 4,
            "h" : 0,
            "i" : 0,
            "j" : 5,
            "k" : 0,
            "l" : 0,
            "m" : 0,
            "n" : 0,
            "o" : 0,
            "p" : 5,
            "q" : 4,
            "r" : 0,
            "s" : 0,
            "t" : 0,
            "u" : 0,
            "v" : 0,
            "w" : 0,
            "x" : 0,
            "y" : 5,
            "z" : 0
        }} # Custom Y Value #


# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Asset Imports #

        SpriteDirectionsArray = ["up","down","left","right"]
        self.groundTileTypeArray = ["full","left","up","down","right",
        "left+up","up+right","right+down","down+left","left+right","up+down","left+up+right","up+right+down","left+right+down","left+up+down","left+up+right+down",
        "upLeft","upRight","downRight","downLeft","upLeft+upRight","upRight+downRight","downRight+downLeft","downLeft+upLeft","upLeft+downRight","upRight+downLeft",
        "upLeft+upRight+downRight","upRight+downRight+downLeft","downRight+downLeft+upLeft","upLeft+upRight+downLeft","upLeft+upRight+downRight+downLeft",
        "left+upRight","left+downRight","left+upRight+downRight","up+downRight","up+downLeft","up+downRight+downLeft","right+downLeft","right+upLeft","right+downLeft+upLeft",
        "down+upLeft","down+upRight","down+upLeft+upRight"]
        self.edgeTileTypeArray = ["left","up","right","down-0","down-1","left+up","up+right","right+down-0","right+down-1","down-0+left","down-1+left","left+right","up+down-0"]
        typeTypeArray = ["[]","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        self.asset = {"sprite":{},"tile":{},"pco":{},"border":pygame.image.load(f"{self.local}/Assets/border.png")}

        for s in range(len(spriteNamesArray)):
            for d in range(len(SpriteDirectionsArray)):
                for i in range(5): self.asset["sprite"][f"{spriteNamesArray[s]}_{SpriteDirectionsArray[d]}_{str(i)}"] = pygame.image.load(f"{self.local}/Assets/Sprites/{spriteNamesArray[s]}_{SpriteDirectionsArray[d]}_{str(i)}.png")

        for g in range(len(groundTileNamesArray)):
            for t in range(len(self.groundTileTypeArray)):
                self.asset["tile"][f"ground_{groundTileNamesArray[g]}_{self.groundTileTypeArray[t]}"] = pygame.image.load(f"{self.local}/Assets/Tiles/Ground/ground_{groundTileNamesArray[g]}_{self.groundTileTypeArray[t]}.png")

        for e in range(len(edgeTileNamesArray)):
            for t in range(len(self.edgeTileTypeArray)):
                self.asset["tile"][f"edge_{edgeTileNamesArray[e]}_{self.edgeTileTypeArray[t]}"] = pygame.image.load(f"{self.local}/Assets/Tiles/Edge/edge_{edgeTileNamesArray[e]}_{self.edgeTileTypeArray[t]}.png")

        for i in range(len(tileNamesArray)): self.asset["tile"][f"{tileNamesArray[i]}"] = pygame.image.load(f"{self.local}/Assets/Tiles/{tileNamesArray[i]}.png")
        for i in range(len(pcoNamesArray)): self.asset["pco"][f"{pcoNamesArray[i]}"] = pygame.image.load(f"{self.local}/Assets/Pcos/{pcoNamesArray[i]}.png")

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Grid #

        self.grid = []
        for l in range(6):
            self.grid.append([])
            for x in range(self.displayData["width"]+1):
                self.grid[l].append([])
                for _ in range(self.displayData["height"]+1):
                    self.grid[l][x].append("")

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Room #

        from Game.Main.Func.RPG.Room.Room import Room
        Room(self)

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    def Controller(self,event,type):

        if type == "z": self.controller["select"] = True
        else: self.controller["select"] = False

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

        def Run_EventHandler(self):

            for i in range(self.room[self.gridData["room"]]["eventCount"]):

                if self.room[self.gridData["room"]][f"event_{str(i)}_triggerType"] == "passive":
                    self.room[self.gridData["room"]][f"event_{str(i)}"].Run()
                elif self.room[self.gridData["room"]][f"event_{str(i)}_triggerType"] == "trigger":
                    self.room[self.gridData["room"]][f"event_{str(i)}"].Check()

            if self.pauseEvent != NULL: self.pauseEvent.Run()

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        def Run_PlayerEventCheck(self):

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            def Run_PlayerEventCheck_TileEvent(self,x,y,direction):

                if self.room[self.gridData["room"]]["state_"+str(math.floor(x/16))+"_"+str(math.floor((y/16)))] == "pass":
                    temp_colision = False

                    if direction == "up" or direction == "down":
                        for i in range((self.player["spriteWidth"] + ( self.player["hitboxSize"] * 2 ))): 
                            if self.room[self.gridData["room"]]["state_"+str(math.floor(( ( math.floor( x - ( self.player["spriteWidth"] / 2 ) ) ) + i )/16))+"_"+str(math.floor((y/16)))] == "": temp_colision = True

                    elif direction == "left" or direction == "right":
                        for i in range((self.player["hitboxSize"]*2)+1):
                            if self.room[self.gridData["room"]]["state_"+str(math.floor(x/16))+"_"+str(math.floor(((  ( y - ( self.player["hitboxSize"] ) ) + i ) /16)))] == "": temp_colision = True

                    if temp_colision != True:

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

            for l in range(6):
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
            temp_cycle = False
            if self.controller["sprint"] == True and self.pauseEvent == NULL: SpriteCycle_FrameCapMultiplier = 2
            else: SpriteCycle_FrameCapMultiplier = 1

            if self.controller["up"] == True or self.controller["down"] == True or self.controller["left"] == True or self.controller["right"] == True:
                if self.pauseEvent == NULL:
                    temp_cycle = True
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

            if temp_cycle == False:
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

            def Run_BlitSetup_RenderLayer(self,l,Player):
                pco_check = False
                for y in range(self.displayData["height"]+1):
                    if Player == True and math.floor(self.player["roomY"]/16) == y: self.surface.blit(self.asset["sprite"][self.player["sprite"]+"_"+self.player["spriteDirection"]+"_"+str(self.player["spriteState"])],(((self.player["gridX"])-(math.floor(self.player["spriteWidth"]/2))),(self.player["gridY"]-self.player["spriteHeight"])))
                    for x in range(self.displayData["width"]+1):
                        tile = self.grid[l][x][y]
                        tile = tile.split("_")
                        if tile[0] == "color": 
                            if tile[1] == "rgba": 
                                temp_rgba = pygame.Surface((self.displayData["tileSize"],self.displayData["tileSize"]))
                                temp_rgba.set_alpha(int(tile[5]))
                                temp_rgba.fill((int(tile[2]),int(tile[3]),int(tile[4])))
                                self.surface.blit(temp_rgba,((x*self.displayData["tileSize"])+self.gridData["offsetX"],(y*self.displayData["tileSize"])+self.gridData["offsetY"]))
                            else: pygame.draw.rect(self.surface,self.color[tile[1]],((x*self.displayData["tileSize"])+self.gridData["offsetX"],(y*self.displayData["tileSize"])+self.gridData["offsetY"],self.displayData["tileSize"],self.displayData["tileSize"]),0)
                        elif tile[0] == "tile":
                            if tile[1] == "ground":
                                self.surface.blit(self.asset["tile"][f"ground_{tile[2]}_{tile[3]}"],((x*self.displayData["tileSize"])+self.gridData["offsetX"],(y*self.displayData["tileSize"])+self.gridData["offsetY"]))
                            elif tile[1] == "edge": self.surface.blit(self.asset["tile"][f"edge_{tile[2]}_{tile[3]}"],((x*self.displayData["tileSize"])+self.gridData["offsetX"],(y*self.displayData["tileSize"])+self.gridData["offsetY"]))
                            else: self.surface.blit(self.asset["tile"][f"{tile[1]}"],((x*self.displayData["tileSize"])+self.gridData["offsetX"],(y*self.displayData["tileSize"])+self.gridData["offsetY"]))
                            #https://stackoverflow.com/questions/30826897/pygame-changing-hue-of-image
                            #0=Tile_1=Ground_2=ID_3=Varient_4=R_5=G_6=B
                        elif tile[0] == "sprite": self.surface.blit(self.asset["sprite"][tile[1]+"_"+tile[2]+"_"+tile[3]],(math.floor(((x*self.displayData["tileSize"])+8)-(self.asset["sprite"][tile[1]+"_"+tile[2]+"_"+tile[3]].get_width()/2)),((y*self.displayData["tileSize"])+12)-self.asset["sprite"][tile[1]+"_"+tile[2]+"_"+tile[3]].get_height()))
                        elif tile[0] == "pco":
                            if pco_check != True: 
                                self.surface.blit(self.asset["pco"][tile[1]],(self.player["gridX"]-math.floor((self.asset["pco"][tile[1]].get_width())/2),(self.player["gridY"]-(math.floor((self.asset["sprite"][self.player["sprite"]+"_"+self.player["spriteDirection"]+"_"+str(self.player["spriteState"])].get_height())/2)))-math.floor((self.asset["pco"][tile[1]].get_height())/2)))
                                pco_check = True

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            Run_BlitSetup_RenderLayer(self,0,False)
            Run_BlitSetup_RenderLayer(self,1,False)
            Run_BlitSetup_RenderLayer(self,2,False)
            Run_BlitSetup_RenderLayer(self,3,False)
            Run_BlitSetup_RenderLayer(self,4,True)
            Run_BlitSetup_RenderLayer(self,5,False)

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

                #Checks and Runs any Player Events
                Run_EventHandler(self)

                    #Check for Player Movement [ And Trigger Tile Events if Nessesary ]
                if self.pauseEvent == NULL: Run_PlayerEventCheck(self)
                
        #Determine Grid Lock
        Run_CheckGridLock(self)

        #Determine Grid Offset
        Run_GetGridOffset(self)

        #Render Grid from Room
        Run_RenderGridFromRoom(self)

        #Determine Player Placement on Grid
        Run_PlayerToGrid(self)

        #Determine Player Sprite Cycle
        Run_SpriteCycle(self)

        #Renders all Elements to the RPG surface, ready for Blitting
        Run_BlitSetup(self)

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    def Blit(self,surface,x,y,width,height): 
        surface.blit(pygame.transform.scale(self.surface,(width,height)),(x,y))
        return x,y,pygame.transform.scale(self.surface,(width,height)).get_width(),pygame.transform.scale(self.surface,(width,height)).get_height()
    
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    def BlitBorder(self,surface,x,y,width,height): 
        surface.blit(pygame.transform.scale(self.asset["border"],(width,height)),(x,y))

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #