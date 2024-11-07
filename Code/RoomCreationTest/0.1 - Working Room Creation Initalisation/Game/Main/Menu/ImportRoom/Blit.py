from Imports.Data import *
from Imports.Widgets import *

def Menu_ImportRoom_Blit():
    Window.fill(color["grey"])
    Window.blit(render["menu_importRoom"]["text_importRoom"],(5,5))
    button["menu_importRoom"]["goBack"] = Widgets_Button(render["menu_importRoom"]["text_goBack"],850,700,1050,800,color["white"],color["white"],color["black"],color["orange"])