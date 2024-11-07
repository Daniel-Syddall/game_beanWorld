from Data.Variables import *
from Data.Assets import *
from Imports.Rooms import *

if data["varInit"] == False:
    
    Room_Build("test0",17,13,"color_white","color_orange")

    Room_CreateSend("test0",0,16,10,"color_black","test1",0)
    Room_CreateSpawn("test0",0,15,10)

    