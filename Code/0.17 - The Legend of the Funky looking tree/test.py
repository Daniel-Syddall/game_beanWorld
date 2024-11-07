from ast import Pass
from math import floor as round
import pygame

local = "./data/RPG/"
typeTypeArray = ["_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
typeImage = {}

textBoxWidth = round((16*17)*0.9)
averageWidth = 0
for i in range(len(typeTypeArray)):
    typeImage.update({typeTypeArray[i] : pygame.image.load(f"{local}/assets/type/PixelSans/{typeTypeArray[i]}.png")})
    averageWidth += typeImage[typeTypeArray[i]].get_width() + 1
averageWidth = round(averageWidth/len(typeTypeArray))
averageCharacterCountPerLine = round(textBoxWidth/averageWidth)

print(f"width of Text box : {textBoxWidth}")
print(f"average Lower Case Character Width : {averageWidth}")
print(f"average Lower Case Character Count per Line : {averageCharacterCountPerLine}")
print()

testText = "bean dude :quickly bean man you gotta get them balls "

print(f"Test Text : '{testText}'")

line = [""]
lineWidth = [0]
currentLine = 0
word = ""
wordWidth = 0

for i in range(len(testText)):
    #Gets Next Character
    char = testText[0]
    testText = testText[1:]

    #if Character = space then attach word + word width to current Line and reset the word
    if char == " ": 
        line[currentLine] += word + " "
        lineWidth[currentLine] += wordWidth + typeImage["_"].get_width()
        word = ""
        wordWidth = 0

    #Checks if needs to move to new Line (Collons indicate an instant change of line, usually utilised to indicate the end of a characters name)
    elif char == ":":
        currentLine += 1
        line.append("")
        lineWidth.append(0)
    elif typeImage[char].get_width() + wordWidth + lineWidth[currentLine] > textBoxWidth:
        currentLine += 1
        line.append("")
        lineWidth.append(0)

    #else attach the character + character width to the end of the current word
    if char != " " and char != ":":
        word += char
        wordWidth += typeImage[char].get_width()

for i in range(len(line)):
    print(f"line {i} : {line[i]}")
    print(f"Number of characters on line {i} : {len(line[i])}")

customAssets = {"roomA":[["balls"]],"roomB":[["nuts"]]}

print(customAssets["roomA"][0][0])
print(customAssets["roomB"][0][0])