from data.RPG.room.Builder import *
from random import randint as random

def roomVariantsTest(self):

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    roomName = ["red","blue","yellow","orange","purple","green",""]
    hueChange = [[50,0,0],[0,0,50],[50,50,0],[50,0,-50],[50,0,50],[0,50,0],[-35,-35,-35]]
    beanLine = ["default_I'm gonna beat the BEAN out of you!_","default_Amogus Beans?_","default_One bean and I'm dead..._","default_THEY HIT THE BIG TIN!!!_","default_Bean You_","default_Suck my BEANS_","default_Too many Shats.._"]
    shadowRoom = []

    for i in range(6):

        Room_Build(self,roomName[i],17,20,"","")
        shadowRoom.append(random(0,11))

    for i in range(6):

        Room_CreateWall(self,roomName[i],5,0,0,16,12,f"overlay_hue_0_0_0_-100","na")
        Room_CreateWall(self,roomName[i],0,0,0,16,19,f"rgba_0_0_0_255","na")
        Room_SetEdge(self,roomName[i],1,1,15,11,"0","0")

        Room_CreateBlock(self,roomName[i],4,2,4,f"tile_decor_tree0","")
        Room_CreateBlock(self,roomName[i],3,2,4,f"shadow_default2_7_10","na")
        Room_CreateBlock(self,roomName[i],4,8,2,f"tile_decor_tree0","")
        Room_CreateBlock(self,roomName[i],3,8,2,f"shadow_default2_7_10","na")
        Room_CreateBlock(self,roomName[i],4,14,10,f"tile_decor_tree0","")
        Room_CreateBlock(self,roomName[i],3,14,10,f"shadow_default2_7_10","na")

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
        Room_CreateBlock(self,roomName[i],3,5,14,f"shadow_default2_7_10","na")
        
        if shadowRoom[i] == 0:
            Room_ChangeState(self,roomName[i],"pass",9,16,10,19)
            Room_SetEdge(self,roomName[i],9,16,10,19,"0","0")
            Room_CreateBlock(self,roomName[i],2,9,16,f"tile_ground_0_full","na")
            Room_CreateBlock(self,roomName[i],2,10,16,f"tile_ground_0_full","na")
            Room_CreateBlock(self,roomName[i],1,9,16,f"tile_edge_0_right","na")
            Room_CreateBlock(self,roomName[i],1,10,16,f"tile_edge_0_left","na")
            Room_CreateBlock(self,roomName[i],2,9,19,f"tile_ground_0_Left","na")
            Room_CreateBlock(self,roomName[i],2,10,19,f"tile_ground_0_Right","na")
            Room_CreateBlock(self,roomName[i],1,9,19,f"tile_edge_0_Left","na")
            Room_CreateBlock(self,roomName[i],1,10,19,f"tile_edge_0_Right","na")
            Room_CreateSend(self,roomName[i],9,19,roomName[i]+"_shadow",4,4)
            Room_CreateSend(self,roomName[i],10,19,roomName[i]+"_shadow",4,4)

        for l in range(6): 
            Room_ChangeHue(self,roomName[i],l,f"{hueChange[i][0]}_{hueChange[i][1]}_{hueChange[i][2]}_0",0,0,16,19)
            if shadowRoom[l] == 0:
                Room_ChangeHue(self,roomName[i],2,f"-3_-3_-3_0",9,17,10,17)
                Room_ChangeHue(self,roomName[i],2,f"-6_-6_-6_0",9,18,10,18)
                Room_ChangeHue(self,roomName[i],2,f"-9_-9_-9_0",9,19,10,19)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    for i in range(6):
        if shadowRoom[i] == 0:
            Room_Build(self,roomName[i]+"_shadow",17,13,"","")

            Room_CreateWall(self,roomName[i]+"_shadow",5,0,0,16,12,f"pco_shadow_0_0_0_-50","na")
            Room_CreateWall(self,roomName[i]+"_shadow",0,0,0,16,12,f"rgba_0_0_0_255","na")

            Room_ChangeState(self,roomName[i]+"_shadow","",0,0,16,12)
            Room_ChangeState(self,roomName[i]+"_shadow","pass",3,2,13,10)
            Room_SetEdge(self,roomName[i]+"_shadow",3,2,13,10,"0","0")

            Room_ChangeHue(self,roomName[i]+"_shadow",1,f"-50_-50_-50_5",0,0,16,12)
            Room_ChangeHue(self,roomName[i]+"_shadow",2,f"-50_-50_-50_5",0,0,16,12)

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
            Room_CreateBlock(self.rpg,roomName,4,self.x,self.y,f"sprite_default_down_0_{hueChange[self.hue][0]*2}_{hueChange[self.hue][1]*2}_{hueChange[self.hue][2]*2}_0","")
            Room_CreateBlock(self.rpg,roomName,3,self.x,self.y,"shadow_default1_2_9","na")

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
                Room_CreateBlock(self.rpg,self.roomName,3,self.x,self.y,f"shadow_default{str(self.state)}_2_9","na")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    class test0_event_1:
        def __init__(self,Self,roomName,x,y,hue):
            self.rpg = Self
            self.roomName = roomName
            self.hue = hue
            self.x = x
            self.y = y
            self.state = 0
            self.stateFrame = 60
            self.direction = 0
            self.directionArray = ["right"]
            Room_CreateBlock(self.rpg,roomName,4,self.x,self.y,f"sprite_default_right_0_{hueChange[self.hue][0]*2}_{hueChange[self.hue][1]*2}_{hueChange[self.hue][2]*2}_0","")
            Room_CreateBlock(self.rpg,roomName,3,self.x,self.y,"shadow_default1_2_9","na")

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
                self.stateFrame = 40
                if self.state == 0: self.state = 1
                elif self.state == 1: self.state = 0
                Room_CreateBlock(self.rpg,self.roomName,4,self.x,self.y,"sprite_default_"+self.directionArray[self.direction]+"_"+str(self.state)+"_"+str(hueChange[self.hue][0]*2)+"_"+str(hueChange[self.hue][1]*2)+"_"+str(hueChange[self.hue][2]*2)+"_0","")
                Room_CreateBlock(self.rpg,self.roomName,3,self.x,self.y,f"shadow_default{str(self.state)}_2_9","na")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # Event 0
    
    for i in range(6):
        Room_CreateEvent(self,roomName[i],test0_event_0(self,roomName[i],14,2,i),"trigger")
        if shadowRoom[i] == 0: Room_CreateEvent(self,roomName[i]+"_shadow",test0_event_1(self,roomName[i]+"_shadow",12,9,6),"trigger")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #