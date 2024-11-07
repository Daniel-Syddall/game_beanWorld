from Imports.Data import *
from Imports.Widgets import *

def Menu_CreateRoom_Blit():
    Window.fill(color["grey"])
    Window.blit(render["menu_createRoom"]["text_createRoom"],(2*display["grid"]["scale"],2*display["grid"]["scale"]))

    Widgets_Label(render["menu_createRoom"]["text_roomName"],18*display["grid"]["scale"],25*display["grid"]["scale"],118*display["grid"]["scale"],43*display["grid"]["scale"],color["white"],color["black"])
    button["menu_createRoom"]["click_dataEntry_roomName"],button["menu_createRoom"]["misClick_dataEntry_roomName"] = Widgets_Button(render["menu_createRoom"]["dataEntry_roomName"],143*display["grid"]["scale"],25*display["grid"]["scale"],231*display["grid"]["scale"],43*display["grid"]["scale"],color["white"],color["white"],color["black"],color["orange"])
    Widgets_Label(render["menu_createRoom"]["text_maxX"],18*display["grid"]["scale"],62*display["grid"]["scale"],118*display["grid"]["scale"],81*display["grid"]["scale"],color["white"],color["black"])
    button["menu_createRoom"]["click_dataEntry_maxX"],button["menu_createRoom"]["misClick_dataEntry_maxX"] = Widgets_Button(render["menu_createRoom"]["dataEntry_maxX"],143*display["grid"]["scale"],62*display["grid"]["scale"],231*display["grid"]["scale"],81*display["grid"]["scale"],color["white"],color["white"],color["black"],color["orange"])
    Widgets_Label(render["menu_createRoom"]["text_maxY"],18*display["grid"]["scale"],93*display["grid"]["scale"],118*display["grid"]["scale"],112*display["grid"]["scale"],color["white"],color["black"])
    button["menu_createRoom"]["click_dataEntry_maxY"],button["menu_createRoom"]["misClick_dataEntry_maxY"] = Widgets_Button(render["menu_createRoom"]["dataEntry_maxY"],143*display["grid"]["scale"],93*display["grid"]["scale"],231*display["grid"]["scale"],112*display["grid"]["scale"],color["white"],color["white"],color["black"],color["orange"])
    
    button["menu_createRoom"]["create"],button["null"] = Widgets_Button(render["menu_createRoom"]["text_create"],18*display["grid"]["scale"],131*display["grid"]["scale"],231*display["grid"]["scale"],150*display["grid"]["scale"],color["white"],color["white"],color["black"],color["orange"])
    button["menu_createRoom"]["goBack"],button["null"] = Widgets_Button(render["menu_createRoom"]["text_goBack"],212*display["grid"]["scale"],175*display["grid"]["scale"],262*display["grid"]["scale"],200*display["grid"]["scale"],color["white"],color["white"],color["black"],color["orange"])