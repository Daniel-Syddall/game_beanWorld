from Data.Variables import *
from Data.Assets import *
from Imports.Rooms import *

if data["varInit"] == False:
    
    Room_Build("test1",19,15,"color_white","color_orange")

    Room_CreateWall("test1",0,4,4,14,4,"color_orange")
    Room_ChangeState("test1","",4,4,14,4)
    Room_CreateWall("test1",0,9,6,9,11,"color_orange")
    Room_ChangeState("test1","",9,6,9,11)

    Room_CreateSend("test1",0,0,2,"color_black","test0",0)
    Room_CreateSpawn("test1",0,1,2)

    Room_CreateSend("test1",1,16,14,"color_grey","test2",0)
    Room_CreateSpawn("test1",1,16,13)

    Room_CreateSend("test1",2,17,1,"color_brown","test1",3)
    Room_CreateSpawn("test1",2,16,2)

    Room_CreateSend("test1",3,1,13,"color_brown","test1",2)
    Room_CreateSpawn("test1",3,2,12)