from Imports.Data import *
from Imports.Widgets import *

def Menu_ImportRoom_Blit():
    Window.fill(color["grey"])
    Window.blit(render["menu_importRoom"]["text_importRoom"],(5,5))

    Widgets_Label(render["menu_importRoom"]["text_fileName"],75,100,475,175,color["white"],color["black"])
    button["menu_importRoom"]["dataEntry_fileName"] = Widgets_Button(render["menu_importRoom"]["dataEntry_fileName"],575,100,925,175,color["white"],color["white"],color["black"],color["orange"])

    button["menu_importRoom"]["import"] = Widgets_Button(render["menu_importRoom"]["text_import"],75,225,925,300,color["white"],color["white"],color["black"],color["orange"])
    button["menu_importRoom"]["goBack"] = Widgets_Button(render["menu_importRoom"]["text_goBack"],850,700,1050,800,color["white"],color["white"],color["black"],color["orange"])