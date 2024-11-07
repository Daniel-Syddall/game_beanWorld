from Imports.Data import *

def Widgets_Button(text,x1,y1,x2,y2,Fill1,Fill2,Outline1,Outline2):

    mouse = controller["mouse"]
    click = False

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

    if LowX <= mouse[0] <= HighX and LowY <= mouse[1] <= HighY:
        if controller["click"] == True: click = True
        pygame.draw.rect(Window,Fill2,(LowX,LowY,buttonW,buttonH),0)
        pygame.draw.rect(Window,Outline2,(LowX,LowY,buttonW,buttonH),2)
    else:
        pygame.draw.rect(Window,Fill1,(LowX,LowY,buttonW,buttonH),0)
        pygame.draw.rect(Window,Outline1,(LowX,LowY,buttonW,buttonH),2)

    Window.blit(text,((math.floor((buttonW-(text.get_width()))/2)+LowX),(math.floor((buttonH-(text.get_height()))/2)+LowY)))

    return click
    