from Imports.Data import *
from Imports.Widgets import *

def Menu_Select_Blit():
    Window.fill(color["grey"])
    Window.blit(render["menu_select"]["text_selectMenu"],(5,5))
    button["menu_select"]["createRoom"] = Widgets_Button(render["menu_select"]["text_createRoom"],362,100,725,300,color["white"],color["white"],color["black"],color["orange"])
    button["menu_select"]["importRoom"] = Widgets_Button(render["menu_select"]["text_importRoom"],362,500,725,700,color["white"],color["white"],color["black"],color["orange"])