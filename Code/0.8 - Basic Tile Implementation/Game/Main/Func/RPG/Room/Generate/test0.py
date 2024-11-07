from Game.Main.Func.RPG.Room.Builder import *
def test0(self):
    Room_Build(self,"test0",17,13,"","color_orange")
    Room_SetGround(self,"test0",1,1,15,11,"1","0")
    
    Room_CreateBlock(self,"test0",1,15,10,"tile_ground_0_full","pass")
    Room_CreateSend(self,"test0",0,16,10,1,"tile_ground_0_up+down","test1",0)
    Room_CreateSpawn(self,"test0",0,15,10)
    Room_CreateBlock(self,"test0",0,16,10,"tile_ground_1_full","send")
