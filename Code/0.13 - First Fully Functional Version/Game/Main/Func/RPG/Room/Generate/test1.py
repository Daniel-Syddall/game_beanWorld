from Game.Main.Func.RPG.Room.Builder import *

def test1(self):

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    Room_Build(self,"test1",19,15,"","color_saturatedBrown")
    Room_SetGround(self,"test1",1,1,17,13,"3","2")
    
# Wall Generation - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    Room_CreateWall(self,"test1",2,4,4,14,4,"color_saturatedBrown","")
    Room_GroundDisturbance(self,"test1",4,4,14,4,"3","2")

    Room_CreateWall(self,"test1",2,8,10,10,12,"color_saturatedBrown","")
    Room_GroundDisturbance(self,"test1",8,10,10,12,"3","2")
    Room_CreateBlock(self,"test1",2,7,13,"tile_ground_2_down+upRight","na")
    Room_CreateWall(self,"test1",2,8,13,10,13,"tile_ground_2_up+down","na")
    Room_CreateBlock(self,"test1",2,11,13,"tile_ground_2_down+upLeft","na")

# Teleport Test - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    Room_CreateSend(self,"test1",2,17,1,"test1",3)
    Room_CreateBlock(self,"test1",3,17,1,"tile_ground_0_left+up+right+down","na")
    Room_CreateSpawn(self,"test1",2,16,2)
    Room_CreateSend(self,"test1",3,1,13,"test1",2)
    Room_CreateBlock(self,"test1",3,1,13,"tile_ground_0_left+up+right+down","na")
    Room_CreateSpawn(self,"test1",3,2,12)

# Teleport Room 1 to Room 0 - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    Room_CreateBlock(self,"test1",2,1,2,"tile_ground_2_downLeft+upLeft","na")
    Room_CreateSend(self,"test1",0,0,2,"test0",0)
    Room_CreateBlock(self,"test1",2,0,2,"tile_ground_2_up+down","na")
    Room_CreateBlock(self,"test1",1,0,2,"tile_ground_3_full","na")
    Room_CreateSpawn(self,"test1",0,1,2)
    
# Teleport Room 1 to Room 2 - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    Room_CreateBlock(self,"test1",2,16,13,"tile_ground_2_downRight+downLeft","na")
    Room_CreateSend(self,"test1",1,16,14,"test2",0)
    Room_CreateBlock(self,"test1",2,16,14,"tile_ground_2_left+right","na")
    Room_CreateBlock(self,"test1",1,16,14,"tile_ground_3_full","na")
    Room_CreateSpawn(self,"test1",1,16,13)

# Player Central Overlay Shadow - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = #

    Room_CreateWall(self,"test1",5,0,0,18,14,"pco_shadow","na")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #