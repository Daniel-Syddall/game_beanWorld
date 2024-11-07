from data.RPG.room.Builder import *

def roomVariantsTest(self):

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    roomName = ["red","blue","yellow","orange","purple","green"]
    hueChange = [[50,0,0],[0,0,50],[50,50,0],[50,0,-50],[50,0,50],[0,50,0]]
    beanLine = ["default_I'm gonna beat the shit out of you!_","default_Amogus Balls?_","default_One fart and I'm dead..._","default_THEY HIT THE PENTAGON!!!_","default_Fuck You_","default_Suck my NUTS_"]

    for i in range(6):

        Room_Build(self,roomName[i],17,20,"","")

    for i in range(6):

        #Room_CreateWall(self,roomName[i],5,0,0,16,12,f"pco_shadow","na")
        Room_CreateWall(self,roomName[i],0,0,0,16,19,f"rgba_0_0_0_255","na")
        Room_SetEdge(self,roomName[i],1,1,15,11,"0","0")

        Room_CreateBlock(self,roomName[i],4,2,4,f"tile_decor_tree0","")
        Room_CreateBlock(self,roomName[i],4,8,2,f"tile_decor_tree0","")
        Room_CreateBlock(self,roomName[i],4,14,10,f"tile_decor_tree0","")

        Room_CreateBlock(self,roomName[i],2,1,6,f"tile_ground_0_downLeft+upLeft","na")
        Room_CreateBlock(self,roomName[i],2,0,6,f"tile_ground_0_up+down","na")
        Room_CreateBlock(self,roomName[i],1,0,6,f"tile_edge_0_up+down-0","na")
        Room_CreateBlock(self,roomName[i],1,0,7,f"tile_edge_0_down-1","na")
        if i != 0: Room_CreateSend(self,roomName[i],0,6,roomName[i-1],15,6)
        else: Room_CreateSend(self,roomName[i],0,6,roomName[5],15,6)

        Room_CreateBlock(self,roomName[i],2,15,6,f"tile_ground_0_upRight+downRight","na")
        Room_CreateBlock(self,roomName[i],2,16,6,f"tile_ground_0_up+down","na")
        Room_CreateBlock(self,roomName[i],1,16,6,f"tile_edge_0_up+down-0","na")
        Room_CreateBlock(self,roomName[i],1,16,7,f"tile_edge_0_down-1","na")
        if i != 5: Room_CreateSend(self,roomName[i],16,6,roomName[i+1],1,6)
        else: Room_CreateSend(self,roomName[i],16,6,roomName[0],1,6)

        Room_ChangeState(self,roomName[i],"",0,12,16,19)
        Room_ChangeState(self,roomName[i],"pass",4,12,11,16)
        Room_SetEdge(self,roomName[i],4,12,11,16,"0","0")
        Room_CreateWall(self,roomName[i],2,5,11,10,12,f"tile_ground_0_full","na")
        Room_CreateBlock(self,roomName[i],2,4,12,f"tile_ground_0_left","na")
        Room_CreateBlock(self,roomName[i],2,11,12,f"tile_ground_0_right","na")
        Room_CreateBlock(self,roomName[i],2,4,11,f"tile_ground_0_downLeft","na")
        Room_CreateBlock(self,roomName[i],2,11,11,f"tile_ground_0_downRight","na")
        Room_CreateBlock(self,roomName[i],4,5,14,f"tile_decor_tree0","")
        
        for l in range(6): Room_ChangeLayerHue(self,roomName[i],l,f"{hueChange[i][0]}_{hueChange[i][1]}_{hueChange[i][2]}_0")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    class test0_event_0:
        def __init__(self,Self,roomName,x,y,hue):
            self.rpg = Self
            self.roomName = roomName
            self.hue = hue
            self.x = x
            self.y = y
            self.state = 0
            self.stateFrame = 3
            self.direction = 0
            self.directionArray = ["down","down","right","right","up","up","left","left"]
            Room_CreateBlock(self.rpg,roomName,4,self.x,self.y,f"sprite_default_down_0_{hueChange[self.hue][0]*2}_{hueChange[self.hue][1]*2}_{hueChange[self.hue][2]*2}_0","na")

        def Run(self):
            class test0_event_1_pauseEvent:
                def __init__(self,Self,i):
                    self.rpg = Self
                    self.rpg.textBox = beanLine[i]
                    self.rpg.controller["select"] = False

                def Run(self):
                    if self.rpg.controller["select"] == True:
                        self.rpg.controller["select"] = False
                        self.rpg.textBox = ""
                        self.rpg.pauseEvent = NULL
            self.rpg.pauseEvent = test0_event_1_pauseEvent(self.rpg,self.hue)

        def Check(self):
            if self.rpg.controller["select"] == True and self.rpg.pauseEvent == NULL:
                if self.rpg.player["spriteDirection"] == "up" and math.floor(self.rpg.player["roomX"]/16) == self.x and math.floor(self.rpg.player["roomY"]/16) == self.y+1 or self.rpg.player["spriteDirection"] == "down" and math.floor(self.rpg.player["roomX"]/16) == self.x and math.floor(self.rpg.player["roomY"]/16) == self.y-1 or self.rpg.player["spriteDirection"] == "left" and math.floor(self.rpg.player["roomX"]/16) == self.x+1 and math.floor(self.rpg.player["roomY"]/16) == self.y or self.rpg.player["spriteDirection"] == "right" and math.floor(self.rpg.player["roomX"]/16) == self.x-1 and math.floor(self.rpg.player["roomY"]/16) == self.y:
                    self.Run()

            if self.stateFrame != 0: self.stateFrame -= 1
            if self.stateFrame == 0:
                self.stateFrame = 3
                if self.direction != 7: self.direction += 1
                else: self.direction = 0
                if self.state == 0: self.state = 1
                elif self.state == 1: self.state = 0
                Room_CreateBlock(self.rpg,self.roomName,4,self.x,self.y,"sprite_default_"+self.directionArray[self.direction]+"_"+str(self.state)+"_"+str(hueChange[self.hue][0]*2)+"_"+str(hueChange[self.hue][1]*2)+"_"+str(hueChange[self.hue][2]*2)+"_0","")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # Event 0
    
    for i in range(6):
        Room_CreateEvent(self,roomName[i],test0_event_0(self,roomName[i],14,2,i),"trigger")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #