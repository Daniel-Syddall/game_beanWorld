from Imports.MainData import *

class Widget_Label:
    def __init__(self,textType,text,textColor,x1,x2,y1,y2,box,fill,outline):
        self.textType = textType
        self.textColor = textColor
        if self.textType == "h1": self.text = h1(text,self.textColor)
        elif self.textType == "h2": self.text = h2(text,self.textColor)
        elif self.textType == "p": self.text = p(text,self.textColor)
        self.box = box
        self.fill = color[fill]
        self.outline = color[outline]
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
        self.textX = math.floor((self.width-(self.text.get_width()))/2)+self.lowX
        self.textY = math.floor((self.height-(self.text.get_height()))/2)+self.lowY

    def update_text(self,text):
        if self.textType == "h1": self.text = h1(text,self.textColor)
        elif self.textType == "h2": self.text = h2(text,self.textColor)
        elif self.textType == "p": self.text = p(text,self.textColor)
        self.textX = math.floor((self.width-(self.text.get_width()))/2)+self.lowX
        self.textY = math.floor((self.height-(self.text.get_height()))/2)+self.lowY

    def blit(self):
        if self.box == True:
            pygame.draw.rect(window.surface,self.fill,(self.lowX,self.lowY,self.width,self.height),0)
            pygame.draw.rect(window.surface,self.outline,(self.lowX,self.lowY,self.width,self.height),2)
        window.surface.blit(self.text,(self.textX,self.textY))