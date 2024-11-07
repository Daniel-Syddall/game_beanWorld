from Imports.Data import *

def Menu_ImportRoom_Render():
    if data["init"] == False:
        render["menu_importRoom"] = {}
        render["menu_importRoom"]["text_importRoom"] = h1.render("Import Room",True,color["orange"])
        render["menu_importRoom"]["text_fileName"] = h2.render("File Name (Without .txt) :",True,color["black"])
        render["menu_importRoom"]["text_import"] = h2.render("Import",True,color["black"])
        render["menu_importRoom"]["text_goBack"] = p.render("Go Back",True,color["black"])
        button["menu_importRoom"] = {}
        button["menu_importRoom"]["click_dataEntry_fileName"] = False
        button["menu_importRoom"]["misClick_dataEntry_fileName"] = False
        button["menu_importRoom"]["import"] = False
        button["menu_importRoom"]["goBack"] = False
        dataEntry["menu_importRoom"] = {}
        dataEntry["menu_importRoom"]["busy"] = False
        dataEntry["menu_importRoom"]["check_fileName"] = False
        dataEntry["menu_importRoom"]["store_fileName"] = ""

    render["menu_importRoom"]["dataEntry_fileName"] = h2.render(dataEntry["menu_importRoom"]["store_fileName"],True,color["black"])