from Imports.MainData import *

def Controller():

    controller["type"] = ""
    controller["mouse"] = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONUP: controller["click"] = False
        if event.type == pygame.MOUSEBUTTONDOWN: controller["click"] = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE: controller["backspace"] = True
            else: controller["type"] = event.unicode
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE: controller["backspace"] = False

        rpg.Controller(event)