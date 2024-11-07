import pygame
pygame.init()
import math
from random import randint as random
from asyncio.windows_events import NULL

class Window:
    def __init__(self):
        self.fullscreen = True
        self.surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

        self.fontSlot = 2
        self.fontArray = pygame.font.get_fonts()
        self.fontScale = math.floor(self.width/180)
        self.H1 = pygame.font.SysFont(self.fontArray[self.fontSlot],4*self.fontScale)
        self.H2 = pygame.font.SysFont(self.fontArray[self.fontSlot],3*self.fontScale)
        self.P = pygame.font.SysFont(self.fontArray[self.fontSlot],2*self.fontScale)


    def change_size(self,fullscreen,width,height):
        if fullscreen == True: 
            self.surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.fullscreen = True
        if fullscreen == False: 
            self.surface = pygame.display.set_mode((width,height),pygame.RESIZABLE)
            self.fullscreen = False

        self.width = self.surface.get_width()
        self.height = self.surface.get_height()

        self.fontScale = math.floor(self.width/180)
        self.H1 = pygame.font.SysFont(self.fontArray[self.fontSlot],4*self.fontScale)
        self.H2 = pygame.font.SysFont(self.fontArray[self.fontSlot],3*self.fontScale)
        self.P = pygame.font.SysFont(self.fontArray[self.fontSlot],2*self.fontScale)

window = Window()