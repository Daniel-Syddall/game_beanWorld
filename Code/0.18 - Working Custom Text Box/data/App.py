from asyncio.windows_events import NULL
import pygame
import math
pygame.init()

from data.RPG.Main import RPG
rpg = RPG()

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#===================================================================================================================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#=========================================================================- STATE ADDONS -==========================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#===================================================================================================================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

def GetLowAndHigh(StartX,StartY,EndX,EndY):
    if StartX <= EndX:
        LowX = StartX
        HighX = EndX
    elif EndY < StartX:
        LowX = EndY
        HighX = StartY
    if StartY <= EndY:
        LowY = StartY
        HighY = EndY
    elif EndY < StartY:
        LowY = EndY
        HighY = StartY
    return LowX,HighX,LowY,HighY

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

class Widget_Label:
    def __init__(self,app,textType,text,textColor,x1,x2,y1,y2,fill,outline):
        self.app = app
        self.textText = text
        self.textType = textType
        self.textColor = textColor
        if self.textType == "h1": self.text = self.app.h1(text,self.textColor)
        elif self.textType == "h2": self.text = self.app.h2(text,self.textColor)
        elif self.textType == "p": self.text = self.app.p(text,self.textColor)
        if fill == "": self.fill = NULL
        else: self.fill = self.app.color[fill]
        if outline == "": self.outline = NULL
        else: self.outline = self.app.color[outline]
        self.lowX,self.highX,self.lowY,self.highY = GetLowAndHigh(x1,y1,x2,y2)
        self.width = self.highX - self.lowX
        self.height = self.highY - self.lowY
        self.textX = math.floor((self.width-(self.text.get_width()))/2)+self.lowX
        self.textY = math.floor((self.height-(self.text.get_height()))/2)+self.lowY

    def update_text(self,text):
        self.textText = text
        if self.textType == "h1": self.text = self.app.h1(text,self.textColor)
        elif self.textType == "h2": self.text = self.app.h2(text,self.textColor)
        elif self.textType == "p": self.text = self.app.p(text,self.textColor)
        self.textX = math.floor((self.width-(self.text.get_width()))/2)+self.lowX
        self.textY = math.floor((self.height-(self.text.get_height()))/2)+self.lowY

    def update_dimentions(self,x1,x2,y1,y2):
        self.lowX,self.highX,self.lowY,self.highY = GetLowAndHigh(x1,y1,x2,y2)
        self.width = self.highX - self.lowX
        self.height = self.highY - self.lowY
        self.update_text(self.textText)

    def blit(self):
        if self.fill != NULL: pygame.draw.rect(self.app.window,self.fill,(self.lowX,self.lowY,self.width,self.height),0)
        if self.outline != NULL: pygame.draw.rect(self.app.window,self.outline,(self.lowX,self.lowY,self.width,self.height),2)
        self.app.window.blit(self.text,(self.textX,self.textY))

class Widget_Button:
    def __init__(self,app,textType,text,textColor1,textColor2,x1,x2,y1,y2,fill1,fill2,outline1,outline2):
        self.app = app
        self.click = False
        self.miss = False
        self.textText = text
        self.textType = textType
        self.textColor1 = textColor1
        self.textColor2 = textColor2
        if self.textType == "h1": 
            self.text1 = self.app.h1(text,self.textColor1)
            self.text2 = self.app.h1(text,self.textColor2)
        elif self.textType == "h2": 
            self.text1 = self.app.h2(text,self.textColor1)
            self.text2 = self.app.h2(text,self.textColor2)
        elif self.textType == "p": 
            self.text1 = self.app.p(text,self.textColor1)
            self.text2 = self.app.p(text,self.textColor2)
        self.fill1 = self.app.color[fill1]
        self.fill2 = self.app.color[fill2]
        self.outline1 = self.app.color[outline1]
        self.outline2 = self.app.color[outline2]
        self.lowX,self.highX,self.lowY,self.highY = GetLowAndHigh(x1,y1,x2,y2)
        self.width = self.highX - self.lowX
        self.height = self.highY - self.lowY
        self.textX = math.floor((self.width-(self.text1.get_width()))/2)+self.lowX
        self.textY = math.floor((self.height-(self.text2.get_height()))/2)+self.lowY

    def update_text(self,text):
        self.textText = text
        if self.textType == "h1": 
            self.text1 = self.app.h1(text,self.textColor1)
            self.text2 = self.app.h1(text,self.textColor2)
        elif self.textType == "h2": 
            self.text1 = self.app.h2(text,self.textColor1)
            self.text2 = self.app.h2(text,self.textColor2)
        elif self.textType == "p": 
            self.text1 = self.app.p(text,self.textColor1)
            self.text2 = self.app.p(text,self.textColor2)
        self.textX = math.floor((self.width-(self.text1.get_width()))/2)+self.lowX
        self.textY = math.floor((self.height-(self.text1.get_height()))/2)+self.lowY

    def update_dimentions(self,x1,x2,y1,y2):
        self.lowX,self.highX,self.lowY,self.highY = GetLowAndHigh(x1,y1,x2,y2)
        self.width = self.highX - self.lowX
        self.height = self.highY - self.lowY
        self.update_text(self.textText)

    def blit(self):
        mouse = self.app.controller_input["mouse"]
        click = self.app.controller_input["click"]
        if self.lowX <= mouse[0] <= self.highX and self.lowY <= mouse[1] <= self.highY:
            self.miss = False
            if click == True: self.click = True
            else: self.click = False
            pygame.draw.rect(self.app.window,self.fill2,(self.lowX,self.lowY,self.width,self.height),0)
            pygame.draw.rect(self.app.window,self.outline2,(self.lowX,self.lowY,self.width,self.height),2)
            self.app.window.blit(self.text2,(self.textX,self.textY))
        else:
            self.click = False
            if click == True: self.miss = True
            else: self.miss = False
            pygame.draw.rect(self.app.window,self.fill1,(self.lowX,self.lowY,self.width,self.height),0)
            pygame.draw.rect(self.app.window,self.outline1,(self.lowX,self.lowY,self.width,self.height),2)
            self.app.window.blit(self.text1,(self.textX,self.textY))

class Widget_Type:
    def __init__(self,app,textType,text,textColor1,textColor2,x1,x2,y1,y2,fill1,fill2,outline1,outline2):
        self.text = text
        self.select = False
        self.enter = False
        self.base = Widget_Button(app,textType,self.text,textColor1,textColor2,x1,x2,y1,y2,fill1,fill2,outline1,outline2)

    def update_text(self,text): self.base.update_text(text)
    def update_dimentions(self,x1,x2,y1,y2): self.base.update_dimentions(x1,x2,y1,y2)

    def blit(self):
        self.base.blit()
        if self.base.click == True: self.select = True
        elif self.base.miss == True: self.select = False
        if self.select == True: 
            if self.base.app.controller_input["enter"] == True or self.base.miss == True:
                self.select = False
                self.enter = True
            elif self.base.app.controller_input["backspace"] == True: self.text = self.text[:-1]
            else: self.text = self.text + self.base.app.controller_input["type"]
            self.base.update_text(self.text)
            
def blits(*argv):
    for arg in argv: 
        arg.blit()

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#===================================================================================================================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#========================================================================- STATE CLASSES -==========================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#===================================================================================================================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

class Glob:

    def __init__(self,app):
        self.app = app
        self.button = Widget_Button(app,"p","{  }","grey","white",app.w(97),app.w(99),app.h(3),app.h(1),"black","grey","black","grey")

    def runtime(self):
        if self.button.click == True:
            self.button.click = False

            if self.app.fullscreen == True: self.app.window_changeSize(False,((self.app.height*0.8)/13)*17,self.app.height*0.8)
            else: self.app.window_changeSize(True,0,0)

            self.app.state = Map(self.app)
            self.app.glob = Glob(self.app)

    def blit(self):
        self.button.blit()

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

class Temp:

    def __init__(self,app):
        self.app = app
        app.fps = 30
        self.state = "Temp"
        self.count = 0
        app.window.fill(app.color["white"])
        self.label = {}
        self.label["example"] = Widget_Label(app,"h1","Example","black",app.w(25),app.w(75),app.h(5),app.h(45),"","")
        self.label["example"].blit()
        self.button = {}
        self.button["example"] = Widget_Button(app,"h2","Exampe","black","white",app.w(25),app.w(75),app.h(55),app.h(95),"white","grey","black","black")
        self.button["quit"] = Widget_Button(app,"p","Quit","black","black",app.w(90),app.w(99),app.h(95),app.h(99),"white","white","black","grey")
        self.type = {}
        self.type["example"] = Widget_Type(app,"p","TYPE HERE","black","black",app.w(3),app.w(20),app.h(80),app.h(97),"white","white","black","grey")

    def runtime(self):
        if self.button["quit"].click == True: 
            pygame.quit()
            quit()
        self.count += 1
        self.button["quit"].update_text("Quit : "+str(self.count))

    def blit(self): blits(self.button["example"],self.button["quit"],self.type["example"])

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

class Map:

    def __init__(self,app):
        self.app = app
        app.fps = 60
        self.state = "Map"
        rpg.BlitBorder(app.window,app.w(0),app.h(0),app.width,app.height)

    def runtime(self):
        rpg.Run()

    def blit(self):
        temp_surfaceX,temp_surfaceY,temp_surface_Width,temp_surface_height = rpg.Blit(self.app.window,math.floor((self.app.w(100)-((self.app.height/13)*17))/2),self.app.h(0),(self.app.height/13)*17,self.app.height)
        #if rpg.textBox != "": 
        #    if rpg.asset["character"][rpg.textBox_character].get_width() >= rpg.asset["character"][rpg.textBox_character].get_height(): self.app.window.blit(pygame.transform.scale(rpg.asset["character"][rpg.textBox_character],((self.app.width/12)*1,(((self.app.width/12)*1)/rpg.asset["character"][rpg.textBox_character].get_width())*rpg.asset["character"][rpg.textBox_character].get_height())),(temp_surfaceX+self.app.w(3),temp_surfaceY+self.app.h(77)))
        #    elif rpg.asset["character"][rpg.textBox_character].get_height() > rpg.asset["character"][rpg.textBox_character].get_width(): self.app.window.blit(pygame.transform.scale(rpg.asset["character"][rpg.textBox_character],((((self.app.height/5))/rpg.asset["character"][rpg.textBox_character].get_height())*rpg.asset["character"][rpg.textBox_character].get_width(),(self.app.height/5))),(temp_surfaceX+self.app.w(3),temp_surfaceY+self.app.h(77)))

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#===================================================================================================================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#==========================================================================- APP CLASS -============================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#===================================================================================================================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

class App:

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def __init__(self):
        self.window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.fullscreen = True
        self.width = self.window.get_width()
        self.height = self.window.get_height()

        pygame.display.set_caption("BEAN WORLD")
        pygame.display.set_icon(rpg.asset["tile"]["decor_tree0"])

        self.fps = 30
        self.glob = NULL
        self.state = NULL
        self.state_name = "Map"
        self.controller_input = {"click":False,"mouse":False,"enter":False,"backspace":False,"type":""}

        self.color = {"white":(255,255,255),"grey":(150,150,150),"black":(0,0,0)}
        self.asset = {}

        pygame.init()
        self.fontSlot = 2
        self.fontArray = pygame.font.get_fonts()
        self.fontScale = math.floor(self.width/180)
        self.H1 = pygame.font.SysFont(self.fontArray[self.fontSlot],4*self.fontScale)
        self.H2 = pygame.font.SysFont(self.fontArray[self.fontSlot],3*self.fontScale)
        self.P = pygame.font.SysFont(self.fontArray[self.fontSlot],2*self.fontScale)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def window_changeSize(self,fullscreen,width,height):
        if fullscreen == True: 
            self.surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.fullscreen = True
        if fullscreen == False: 
            self.surface = pygame.display.set_mode((width,height))
            self.fullscreen = False

        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

        self.fontScale = math.floor(self.width/180)
        self.H1 = pygame.font.SysFont(self.fontArray[self.fontSlot],4*self.fontScale)
        self.H2 = pygame.font.SysFont(self.fontArray[self.fontSlot],3*self.fontScale)
        self.P = pygame.font.SysFont(self.fontArray[self.fontSlot],2*self.fontScale)


# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def w(self,i): return self.width * (i/100)
    def h(self,i): return self.height * (i/100)

    def font(self,type,text,Color): return type.render(text,True,self.color[Color])
    def h1(self,text,color): return self.font(self.H1,text,color)
    def h2(self,text,color): return self.font(self.H2,text,color)
    def p(self,text,color): return self.font(self.P,text,color)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def controller(self):
        self.controller_input["type"] = ""
        self.controller_input["mouse"] = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP: self.controller_input["click"] = False
            if event.type == pygame.MOUSEBUTTONDOWN: self.controller_input["click"] = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: self.controller_input["enter"] = True
                if event.key == pygame.K_BACKSPACE: self.controller_input["backspace"] = True
                else: self.controller_input["type"] = event.unicode
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN: self.controller_input["enter"] = False
                if event.key == pygame.K_BACKSPACE: self.controller_input["backspace"] = False

            rpg.Controller(event,self.controller_input["type"])

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def update(self):

        if self.glob == NULL: self.glob = Glob(self)
        if self.state_name == "Map" and self.state == NULL: self.state = Map(self)
        #elif self.state_name == "Temp" and self.state.state != "Temp": self.state = Temp(self)

        self.state.runtime()
        self.state.blit()

        self.glob.blit()
        self.glob.runtime()

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def frameDelay(self): pygame.time.delay(math.floor(1000/self.fps))

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    def run(self):
        self.controller()
        self.update()

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#===================================================================================================================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#===================================================================================================================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #
#===================================================================================================================================================================================#
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #