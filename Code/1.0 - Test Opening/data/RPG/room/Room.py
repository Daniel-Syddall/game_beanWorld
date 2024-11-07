#from data.RPG.room.generate.roomVariantsTest import roomVariantsTest
from data.RPG.room.generate.RPG_Rooms import roomBuild

def Room(self):
    self.room = {}
    #roomVariantsTest(self)
    roomBuild(self)