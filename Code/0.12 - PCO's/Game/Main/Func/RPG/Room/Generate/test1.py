from Game.Main.Func.RPG.Room.Builder import *

def test1(self):
    Room_Build(self,"test1",19,15,"","color_saturatedBrown")
    Room_SetGround(self,"test1",1,1,17,13,"3","2")
    
    Room_CreateWall(self,"test1",2,4,4,14,4,"color_saturatedBrown","")
    Room_GroundDisturbance(self,"test1",4,4,14,4,"3","2")


    

    Room_CreateWall(self,"test1",2,8,10,10,12,"color_saturatedBrown","")
    Room_GroundDisturbance(self,"test1",8,10,10,12,"3","2")
    Room_CreateBlock(self,"test1",1,7,13,"tile_ground_2_down+upRight","pass")
    Room_CreateWall(self,"test1",1,8,13,10,13,"tile_ground_2_up+down","pass")
    Room_CreateBlock(self,"test1",1,11,13,"tile_ground_2_down+upLeft","pass")

    # Teleport Test  = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    Room_CreateSend(self,"test1",2,17,1,2,"tile_ground_0_left+up+right+down","test1",3)
    Room_CreateSpawn(self,"test1",2,16,2)
    Room_CreateSend(self,"test1",3,1,13,2,"tile_ground_0_left+up+right+down","test1",2)
    Room_CreateSpawn(self,"test1",3,2,12)

    # Room 1 to Room 0  = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    Room_CreateBlock(self,"test1",1,1,2,"tile_ground_2_downLeft+upLeft","pass")
    Room_CreateSend(self,"test1",0,0,2,1,"tile_ground_2_up+down","test0",0)
    Room_CreateSpawn(self,"test1",0,1,2)
    Room_CreateBlock(self,"test1",0,0,2,"tile_ground_3_full","send")
    
    # Room 1 to Room 2  = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    Room_CreateBlock(self,"test1",1,16,13,"tile_ground_2_downRight+downLeft","pass")
    Room_CreateSend(self,"test1",1,16,14,2,"tile_ground_2_left+right","test2",0)
    Room_CreateSpawn(self,"test1",1,16,13)
    Room_CreateBlock(self,"test1",0,16,14,"tile_ground_3_full","send")

    # - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    class test1_event_0:
        def __init__(self,Self,x,y,range):
            self.rpg = Self
            self.x = x
            self.y = y
            self.range = range
            self.rgba = [0,0,0,0]

        def Run(self):
            look = []
            fill = []

            self.x = math.floor(self.rpg.player["roomX"]/16)
            self.y = math.floor(self.rpg.player["roomY"]/16)

            minX = self.x - self.range
            maxX = self.x + self.range
            minY = self.y - self.range
            maxY = self.y + self.range

            for x in range((maxX-minX)+1):
                look.append([])
                for y in range((maxY-minY)+1):
                    if minX+x < 0 or minY+y < 0 or minX+x > self.rpg.room["test1"]["maxX"]-1 or minY+y > self.rpg.room["test1"]["maxY"]-1: look[x].append("x")
                    else: look[x].append("")

            for i in range(self.range):
                fill.append([])
                temp_lookRange = 1 + i
                x = temp_lookRange
                y = 0
                for _ in range(temp_lookRange+1):
                    fill[i].append(look[self.range+x][self.range+y]+"_"+str(x)+"_"+str(y))
                    if x != 0: fill[i].append(look[self.range-x][self.range+y]+"_-"+str(x)+"_"+str(y))
                    if y != 0: fill[i].append(look[self.range+x][self.range-y]+"_"+str(x)+"_-"+str(y))
                    if x != 0 and y != 0: fill[i].append(look[self.range-x][self.range-y]+"_-"+str(x)+"_-"+str(y))
                    x -= 1
                    y += 1
            
            temp_rgba = [0,0,0,50]
            Room_CreateBlock(self.rpg,"test1",5,self.x,self.y,"color_rgba_"+str(temp_rgba[0])+"_"+str(temp_rgba[1])+"_"+str(temp_rgba[2])+"_"+str(temp_rgba[3]),"na")

            for l in range(len(fill)):
                temp_rgba[3] += 25
                for i in range(len(fill[l])):
                    temp_tileEval = fill[l][i].split("_")
                    if temp_tileEval[0] != "x":
                        Room_CreateBlock(self.rpg,"test1",5,self.x+int(temp_tileEval[1]),self.y+int(temp_tileEval[2]),"color_rgba_"+str(temp_rgba[0])+"_"+str(temp_rgba[1])+"_"+str(temp_rgba[2])+"_"+str(temp_rgba[3]),"na")

    #Room_CreateEvent(self,"test1",test1_event_0(self,6,6,30),"passive")
    Room_CreateWall(self,"test1",5,0,0,18,14,"pco_shadow","na")