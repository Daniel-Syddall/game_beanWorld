from Imports.Data import *
from Display.Widgets.Player import *

def Widgets_Map():
    global window,map

    def PrintLayer(Layer):
        global map
        for y in range(14):
            for x in range(18):
                tile = room[data["map"]["room"]][f"{str(Layer)}-{str(x)}-{str(y)}"]
                tile = tile.split("-")
                if tile[0] == "color":
                    pygame.draw.rect(map,color[tile[1]],((x*display["map"]["tileSize"]),(y*display["map"]["tileSize"]),display["map"]["tileSize"],display["map"]["tileSize"]))
                elif tile[0] == "asset":
                    display["map"]["main"].blit(asset[tile[1]],((x*display["map"]["tileSize"]),(y*display["map"]["tileSize"])))

    PrintLayer(0)
    PrintLayer(1)
    Widgets_Player()
    PrintLayer(2)
    PrintLayer(3)

    window.blit(pygame.transform.scale(map,((display["map"]["width"]*display["map"]["tileSize"])*display["map"]["scale"],(display["map"]["height"]*display["map"]["tileSize"])*display["map"]["scale"])),(data["map"]["offsetX"]*display["map"]["scale"],data["map"]["offsetY"]*display["map"]["scale"]))
    #map = pygame.Surface(((display["map"]["width"]*display["map"]["tileSize"]),(display["map"]["height"]*display["map"]["tileSize"])))