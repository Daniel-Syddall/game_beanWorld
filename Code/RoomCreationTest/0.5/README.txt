-= Guide on how to use the Pygame Template =-

    To create a new Game State, please go to ./Game/Main/Temp/Temp.py and follow the steps featured on line 9 - 35

    data["dataInit"] = (Bool) <-- Indicates if the Script.py file has loaded all the files within ./Data
    data["init"] = (Bool) <-- Indicates if the Script.py file has ran through all existing files within the program atleast once
    data["GameState"] = (Str) <-- Indicates the name of the Game State that is currently being ran

    controller["mouse"] = [(Int),(Int)] <-- Indicates the current position of the users curser on the screen
    controller["click"] = (Bool) <-- Indicates if the player has pressed down the mouse1 button in this instant
    controller["backspace"] = (Bool) <-- Indicates if the player has pressed down the backspace button in this instant
    controller["type"] = (Str) <-- Indicates what keys the player hass pressed down on in this instant

    color["Name Of Color"] = [(Int),(Int),(Int)] <-- Stores 3 Int Values that forms the RGB value that the color name reperesents

    custom = {Dict} <-- Stores Global Variables that exist across all game states (Seperate Global Variables can be created within ./Data/Vars)