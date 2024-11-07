from Imports.Data import *
from Imports.Widgets import *

def Menu_CreateRoom_Blit():
    Window.fill(color["grey"])
    Window.blit(render["menu_createRoom"]["text_createRoom"],(5,5))

    Widgets_Label(render["menu_createRoom"]["text_roomName"],75,100,475,175,color["white"],color["black"])
    button["menu_createRoom"]["dataEntry_roomName"] = Widgets_Button(render["menu_createRoom"]["dataEntry_roomName"],575,100,925,175,color["white"],color["white"],color["black"],color["orange"])
    Widgets_Label(render["menu_createRoom"]["text_maxX"],75,250,475,325,color["white"],color["black"])
    button["menu_createRoom"]["dataEntry_maxX"] = Widgets_Button(render["menu_createRoom"]["dataEntry_maxX"],575,250,925,325,color["white"],color["white"],color["black"],color["orange"])
    Widgets_Label(render["menu_createRoom"]["text_maxY"],75,375,475,450,color["white"],color["black"])
    button["menu_createRoom"]["dataEntry_maxY"] = Widgets_Button(render["menu_createRoom"]["dataEntry_maxY"],575,375,925,450,color["white"],color["white"],color["black"],color["orange"])
    
    button["menu_createRoom"]["create"] = Widgets_Button(render["menu_createRoom"]["text_create"],75,525,925,600,color["white"],color["white"],color["black"],color["orange"])
    button["menu_createRoom"]["goBack"] = Widgets_Button(render["menu_createRoom"]["text_goBack"],850,700,1050,800,color["white"],color["white"],color["black"],color["orange"])