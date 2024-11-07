from Imports.Data import *
from Imports.Widgets import *

def Menu_Select_Blit():
    Window.fill(color["grey"])
    Window.blit(render["menu_select"]["text_selectMenu"],(2*display["grid"]["scale"],2*display["grid"]["scale"]))
    button["menu_select"]["createRoom"],button["null"] = Widgets_Button(render["menu_select"]["text_createRoom"],90*display["grid"]["scale"],25*display["grid"]["scale"],181*display["grid"]["scale"],75*display["grid"]["scale"],color["white"],color["white"],color["black"],color["orange"])
    button["menu_select"]["importRoom"],button["null"] = Widgets_Button(render["menu_select"]["text_importRoom"],90*display["grid"]["scale"],125*display["grid"]["scale"],181*display["grid"]["scale"],175*display["grid"]["scale"],color["white"],color["white"],color["black"],color["orange"])