from Data.Variables import *
from Data.Assets import *
from Imports.Rooms import *

if data["varInit"] == False:
    Build("test1",19,15,"color_white","color_orange")

    room["test1"]["spawn_0_X"] = 1
    room["test1"]["spawn_0_Y"] = 2

    room["test1"]["0_0_2"] = "color_black"
    room["test1"]["state_0_2"] = "send"
    room["test1"]["send_0_X"] = 0
    room["test1"]["send_0_Y"] = 2
    room["test1"]["send_0_room"] = "test0"
    room["test1"]["send_0_spawn"] = 0