from Imports.Data import *

def Menu_Select_Render():
    if data["init"] == False:
        render["menu_select"] = {}
        render["menu_select"]["text_selectMenu"] = h1.render("Select Menu",True,color["orange"])
        render["menu_select"]["text_createRoom"] = h1.render("Create Room",True,color["black"])
        render["menu_select"]["text_importRoom"] = h1.render("Import Room",True,color["black"])
        button["menu_select"] = {}
        button["menu_select"]["createRoom"] = False
        button["menu_select"]["importRoom"] = False