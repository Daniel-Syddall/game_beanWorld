from Imports.Data import *

def Menu_ImportRoom_Render():
    if data["init"] == False:
        render["menu_importRoom"] = {}
        render["menu_importRoom"]["text_importRoom"] = h1.render("Import Room",True,color["orange"])
        render["menu_importRoom"]["text_goBack"] = p.render("Go Back",True,color["black"])
        button["menu_importRoom"] = {}
        button["menu_importRoom"]["goBack"] = False
