from Game.Main.Func.RPG.Room.Builder import *

def test2(self):
    Room_Build(self,"test2",100,100,"color_black","color_black")

    Room_CreateSend(self,"test2",0,27,0,2,"tile_ground_3_left+right","test1",1)
    Room_CreateSpawn(self,"test2",0,27,1)

    class test2_event_0:
        def __init__(self,Self):
            self.rpg = Self
            self.tick = 0
            self.tickPass = 5
            self.louis_X = random(2,96)
            self.louis_Y = random(2,96)
            Room_CreateBlock(self.rpg,"test2",2,self.louis_X,self.louis_Y,"tile_louis-0-0","")
            Room_CreateBlock(self.rpg,"test2",2,self.louis_X+1,self.louis_Y,"tile_louis-1-0","")
            Room_CreateBlock(self.rpg,"test2",2,self.louis_X,self.louis_Y+1,"tile_louis-0-1","")
            Room_CreateBlock(self.rpg,"test2",2,self.louis_X+1,self.louis_Y+1,"tile_louis-1-1","")
        def Run(self):
            self.tick += 1
            if self.tick == self.tickPass:
                self.tick = 0
                Room_CreateBlock(self.rpg,"test2",2,self.louis_X,self.louis_Y,"","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.louis_X+1,self.louis_Y,"","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.louis_X,self.louis_Y+1,"","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.louis_X+1,self.louis_Y+1,"","pass")
                self.louis_X = random(2,96)
                self.louis_Y = random(2,96)
                Room_CreateBlock(self.rpg,"test2",2,self.louis_X,self.louis_Y,"tile_louis-0-0","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.louis_X+1,self.louis_Y,"tile_louis-1-0","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.louis_X,self.louis_Y+1,"tile_louis-0-1","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.louis_X+1,self.louis_Y+1,"tile_louis-1-1","pass")

    class test2_event_1:
        def __init__(self,Self):
            self.rpg = Self
            self.tick = 0
            self.tickPass = 5
            self.wigi_X = random(2,95)
            self.wigi_Y = random(2,95)
            Room_CreateBlock(self.rpg,"test2",2,self.wigi_X,self.wigi_Y,"tile_wigi-0-0","pass")
            Room_CreateBlock(self.rpg,"test2",2,self.wigi_X+1,self.wigi_Y,"tile_wigi-1-0","pass")
            Room_CreateBlock(self.rpg,"test2",2,self.wigi_X,self.wigi_Y+1,"tile_wigi-0-1","pass")
            Room_CreateBlock(self.rpg,"test2",2,self.wigi_X+1,self.wigi_Y+1,"tile_wigi-1-1","pass")
            Room_CreateBlock(self.rpg,"test2",2,self.wigi_X,self.wigi_Y+2,"tile_wigi-0-2","pass")
            Room_CreateBlock(self.rpg,"test2",2,self.wigi_X+1,self.wigi_Y+2,"tile_wigi-1-2","pass")
        def Run(self):
            self.tick += 1
            if self.tick == self.tickPass:
                self.tick = 0
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X,self.wigi_Y,"","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X+1,self.wigi_Y,"","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X,self.wigi_Y+1,"","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X+1,self.wigi_Y+1,"","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X,self.wigi_Y+2,"","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X+1,self.wigi_Y+2,"","pass")
                self.wigi_X = random(2,95)
                self.wigi_Y = random(2,95)
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X,self.wigi_Y,"tile_wigi-0-0","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X+1,self.wigi_Y,"tile_wigi-1-0","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X,self.wigi_Y+1,"tile_wigi-0-1","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X+1,self.wigi_Y+1,"tile_wigi-1-1","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X,self.wigi_Y+2,"tile_wigi-0-2","pass")
                Room_CreateBlock(self.rpg,"test2",2,self.wigi_X+1,self.wigi_Y+2,"tile_wigi-1-2","pass")

    for _ in range(20): Room_CreateEvent(self,"test2",test2_event_0(self),"passive")
    for _ in range(20): Room_CreateEvent(self,"test2",test2_event_1(self),"passive")