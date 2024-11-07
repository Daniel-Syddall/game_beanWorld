from Game.Main.Func.RPG.Room.Builder import *

def test2(self):

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    Room_Build(self,"test2",30,30,"color_black","color_black")

    Room_CreateSend(self,"test2",0,15,0,"test1",1)
    Room_CreateBlock(self,"test2",2,15,0,"tile_ground_3_left+right","na")
    Room_CreateBlock(self,"test2",1,15,0,"tile_ground_2_full","send")
    Room_CreateSpawn(self,"test2",0,15,1)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    class test2_event_0:
        def __init__(self,Self):
            self.rpg = Self
            self.tick = 0
            self.tickPass = 5
            self.louis_X = random(2,26)
            self.louis_Y = random(2,26)
            Room_CreateBlock(self.rpg,"test2",3,self.louis_X,self.louis_Y,"tile_louis-0-0","")
            Room_CreateBlock(self.rpg,"test2",3,self.louis_X+1,self.louis_Y,"tile_louis-1-0","")
            Room_CreateBlock(self.rpg,"test2",3,self.louis_X,self.louis_Y+1,"tile_louis-0-1","")
            Room_CreateBlock(self.rpg,"test2",3,self.louis_X+1,self.louis_Y+1,"tile_louis-1-1","")
        def Run(self):
            self.tick += 1
            if self.tick == self.tickPass:
                self.tick = 0
                Room_CreateBlock(self.rpg,"test2",3,self.louis_X,self.louis_Y,"","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.louis_X+1,self.louis_Y,"","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.louis_X,self.louis_Y+1,"","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.louis_X+1,self.louis_Y+1,"","pass")
                self.louis_X = random(2,26)
                self.louis_Y = random(2,26)
                Room_CreateBlock(self.rpg,"test2",3,self.louis_X,self.louis_Y,"tile_louis-0-0","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.louis_X+1,self.louis_Y,"tile_louis-1-0","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.louis_X,self.louis_Y+1,"tile_louis-0-1","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.louis_X+1,self.louis_Y+1,"tile_louis-1-1","pass")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    class test2_event_1:
        def __init__(self,Self):
            self.rpg = Self
            self.tick = 0
            self.tickPass = 5
            self.wigi_X = random(2,25)
            self.wigi_Y = random(2,25)
            Room_CreateBlock(self.rpg,"test2",3,self.wigi_X,self.wigi_Y,"tile_wigi-0-0","pass")
            Room_CreateBlock(self.rpg,"test2",3,self.wigi_X+1,self.wigi_Y,"tile_wigi-1-0","pass")
            Room_CreateBlock(self.rpg,"test2",3,self.wigi_X,self.wigi_Y+1,"tile_wigi-0-1","pass")
            Room_CreateBlock(self.rpg,"test2",3,self.wigi_X+1,self.wigi_Y+1,"tile_wigi-1-1","pass")
            Room_CreateBlock(self.rpg,"test2",3,self.wigi_X,self.wigi_Y+2,"tile_wigi-0-2","pass")
            Room_CreateBlock(self.rpg,"test2",3,self.wigi_X+1,self.wigi_Y+2,"tile_wigi-1-2","pass")
        def Run(self):
            self.tick += 1
            if self.tick == self.tickPass:
                self.tick = 0
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X,self.wigi_Y,"","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X+1,self.wigi_Y,"","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X,self.wigi_Y+1,"","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X+1,self.wigi_Y+1,"","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X,self.wigi_Y+2,"","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X+1,self.wigi_Y+2,"","pass")
                self.wigi_X = random(2,25)
                self.wigi_Y = random(2,25)
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X,self.wigi_Y,"tile_wigi-0-0","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X+1,self.wigi_Y,"tile_wigi-1-0","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X,self.wigi_Y+1,"tile_wigi-0-1","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X+1,self.wigi_Y+1,"tile_wigi-1-1","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X,self.wigi_Y+2,"tile_wigi-0-2","pass")
                Room_CreateBlock(self.rpg,"test2",3,self.wigi_X+1,self.wigi_Y+2,"tile_wigi-1-2","pass")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    class test2_event_2:
        def __init__(self,Self):
            self.rpg = Self
            self.trigger = False
        def Run(self):
            self.trigger = True

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # Event 0 - 2
    for _ in range(3): Room_CreateEvent(self,"test2",test2_event_0(self),"passive")

    # Event 3 - 5
    for _ in range(3): Room_CreateEvent(self,"test2",test2_event_1(self),"passive")

    # Event 6
    Room_CreateEvent(self,"test2",test2_event_2(self),"passive")