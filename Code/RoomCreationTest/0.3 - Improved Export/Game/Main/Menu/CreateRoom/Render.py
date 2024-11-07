from Imports.Data import *

def Menu_CreateRoom_Render():
    if data["init"] == False:
        render["menu_createRoom"] = {}
        render["menu_createRoom"]["text_createRoom"] = h1.render("Create Room",True,color["orange"])
        render["menu_createRoom"]["text_roomName"] = h2.render("Room Name :",True,color["black"])
        render["menu_createRoom"]["text_maxX"] = h2.render("Max X :",True,color["black"])
        render["menu_createRoom"]["text_maxY"] = h2.render("Max Y :",True,color["black"])
        render["menu_createRoom"]["text_create"] = h2.render("Create",True,color["black"])
        render["menu_createRoom"]["text_goBack"] = p.render("Go Back",True,color["black"])
        button["menu_createRoom"] = {}
        button["menu_createRoom"]["click_dataEntry_roomName"] = False
        button["menu_createRoom"]["misClick_dataEntry_roomName"] = False
        button["menu_createRoom"]["click_dataEntry_maxX"] = False
        button["menu_createRoom"]["misClick_dataEntry_maxX"] = False
        button["menu_createRoom"]["click_dataEntry_maxY"] = False
        button["menu_createRoom"]["misClick_dataEntry_maxY"] = False
        button["menu_createRoom"]["create"] = False
        button["menu_createRoom"]["goBack"] = False
        dataEntry["menu_createRoom"] = {}
        dataEntry["menu_createRoom"]["busy"] = False
        dataEntry["menu_createRoom"]["check_roomName"] = False
        dataEntry["menu_createRoom"]["store_roomName"] = ""
        dataEntry["menu_createRoom"]["check_maxX"] = False
        dataEntry["menu_createRoom"]["store_maxX"] = ""
        dataEntry["menu_createRoom"]["check_maxY"] = False
        dataEntry["menu_createRoom"]["store_maxY"] = ""
    
    render["menu_createRoom"]["dataEntry_roomName"] = h2.render(dataEntry["menu_createRoom"]["store_roomName"],True,color["black"])
    render["menu_createRoom"]["dataEntry_maxX"] = h2.render(dataEntry["menu_createRoom"]["store_maxX"],True,color["black"])
    render["menu_createRoom"]["dataEntry_maxY"] = h2.render(dataEntry["menu_createRoom"]["store_maxY"],True,color["black"])