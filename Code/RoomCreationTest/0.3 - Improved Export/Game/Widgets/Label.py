from Imports.Data import *

def Widgets_Label(text,x1,y1,x2,y2,Fill,Outline):

    if x1 <= x2:
        LowX = x1
        HighX = x2
    elif x2 < x1:
        LowX = x2
        HighX = x1
    if y1 <= y2:
        LowY = y1
        HighY = y2
    elif y2 < y1:
        LowY = y2
        HighY = y1

    buttonW = HighX - LowX
    buttonH = HighY - LowY

    pygame.draw.rect(Window,Fill,(LowX,LowY,buttonW,buttonH),0)
    pygame.draw.rect(Window,Outline,(LowX,LowY,buttonW,buttonH),2)

    Window.blit(text,((math.floor((buttonW-(text.get_width()))/2)+LowX),(math.floor((buttonH-(text.get_height()))/2)+LowY)))