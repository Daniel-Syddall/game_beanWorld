
import pygame

local = "./**IMAGE FILE INSIDE LOCAL**"

surface = pygame.display.set_mode((600,600))

imageThingy = pygame.image.load(f"{local}/assets/opening.png")
surfaceThingy = pygame.Surface(imageThingy.get_width()+150,imageThingy.get_height()+150)
surfaceThingy.blit(imageThingy,(0,0))

while True():
    surface.blit(pygame.transform.scale(surfaceThingy,(surface.get_width(),surface.get_height())),(0,0))
    surface.update()
    pygame.surface.update()

