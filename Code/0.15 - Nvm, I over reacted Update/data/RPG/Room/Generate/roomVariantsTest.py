from data.RPG.Room.Builder import *

def roomVariantsTest(self):

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    roomName = ["red","blue","yellow","orange","purple","green"]
    hueChange = [[50,0,0,0],[0,0,50,0],[50,50,0,0],[50,0,-50,0],[50,0,50],[0,50,0,0]]

    for i in range(6):

        Room_Build(self,roomName[i],17,13,"","")

    for i in range(6):

        Room_CreateWall(self,roomName[i],0,0,0,16,12,f"rgba_0_0_0_255","na")
        Room_SetEdge(self,roomName[i],1,1,15,11,"0","0")

        Room_CreateBlock(self,roomName[i],4,2,4,f"tile_decor_tree0_{hueChange[i][0]}_{hueChange[i][1]}_{hueChange[i][2]}_0","")
        Room_CreateBlock(self,roomName[i],4,8,2,f"tile_decor_tree0_{hueChange[i][0]}_{hueChange[i][1]}_{hueChange[i][2]}_0","")
        Room_CreateBlock(self,roomName[i],4,14,10,f"tile_decor_tree0_{hueChange[i][0]}_{hueChange[i][1]}_{hueChange[i][2]}_0","")

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

        Room_ChangeLayerHue(self,roomName[i],2,f"{hueChange[i][0]}_{hueChange[i][1]}_{hueChange[i][2]}_0")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    class test0_event_0:
        def __init__(self,Self,roomName,x,y):
            self.rpg = Self
            self.roomName = roomName
            self.x = x
            self.y = y
            self.state = 0
            self.stateFrame = 3
            self.direction = 0
            self.directionArray = ["down","down","right","right","up","up","left","left"]
            Room_CreateBlock(self.rpg,roomName,4,self.x,self.y,"sprite_default_down_0","na")

        def Run(self):
            class test0_event_1_pauseEvent:
                def __init__(self,Self):
                    self.rpg = Self
                    self.rpg.textBox = "Nuts"
                    self.rpg.controller["select"] = False

                def Run(self):
                    if self.rpg.controller["select"] == True:
                        self.rpg.controller["select"] = False
                        self.rpg.textBox = ""
                        self.rpg.pauseEvent = NULL
            self.rpg.pauseEvent = test0_event_1_pauseEvent(self.rpg)

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
                Room_CreateBlock(self.rpg,self.roomName,4,self.x,self.y,"sprite_default_"+self.directionArray[self.direction]+"_"+str(self.state),"")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # Event 0
    
    for i in range(6):
        Room_CreateEvent(self,roomName[i],test0_event_0(self,roomName[i],14,2),"trigger")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #