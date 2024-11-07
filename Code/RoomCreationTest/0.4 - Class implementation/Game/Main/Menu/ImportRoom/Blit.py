from Imports.Data import *
from Imports.Widgets import *

def Menu_ImportRoom_Blit():
    Window.fill(color["grey"])
    Window.blit(render["menu_importRoom"]["text_importRoom"],(2*display["grid"]["scale"],2*display["grid"]["scale"]))

    Widgets_Label(render["menu_importRoom"]["text_fileName"],18*display["grid"]["scale"],25*display["grid"]["scale"],118*display["grid"]["scale"],43*display["grid"]["scale"],color["white"],color["black"])
    button["menu_importRoom"]["click_dataEntry_fileName"],button["menu_importRoom"]["misClick_dataEntry_fileName"] = Widgets_Button(render["menu_importRoom"]["dataEntry_fileName"],143*display["grid"]["scale"],25*display["grid"]["scale"],231*display["grid"]["scale"],43*display["grid"]["scale"],color["white"],color["white"],color["black"],color["orange"])

    button["menu_importRoom"]["import"],button["null"] = Widgets_Button(render["menu_importRoom"]["text_import"],18*display["grid"]["scale"],56*display["grid"]["scale"],231*display["grid"]["scale"],75*display["grid"]["scale"],color["white"],color["white"],color["black"],color["orange"])
    button["menu_importRoom"]["goBack"],button["null"] = Widgets_Button(render["menu_importRoom"]["text_goBack"],212*display["grid"]["scale"],175*display["grid"]["scale"],262*display["grid"]["scale"],200*display["grid"]["scale"],color["white"],color["white"],color["black"],color["orange"])