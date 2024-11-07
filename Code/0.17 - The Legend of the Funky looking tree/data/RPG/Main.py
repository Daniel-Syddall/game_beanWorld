import pygame
import math
from tkinter import Grid
from random import randint as random
from asyncio.windows_events import NULL

class RPG:
    def __init__(self):
        
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Local of RPG File #

        self.local = "./data/RPG/"

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Screen Creation #

        self.init = False
        self.displayData = {"tileSize" : 16,"width" : 17,"height" : 13}
        self.surface = pygame.Surface((self.displayData["width"]*self.displayData["tileSize"],self.displayData["height"]*self.displayData["tileSize"]))
        self.surface_base = pygame.Surface((self.displayData["width"]*self.displayData["tileSize"],self.displayData["height"]*self.displayData["tileSize"]))

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Other random shit #

        self.pauseEvent = NULL
        self.textBox = ""
        self.gridData = {"room" : "red","lockXL" : False,"lockXR" : False,"lockYL" : False,"lockYR" : False,"offsetX" : 0,"offsetY" : 0,
        "startX":0,"startY":0}
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
        groundTileNamesArray = ["0"]
        edgeTileNamesArray = ["0"]
        decorTileNamesArray = ["tree0"]
        self.decorTileDimentionsArray = {"tree0":[2,3]}
        pcoNamesArray = ["shadow"]

        
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #


        # Type Render #

        typeArray = {
            "a" : {"yOffset":0}, "A" : {"yOffset":0},
            "b" : {"yOffset":0}, "B" : {"yOffset":0},
            "c" : {"yOffset":0}, "C" : {"yOffset":0},
            "d" : {"yOffset":0}, "D" : {"yOffset":0},
            "e" : {"yOffset":0}, "E" : {"yOffset":0},
            "f" : {"yOffset":0}, "F" : {"yOffset":0},
            "g" : {"yOffset":4}, "G" : {"yOffset":0},
            "h" : {"yOffset":0}, "H" : {"yOffset":0},
            "i" : {"yOffset":0}, "I" : {"yOffset":0},
            "j" : {"yOffset":5}, "J" : {"yOffset":0},
            "k" : {"yOffset":0}, "K" : {"yOffset":0},
            "l" : {"yOffset":0}, "L" : {"yOffset":0},
            "m" : {"yOffset":0}, "M" : {"yOffset":0},
            "n" : {"yOffset":0}, "N" : {"yOffset":0},
            "o" : {"yOffset":0}, "O" : {"yOffset":0},
            "p" : {"yOffset":5}, "P" : {"yOffset":0},
            "q" : {"yOffset":4}, "Q" : {"yOffset":3},
            "r" : {"yOffset":0}, "R" : {"yOffset":0},
            "s" : {"yOffset":0}, "S" : {"yOffset":0},
            "t" : {"yOffset":0}, "T" : {"yOffset":0},
            "u" : {"yOffset":0}, "U" : {"yOffset":0},
            "v" : {"yOffset":0}, "V" : {"yOffset":0},
            "w" : {"yOffset":0}, "W" : {"yOffset":0},
            "x" : {"yOffset":0}, "X" : {"yOffset":0},
            "y" : {"yOffset":5}, "Y" : {"yOffset":0},
            "z" : {"yOffset":0}, "Z" : {"yOffset":0},
            "," : {"yOffset":0}, "." : {"yOffset":0}
        } # Custom Y Value #


# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Asset Imports #

        SpriteDirectionsArray = ["up","down","left","right"]
        groundTileTypeArray = ["full","left","up","down","right",
        "left+up","up+right","right+down","down+left","left+right","up+down","left+up+right","up+right+down","left+right+down","left+up+down","left+up+right+down",
        "upLeft","upRight","downRight","downLeft","upLeft+upRight","upRight+downRight","downRight+downLeft","downLeft+upLeft","upLeft+downRight","upRight+downLeft",
        "upLeft+upRight+downRight","upRight+downRight+downLeft","downRight+downLeft+upLeft","upLeft+upRight+downLeft","upLeft+upRight+downRight+downLeft",
        "left+upRight","left+downRight","left+upRight+downRight","up+downRight","up+downLeft","up+downRight+downLeft","right+downLeft","right+upLeft","right+downLeft+upLeft",
        "down+upLeft","down+upRight","down+upLeft+upRight"]
        edgeTileTypeArray = ["left","up","right","down-0","down-1","left+up","up+right","right+down-0","right+down-1","down-0+left","down-1+left","left+right","up+down-0",
        "upLeft","upRight","downLeft","downRight"]
        typeLowerArray = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        typeUpperArray = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","w","X","Y","Z"]
        typeCustomArray = [",",".","?","!","*"]

        self.asset = {"sprite":{},"tile":{},"decor":{},"pco":{},"border":pygame.image.load(f"{self.local}/assets/border.png")}

        for s in range(len(spriteNamesArray)):
            for d in range(len(SpriteDirectionsArray)):
                for i in range(5): self.asset["sprite"][f"{spriteNamesArray[s]}_{SpriteDirectionsArray[d]}_{str(i)}"] = pygame.image.load(f"{self.local}/assets/sprites/{spriteNamesArray[s]}_{SpriteDirectionsArray[d]}_{str(i)}.png")

        for g in range(len(groundTileNamesArray)):
            for t in range(len(groundTileTypeArray)):
                self.asset["tile"][f"ground_{groundTileNamesArray[g]}_{groundTileTypeArray[t]}"] = pygame.image.load(f"{self.local}/assets/tiles/ground/ground_{groundTileNamesArray[g]}_{groundTileTypeArray[t]}.png")

        for e in range(len(edgeTileNamesArray)):
            for t in range(len(edgeTileTypeArray)):
                self.asset["tile"][f"edge_{edgeTileNamesArray[e]}_{edgeTileTypeArray[t]}"] = pygame.image.load(f"{self.local}/assets/tiles/edge/edge_{edgeTileNamesArray[e]}_{edgeTileTypeArray[t]}.png")

        for d in range(len(decorTileNamesArray)): self.asset["tile"][f"decor_{decorTileNamesArray[d]}"] = pygame.image.load(f"{self.local}/assets/tiles/decor/{decorTileNamesArray[d]}.png")
        for p in range(len(pcoNamesArray)): self.asset["pco"][f"{pcoNamesArray[p]}"] = pygame.image.load(f"{self.local}/assets/pcos/{pcoNamesArray[p]}.png")

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Grid #

        self.grid = []
        for l in range(6):
            self.grid.append([])
            for x in range(self.displayData["width"]+1):
                self.grid[l].append([])
                for _ in range(self.displayData["height"]+1):
                    self.grid[l][x].append("")

        self.customTiles = []

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        # Room #

        from data.RPG.room.Room import Room
        Room(self)

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    def Controller(self,event,type):

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z: self.controller["select"] = False
            if event.key == pygame.K_w or event.key == pygame.K_UP: self.controller["up"] = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN: self.controller["down"] = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT: self.controller["left"] = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT: self.controller["right"] = False
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: self.controller["sprint"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z: self.controller["select"] = True
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
                    sendID = -1
                    while True:
                        sendID += 1
                        if math.floor(x/16) == self.room[self.gridData["room"]]["send_"+str(sendID)+"_x"] and math.floor(y/16) == self.room[self.gridData["room"]]["send_"+str(sendID)+"_y"]: break

                    self.gridData["room"] = self.room[self.gridData["room"]]["spawn_"+str(sendID)+"_room"]
                    self.player["roomX"] = (self.room[self.gridData["room"]]["spawn_"+str(sendID)+"_x"]*16)+9
                    self.player["roomY"] = (self.room[self.gridData["room"]]["spawn_"+str(sendID)+"_y"]*16)+9

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

            self.gridData["startX"] = StartX
            self.gridData["startY"] = StartY

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

            def Run_BlitSetup_IdentifyCustomTiles(self):
                self.customTiles = []
                for l in range(3):
                    L = l + 3
                    self.customTiles.append([])
                    for y in range((self.room[self.gridData["room"]]["maxY"] - self.gridData["startY"]) + 1):
                        Y = y + self.gridData["startY"]
                        self.customTiles[l].append([])
                        temp_customCount = 0
                        for x in range(self.room[self.gridData["room"]]["maxX"]):
                            if self.room[self.gridData["room"]][f"{str(L)}_{str(x)}_{str(Y)}"] != "":
                                tile = self.room[self.gridData["room"]][f"{str(L)}_{str(x)}_{str(Y)}"]
                                tile = tile.split("_")
                                if tile[0] == "sprite" or tile[1] == "decor":
                                     self.customTiles[l][y].append([])
                                     self.customTiles[l][y][temp_customCount].append(self.room[self.gridData["room"]][f"{str(L)}_{str(x)}_{str(Y)}"])
                                     self.customTiles[l][y][temp_customCount].append(str(x))
                                     temp_customCount += 1

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            def Run_BlitSetup_ChangeHue(surface,hue,TransparentBG):
                hue = hue.split("_")
                temp_area = pygame.PixelArray(surface)
                for X in range(surface.get_width()):
                    for Y in range(surface.get_height()):
                        temp_rgb = surface.unmap_rgb(temp_area[X][Y])
                        temp_color = pygame.Color(*temp_rgb)
                        R,G,B,A = temp_color
                        if TransparentBG == False or A != 0:
                            temp_rgba = []
                            temp_rgba.append(int(R)+int(hue[0]))
                            temp_rgba.append(int(G)+int(hue[1]))
                            temp_rgba.append(int(B)+int(hue[2]))
                            temp_rgba.append(int(A)+int(hue[3]))
                            for i in range(4):
                                if temp_rgba[i] > 255: temp_rgba[i] = 255
                                elif temp_rgba[i] <= 0: temp_rgba[i] = 0
                            temp_color = temp_rgba[0], temp_rgba[1], temp_rgba[2], temp_rgba[3]
                        else: temp_color = R , G , B , A
                        temp_area[X][Y] = temp_color
                del temp_area

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            def Run_BlitSetup_NewTile(self,tile,title):
                if tile[1] == "decor": 
                    self.asset[tile[0]][title] =  pygame.image.load(f"{self.local}/assets/{tile[0]}s/{tile[1]}/{tile[2]}.png")
                    Run_BlitSetup_ChangeHue(self.asset[tile[0]][title],f"{tile[3]}_{tile[4]}_{tile[5]}_{tile[6]}",True)
                elif tile [0] == "sprite":
                    self.asset[tile[0]][title] =  pygame.image.load(f"{self.local}/assets/{tile[0]}s/{tile[1]}_{tile[2]}_{tile[3]}.png")
                    Run_BlitSetup_ChangeHue(self.asset[tile[0]][title],f"{tile[4]}_{tile[5]}_{tile[6]}_{tile[7]}",True)
                elif tile [0] != "pco": 
                    self.asset[tile[0]][title] =  pygame.image.load(f"{self.local}/assets/{tile[0]}s/{tile[1]}/{tile[1]}_{tile[2]}_{tile[3]}.png")
                    Run_BlitSetup_ChangeHue(self.asset[tile[0]][title],f"{tile[4]}_{tile[5]}_{tile[6]}_{tile[7]}",True)
                else: 
                    self.asset[tile[0]][title] =  pygame.image.load(f"{self.local}/assets/{tile[0]}s/{tile[1]}.png")
                    Run_BlitSetup_ChangeHue(self.asset[tile[0]][title],f"{tile[2]}_{tile[3]}_{tile[4]}_{tile[5]}",True)

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            def Run_BlitSetup_RenderLayer(self,surface,l,Player):
                pco_check = False
                for y in range(self.displayData["height"]+1):
                    if Player == True and math.floor(self.player["gridY"]/16) == y: surface.blit(self.asset["sprite"][self.player["sprite"]+"_"+self.player["spriteDirection"]+"_"+str(self.player["spriteState"])],(((self.player["gridX"])-(math.floor(self.player["spriteWidth"]/2))),(self.player["gridY"]-self.player["spriteHeight"])))
                    for x in range(self.displayData["width"]+1):
                        tile = self.grid[l][x][y]
                        if tile != "":
                            tile = tile.split("_")
                            if tile[0] == "rgba": 
                                temp_rgba = pygame.Surface((self.displayData["tileSize"],self.displayData["tileSize"]))
                                temp_rgba.set_alpha(int(tile[4]))
                                temp_rgba.fill((int(tile[1]),int(tile[2]),int(tile[3])))
                                surface.blit(temp_rgba,((x*self.displayData["tileSize"])+self.gridData["offsetX"],(y*self.displayData["tileSize"])+self.gridData["offsetY"]))
                            else: 
                                temp_title = ""
                                for i in range(len(tile)-1): temp_title += tile[i+1] + "_"
                                temp_title = temp_title[:-1]
                                if self.asset[tile[0]].get(temp_title) == None: Run_BlitSetup_NewTile(self,tile,temp_title)
                                if tile [0] == "tile" and tile [1] != "decor": surface.blit(self.asset[tile[0]][temp_title],((x*self.displayData["tileSize"])+self.gridData["offsetX"],(y*self.displayData["tileSize"])+self.gridData["offsetY"]))
                                elif tile [0] == "pco":
                                    if pco_check != True: 
                                        self.surface.blit(self.asset[tile[0]][temp_title],(self.player["gridX"]-math.floor((self.asset[tile[0]][temp_title].get_width())/2),(self.player["gridY"]-(math.floor((self.asset["sprite"][self.player["sprite"]+"_"+self.player["spriteDirection"]+"_"+str(self.player["spriteState"])].get_height())/2)))-math.floor((self.asset[tile[0]][temp_title].get_height())/2)))
                                    pco_check = True

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

                    if l >= 3:
                        temp_l = l - 3
                        temp_y = y
                        for i in range(len(self.customTiles[temp_l][temp_y])):
                            tile = self.customTiles[temp_l][temp_y][i][0]
                            x = int(self.customTiles[temp_l][temp_y][i][1])-self.gridData["startX"]
                            tile = tile.split("_")
                            temp_title = ""
                            for t in range(len(tile)-1): temp_title += tile[t+1] + "_"
                            temp_title = temp_title[:-1]
                            if tile[1] == "decor": surface.blit(self.asset[tile[0]][temp_title],((x*self.displayData["tileSize"])+self.gridData["offsetX"]-math.floor((self.decorTileDimentionsArray[tile[2]][0]-1)*(self.displayData["tileSize"]/2)),(y*self.displayData["tileSize"])+self.gridData["offsetY"]-math.floor((self.decorTileDimentionsArray[tile[2]][1]-1)*(self.displayData["tileSize"]))))
                            elif tile [0] == "sprite": self.surface.blit(self.asset[tile[0]][temp_title],((math.floor(((x*self.displayData["tileSize"])+8)-(self.asset[tile[0]][temp_title].get_width()/2))+self.gridData["offsetX"]),(((y*self.displayData["tileSize"])+12)-self.asset[tile[0]][temp_title].get_height())+self.gridData["offsetY"]))

                if l >= 3:
                    for y in range(self.room[self.gridData["room"]]["maxY"]-(self.gridData["startY"]+13)):
                        temp_l = l - 3
                        temp_y = y + 13
                        for i in range(len(self.customTiles[temp_l][temp_y])):
                            tile = self.customTiles[temp_l][temp_y][i][0]
                            x = int(self.customTiles[temp_l][temp_y][i][1])-self.gridData["startX"]
                            tile = tile.split("_")
                            temp_title = ""
                            for t in range(len(tile)-1): temp_title += tile[t+1] + "_"
                            temp_title = temp_title[:-1]
                            if tile[1] == "decor": surface.blit(self.asset[tile[0]][temp_title],((x*self.displayData["tileSize"])+self.gridData["offsetX"]-math.floor((self.decorTileDimentionsArray[tile[2]][0]-1)*(self.displayData["tileSize"]/2)),(temp_y*self.displayData["tileSize"])+self.gridData["offsetY"]-math.floor((self.decorTileDimentionsArray[tile[2]][1]-1)*(self.displayData["tileSize"]))))
                            elif tile [0] == "sprite": self.surface.blit(self.asset[tile[0]][temp_title],((math.floor(((x*self.displayData["tileSize"])+8)-(self.asset[tile[0]][temp_title].get_width()/2))+self.gridData["offsetX"]),(((temp_y*self.displayData["tileSize"])+12)-self.asset[tile[0]][temp_title].get_height())+self.gridData["offsetY"]))

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

            Run_BlitSetup_IdentifyCustomTiles(self)
            Run_BlitSetup_RenderLayer(self,self.surface,0,False)
            Run_BlitSetup_RenderLayer(self,self.surface,1,False)
            Run_BlitSetup_RenderLayer(self,self.surface,2,False)
            Run_BlitSetup_RenderLayer(self,self.surface,3,False)
            Run_BlitSetup_RenderLayer(self,self.surface,4,True)
            Run_BlitSetup_RenderLayer(self,self.surface,5,False)

# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

        if self.init == False:

            #Get Room
            #Get Player Sprite Width & Height
            #Get Player Room Placement
            self.player["room"] = "red"
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