from Imports.Data import *

def Controller():

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            data["controller"]["click"] == False
        if event.type == pygame.MOUSEBUTTONDOWN:
            data["controller"]["click"] == True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.KSCAN_W:
                data["controller"]["up0"] = True
            if event.key == pygame.K_UP:
                data["controller"]["up1"] = True
            if event.key == pygame.KSCAN_S:
                data["controller"]["down0"] = True
            if event.key == pygame.K_DOWN:
                data["controller"]["down1"] = True
            if event.key == pygame.KSCAN_A:
                data["controller"]["left0"] = True
            if event.key == pygame.K_LEFT:
                data["controller"]["left1"] = True
            if event.key == pygame.KSCAN_D:
                data["controller"]["right0"] = True
            if event.key == pygame.K_RIGHT:
                data["controller"]["right1"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.KSCAN_W:
                data["controller"]["up0"] = False
            if event.key == pygame.K_UP:
                data["controller"]["up1"] = False
            if event.key == pygame.KSCAN_S:
                data["controller"]["down0"] = False
            if event.key == pygame.K_DOWN:
                data["controller"]["down1"] = False
            if event.key == pygame.KSCAN_A:
                data["controller"]["left0"] = False
            if event.key == pygame.K_LEFT:
                data["controller"]["left1"] = False
            if event.key == pygame.KSCAN_D:
                data["controller"]["right0"] = False
            if event.key == pygame.K_RIGHT:
                data["controller"]["right1"] = False

    data["controller"]["mouse"] = pygame.mouse.get_pos()