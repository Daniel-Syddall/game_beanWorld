from Game.Main.Func.RPG.Room.Builder import *

def test0(self):

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    Room_Build(self,"test0",17,13,"","")
    Room_SetEdge(self,"test0",1,1,15,11,"0","0")

# Teleport Room 0 to Room 1 - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    Room_CreateBlock(self,"test0",2,15,10,"tile_ground_0_upRight+downRight","na")
    Room_CreateSend(self,"test0",0,16,10,"test1",0)
    Room_CreateBlock(self,"test0",2,16,10,"tile_ground_0_up+down","na")
    Room_CreateBlock(self,"test0",1,16,10,"tile_edge_0_up+down-0","na")
    Room_CreateBlock(self,"test0",1,16,11,"tile_edge_0_down-1","na")
    Room_CreateSpawn(self,"test0",0,15,10)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    class test0_event_0:
        def __init__(self,Self,x,y):
            self.rpg = Self
            self.x = x
            self.y = y
            self.state = 0
            self.stateFrame = 3
            self.direction = 0
            self.directionArray = ["down","down","right","right","up","up","left","left"]
            Room_CreateBlock(self.rpg,"test0",4,self.x,self.y,"sprite_default_down_0","na")

        def Run(self):
            class test0_event_1_pauseEvent:
                def __init__(self,Self):
                    self.rpg = Self
                    if self.rpg.room["test2"]["event_6"].trigger == False: self.rpg.textBox = "Nuts"
                    elif self.rpg.room["test2"]["event_6"].trigger == True: self.rpg.textBox = "Fuck You"
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
                Room_CreateBlock(self.rpg,"test0",4,self.x,self.y,"sprite_default_"+self.directionArray[self.direction]+"_"+str(self.state)+"","")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # Event 0
    Room_CreateEvent(self,"test0",test0_event_0(self,14,2),"trigger")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    class test0_event_1:
        def __init__(self,Self):
            self.rpg = Self
            self.rgba = [0,0,0,255]
            self.direct = "up"

        def Run(self):
            if self.direct == "up":
                if self.rgba[0] < 12: 
                    for i in range(3): self.rgba[i] += 0.3
                else: self.direct = "down"
            if self.direct == "down":
                if self.rgba[0] > 0: 
                    for i in range(3): 
                        if self.rgba[i] - 0.3 < 0: self.rgba[i] = 0
                        else: self.rgba[i] -= 0.3
                else: self.direct = "up"
            Room_CreateWall(self.rpg,"test0",0,0,0,16,12,f"color_rgba_{str(math.floor(self.rgba[0]))}_{str(math.floor(self.rgba[1]))}_{str(math.floor(self.rgba[2]))}_{str(math.floor(self.rgba[3]))}","na")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # Event 1
    Room_CreateEvent(self,"test0",test0_event_1(self),"passive")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #