from Imports.Data import *
pygame.init()

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
            if event.key == pygame.K_w: controller["up"][0] = True
            if event.key == pygame.K_UP: controller["up"][1] = True
            if event.key == pygame.K_s: controller["down"][0] = True
            if event.key == pygame.K_DOWN: controller["down"][1] = True
            if event.key == pygame.K_a: controller["left"][0] = True
            if event.key == pygame.K_LEFT: controller["left"][1] = True
            if event.key == pygame.K_d: controller["right"][0] = True
            if event.key == pygame.K_RIGHT: controller["right"][1] = True
            if event.key == pygame.K_LSHIFT: controller["sprint"] = True
            if event.key == pygame.K_RETURN: controller["enter"] = True
            elif event.key == pygame.K_BACKSPACE: controller["backspace"] = True
            else: controller["type"] = event.unicode

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: controller["up"][0] = False
            if event.key == pygame.K_UP: controller["up"][1] = False
            if event.key == pygame.K_s: controller["down"][0] = False
            if event.key == pygame.K_DOWN: controller["down"][1] = False
            if event.key == pygame.K_a: controller["left"][0] = False
            if event.key == pygame.K_LEFT: controller["left"][1] = False
            if event.key == pygame.K_d: controller["right"][0] = False
            if event.key == pygame.K_RIGHT: controller["right"][1] = False
            if event.key == pygame.K_LSHIFT: controller["sprint"] = False
            if event.key == pygame.K_RETURN: controller["enter"] = False
            if event.key == pygame.K_BACKSPACE: controller["backspace"] = False