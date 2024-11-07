from Game.Main.Func.RPG.Room.Builder import *
def test2(self):
    Room_Build(self,"test2",30,30,"color_black","color_black")

    Room_CreateSend(self,"test2",0,27,0,2,"tile_ground_3_left+right","test1",1)
    Room_CreateSpawn(self,"test2",0,27,1)

    louis_X = random(2,26)
    louis_Y = random(2,26)
    Room_CreateBlock(self,"test2",2,louis_X,louis_Y,"tile_louis-0-0","")
    Room_CreateBlock(self,"test2",2,louis_X+1,louis_Y,"tile_louis-1-0","")
    Room_CreateBlock(self,"test2",2,louis_X,louis_Y+1,"tile_louis-0-1","")
    Room_CreateBlock(self,"test2",2,louis_X+1,louis_Y+1,"tile_louis-1-1","")