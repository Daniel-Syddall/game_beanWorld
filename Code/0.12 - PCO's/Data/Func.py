from Data.Const import *
from Data.Vars import *
from Data.Assets import *

def w(i): return window.width * (i/100)
def h(i): return window.height * (i/100)

def font(type,text,Color): return type.render(text,True,color[Color])
def h1(text,color): return font(window.H1,text,color)
def h2(text,color): return font(window.H2,text,color)
def p(text,color): return font(window.P,text,color)

def round(i):
    temp = i * 10
    return math.floor(temp) / 10