from Imports.MainData import *
from Game.Widgets.Button import Widget_Button

if data["init"] == False: 
    gameState = gameState_Temp()
    custom["fullscreen_window"] = Widget_Button("p","Window","black","black",w(94),w(99),h(4),h(1),"grey","white","black","black")
    custom["fullscreen_fullscreen"] = Widget_Button("p","Fullscreen","black","black",w(92),w(99),h(4),h(1),"grey","white","black","black")
    

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def Update():
    global gameState

    # GameState Checks #
    
    if data["gameState"] == "Temp" and gameState.state != "Temp": gameState = gameState_Temp()
    if data["gameState"] == "Play" and gameState.state != "Play": gameState = gameState_Play()

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    gameState.Runtime()
    gameState.Render()
    gameState.Blit()

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    if window.fullscreen == True:
        custom["fullscreen_window"].blit()
        if custom["fullscreen_window"].click == True:
            window.change_size(False,((window.height*0.8)/13)*17,window.height*0.8)
            gameState.__init__()
            custom["fullscreen_fullscreen"].__init__("p","Fullscreen","black","black",w(92),w(99),h(4),h(1),"grey","white","black","black")

    elif window.fullscreen == False:
        custom["fullscreen_fullscreen"].blit()
        if custom["fullscreen_fullscreen"].click == True:
            window.change_size(True,0,0)
            gameState.__init__()
            custom["fullscreen_window"].__init__("p","Window","black","black",w(94),w(99),h(4),h(1),"grey","white","black","black")