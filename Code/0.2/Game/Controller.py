from Imports.Data import *

def Controller():

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            controller["click"] == False
        if event.type == pygame.MOUSEBUTTONDOWN:
            controller["click"] == True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.KSCAN_W:
                controller["up"][0] = True
            if event.key == pygame.K_UP:
                controller["up"][1] = True
            if event.key == pygame.KSCAN_S:
                controller["down"][0] = True
            if event.key == pygame.K_DOWN:
                controller["down"][1] = True
            if event.key == pygame.KSCAN_A:
                controller["left"][0] = True
            if event.key == pygame.K_LEFT:
                controller["left"][1] = True
            if event.key == pygame.KSCAN_D:
                controller["right"][0] = True
            if event.key == pygame.K_RIGHT:
                controller["right"][1] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.KSCAN_W:
                controller["up"][0] = False
            if event.key == pygame.K_UP:
                controller["up"][1] = False
            if event.key == pygame.KSCAN_S:
                controller["down"][0] = False
            if event.key == pygame.K_DOWN:
                controller["down"][1] = False
            if event.key == pygame.KSCAN_A:
                controller["left"][0] = False
            if event.key == pygame.K_LEFT:
                controller["left"][1] = False
            if event.key == pygame.KSCAN_D:
                controller["right"][0] = False
            if event.key == pygame.K_RIGHT:
                controller["right"][1] = False

    controller["mouse"] = pygame.mouse.get_pos()