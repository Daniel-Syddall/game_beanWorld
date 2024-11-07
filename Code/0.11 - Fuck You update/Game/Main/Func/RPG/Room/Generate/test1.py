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

    Room_CreateSend(self,"test1",2,17,1,2,"tile_ground_0_left+up+right+down","test1",3)
    Room_CreateSpawn(self,"test1",2,16,2)
    Room_CreateSend(self,"test1",3,1,13,2,"tile_ground_0_left+up+right+down","test1",2)
    Room_CreateSpawn(self,"test1",3,2,12)

    Room_CreateBlock(self,"test1",1,1,2,"tile_ground_2_downLeft+upLeft","pass")
    Room_CreateSend(self,"test1",0,0,2,1,"tile_ground_2_up+down","test0",0)
    Room_CreateSpawn(self,"test1",0,1,2)
    Room_CreateBlock(self,"test1",0,0,2,"tile_ground_3_full","send")
    
    Room_CreateBlock(self,"test1",1,16,13,"tile_ground_2_downRight+downLeft","pass")
    Room_CreateSend(self,"test1",1,16,14,2,"tile_ground_2_left+right","test2",0)
    Room_CreateSpawn(self,"test1",1,16,13)
    Room_CreateBlock(self,"test1",0,16,14,"tile_ground_3_full","send")