from Data.Variables import *
from Data.Assets import *
from Imports.Rooms import *

if data["varInit"] == False:
    Build("test0",17,13,"color_white","color_orange")


    room["test0"]["0_6_6"] = "color_orange"
    room["test0"]["state_6_6"] = ""


    room["test0"]["spawn_0_X"] = 15
    room["test0"]["spawn_0_Y"] = 10

    room["test0"]["0_16_10"] = "color_black"
    room["test0"]["state_16_10"] = "send"
    room["test0"]["send_0_X"] = 16
    room["test0"]["send_0_Y"] = 10
    room["test0"]["send_0_room"] = "test1"
    room["test0"]["send_0_spawn"] = 0