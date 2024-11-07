from Game.Main.Func.RPG.Room.Builder import *

def test0(self):
    Room_Build(self,"test0",17,13,"","color_orange")
    Room_SetGround(self,"test0",1,1,15,11,"1","0")
    
    # Room 0 to Room 1  = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    Room_CreateBlock(self,"test0",1,15,10,"tile_ground_0_upRight+downRight","na")
    Room_CreateBlock(self,"test0",0,16,10,"tile_ground_1_full","na")

    Room_CreateSend(self,"test0",0,16,10,1,"tile_ground_0_up+down","test1",0)
    Room_CreateSpawn(self,"test0",0,15,10)

    # - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    class test0_event_0:
        def __init__(self,Self):
            self.rpg = Self
            self.tick = 0
            self.tickPass = 2
            self.state = 0
            self.StateArray = [[5,6,7,7,7,6,5,5],[5,5,5,6,7,7,7,6]]
            Room_CreateBlock(self.rpg,"test0",3,self.StateArray[0][self.state],self.StateArray[1][self.state],"color_black","na")

        def Run(self):
            self.tick += 1
            if self.tick == self.tickPass:
                self.tick = 0
                x = self.StateArray[0][self.state]
                y = self.StateArray[1][self.state]
                self.state += 1
                if self.state > len(self.StateArray[0])-1: self.state = 0
                Room_CreateBlock(self.rpg,"test0",3,self.StateArray[0][self.state],self.StateArray[1][self.state],"color_black","na")
                Room_CreateBlock(self.rpg,"test0",3,x,y,"","na")

    class test0_event_1:
        def __init__(self,Self,x,y):
            self.rpg = Self
            self.x = x
            self.y = y
            self.state = 0
            self.stateFrame = 3
            self.direction = 0
            self.directionArray = ["down","down","right","right","up","up","left","left"]
            Room_CreateBlock(self.rpg,"test0",3,self.x,self.y,"sprite_default_down_0","na")

        def Run(self):
            class test0_event_1_pauseEvent:
                def __init__(self,Self):
                    self.rpg = Self
                    if self.rpg.room["test2"]["event_40"].trigger == False: self.rpg.textBox = "Nuts"
                    elif self.rpg.room["test2"]["event_40"].trigger == True: self.rpg.textBox = "Fuck You"
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
                Room_CreateBlock(self.rpg,"test0",3,self.x,self.y,"sprite_default_"+self.directionArray[self.direction]+"_"+str(self.state)+"","")

    class test0_event_2:
        def __init__(self,Self):
            self.rpg = Self
            self.rgba = [150,120,0,150]
            self.direction = "up"

        def Run(self):
            if self.direction == "up":
                if self.rgba[1] < 175:
                    self.rgba[0] += 2
                    self.rgba[1] += 2
                else: self.direction = "down"

            elif self.direction == "down":
                if self.rgba[1] > 150: 
                    self.rgba[0] -= 2
                    self.rgba[1] -= 2
                else: self.direction = "up"
            
            Room_CreateWall(self.rpg,"test0",4,0,0,16,0,"color_rgba_"+str(self.rgba[0])+"_"+str(self.rgba[1])+"_"+str(self.rgba[2])+"_"+str(self.rgba[3]),"na")
            Room_CreateWall(self.rpg,"test0",4,16,0,16,12,"color_rgba_"+str(self.rgba[0])+"_"+str(self.rgba[1])+"_"+str(self.rgba[2])+"_"+str(self.rgba[3]),"na")
            Room_CreateWall(self.rpg,"test0",4,0,12,16,12,"color_rgba_"+str(self.rgba[0])+"_"+str(self.rgba[1])+"_"+str(self.rgba[2])+"_"+str(self.rgba[3]),"na")
            Room_CreateWall(self.rpg,"test0",4,0,12,0,0,"color_rgba_"+str(self.rgba[0])+"_"+str(self.rgba[1])+"_"+str(self.rgba[2])+"_"+str(self.rgba[3]),"na")
            Room_CreateBlock(self.rpg,"test0",4,16,10,"","na")
            

    class test0_event_3:
        def __init__(self,Self):
            self.rpg = Self
            self.rgba = [0,0,0,100]
            self.direction = "up"

        def Run(self):
            if self.direction == "up":
                if self.rgba[3] < 150:
                    self.rgba[3] += 1
                else: self.direction = "down"

            elif self.direction == "down":
                if self.rgba[3] > 100: 
                    self.rgba[3] -= 1
                else: self.direction = "up"

            Room_CreateWall(self.rpg,"test0",5,0,0,16,12,"color_rgba_"+str(self.rgba[0])+"_"+str(self.rgba[1])+"_"+str(self.rgba[2])+"_"+str(self.rgba[3]),"na")

    # Event 0
    Room_CreateEvent(self,"test0",test0_event_0(self),"passive")
    # Event 1
    Room_CreateEvent(self,"test0",test0_event_1(self,10,2),"trigger")
    # Event 2
    Room_CreateEvent(self,"test0",test0_event_2(self),"passive")
    # Event 3
    Room_CreateEvent(self,"test0",test0_event_3(self),"passive")