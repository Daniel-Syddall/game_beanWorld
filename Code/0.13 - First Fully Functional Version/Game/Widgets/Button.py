from Imports.MainData import *

class Widget_Button:
    def __init__(self,textType,text,textColor1,textColor2,x1,x2,y1,y2,fill1,fill2,outline1,outline2):
        self.click = False
        self.miss = False
        self.textType = textType
        self.textColor1 = textColor1
        self.textColor2 = textColor2
        if self.textType == "h1": self.text1,self.text2 = h1(text,self.textColor1),h1(text,self.textColor2)
        elif self.textType == "h2": self.text1,self.text2 = h2(text,self.textColor1),h2(text,self.textColor2)
        elif self.textType == "p": self.text1,self.text2 = p(text,self.textColor1),p(text,self.textColor2)
        self.fill1 = color[fill1]
        self.fill2 = color[fill2]
        self.outline1 = color[outline1]
        self.outline2 = color[outline2]
        if x1 <= x2:
            self.lowX = x1
            self.highX = x2
        elif x2 < x1:
            self.lowX = x2
            self.highX = x1
        if y1 <= y2:
            self.lowY = y1
            self.highY = y2
        elif y2 < y1:
            self.lowY = y2
            self.highY = y1
        self.width = self.highX - self.lowX
        self.height = self.highY - self.lowY
        self.textX = math.floor((self.width-(self.text1.get_width()))/2)+self.lowX
        self.textY = math.floor((self.height-(self.text2.get_height()))/2)+self.lowY

    def update_text(self,text):
        if self.textType == "h1": self.text1,self.text2 = h1(text,self.textColor1),h1(text,self.textColor2)
        elif self.textType == "h2": self.text1,self.text2 = h2(text,self.textColor1),h2(text,self.textColor2)
        elif self.textType == "p": self.text1,self.text2 = p(text,self.textColor1),p(text,self.textColor2)
        self.textX = math.floor((self.width-(self.text1.get_width()))/2)+self.lowX
        self.textY = math.floor((self.height-(self.text1.get_height()))/2)+self.lowY

    def update_dimentions(self,x1,x2,y1,y2):
        if x1 <= x2:
            self.lowX = x1
            self.highX = x2
        elif x2 < x1:
            self.lowX = x2
            self.highX = x1
        if y1 <= y2:
            self.lowY = y1
            self.highY = y2
        elif y2 < y1:
            self.lowY = y2
            self.highY = y1
        self.width = self.highX - self.lowX
        self.height = self.highY - self.lowY
        self.update_text(self.text1,self.text2)

    def blit(self):
        if self.lowX <= controller["mouse"][0] <= self.highX and self.lowY <= controller["mouse"][1] <= self.highY:
            if controller["click"] == True: self.click = True
            else: self.click = False
            pygame.draw.rect(window.surface,self.fill2,(self.lowX,self.lowY,self.width,self.height),0)
            pygame.draw.rect(window.surface,self.outline2,(self.lowX,self.lowY,self.width,self.height),2)
            window.surface.blit(self.text2,(self.textX,self.textY))
        else:
            if controller["click"] == True: self.miss = True
            else: self.miss = False
            pygame.draw.rect(window.surface,self.fill1,(self.lowX,self.lowY,self.width,self.height),0)
            pygame.draw.rect(window.surface,self.outline1,(self.lowX,self.lowY,self.width,self.height),2)
            window.surface.blit(self.text1,(self.textX,self.textY))