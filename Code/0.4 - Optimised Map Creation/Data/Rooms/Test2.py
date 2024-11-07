from Data.Variables import *
from Data.Assets import *
from Imports.Rooms import *

if data["varInit"] == False:
    
    Room_Build("test2",30,30,"color_black","color_black")

    Room_CreateWall("test2",0,2,27,4,27,"color_grey")
    Room_ChangeState("test2","",2,27,4,27)
    Room_CreateWall("test2",0,3,26,3,24,"color_grey")
    Room_ChangeState("test2","",3,26,3,24)

    Room_CreateMerge("test2","louis",0,26,26)
    Room_ChangeState("test2","",26,26,27,27)

    Room_CreateSend("test2",0,27,0,"color_grey","test1",1)
    Room_CreateSpawn("test2",0,27,1)