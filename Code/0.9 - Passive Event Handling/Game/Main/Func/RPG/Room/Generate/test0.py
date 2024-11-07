from Game.Main.Func.RPG.Room.Builder import *
def test0(self):
    Room_Build(self,"test0",17,13,"","color_orange")
    Room_SetGround(self,"test0",1,1,15,11,"1","0")
    
    Room_CreateBlock(self,"test0",1,15,10,"tile_ground_0_upRight+downRight","pass")
    Room_CreateSend(self,"test0",0,16,10,1,"tile_ground_0_up+down","test1",0)
    Room_CreateSpawn(self,"test0",0,15,10)
    Room_CreateBlock(self,"test0",0,16,10,"tile_ground_1_full","send")

    class test0_event_0:
        def __init__(self,Self):
            self.rpg = Self
            self.tick = 0
            self.tickPass = 15
            self.state = 0
            self.StateArray = [[5,6,7,7,7,6,5,5],[5,5,5,6,7,7,7,6]]
            Room_CreateBlock(self.rpg,"test0",2,self.StateArray[0][self.state],self.StateArray[1][self.state],"color_black","")

        def Run(self):
            self.tick += 1
            if self.tick == self.tickPass:
                self.tick = 0
                x = self.StateArray[0][self.state]
                y = self.StateArray[1][self.state]
                self.state += 1
                if self.state > len(self.StateArray[0])-1: self.state = 0
                Room_CreateBlock(self.rpg,"test0",2,self.StateArray[0][self.state],self.StateArray[1][self.state],"color_black","")
                Room_CreateBlock(self.rpg,"test0",2,x,y,"","pass")

    Room_CreateEvent(self,"test0",test0_event_0(self),0,"passive")