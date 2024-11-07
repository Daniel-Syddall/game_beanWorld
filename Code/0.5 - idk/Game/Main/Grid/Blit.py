from Imports.Data import *
from Imports.Widgets import *

def Grid_Blit():

    def Grid_Blit_RenderLayer(l):
        for x in range(display["grid"]["width"]+1):
            for y in range(display["grid"]["height"]+1):
                tile = grid[f"{str(l)}_{str(x)}_{str(y)}"]
                tile = tile.split("_")
                if tile[0] == "color":
                    pygame.draw.rect(Grid,color[tile[1]],((x*display["grid"]["tileSize"])+grid["offsetX"],(y*display["grid"]["tileSize"])+grid["offsetY"],display["grid"]["tileSize"],display["grid"]["tileSize"]),0)
                    #pygame.draw.rect(Grid,color["black"],((x*display["grid"]["tileSize"])+grid["offsetX"],(y*display["grid"]["tileSize"])+grid["offsetY"],display["grid"]["tileSize"],display["grid"]["tileSize"]),1)
                elif tile[0] == "asset":
                    if tile[1] == "merge":
                        Grid.blit(asset[tile[1]][f"{tile[2]}_{tile[3]}_{tile[4]}"],((x*display["grid"]["tileSize"])+grid["offsetX"],(y*display["grid"]["tileSize"])+grid["offsetY"]))
    
    def Grid_Blit_RenderPlayer():
        sprite = player["sprite"]
        sprite = sprite.split("_")
        if sprite[0] == "color":
            pygame.draw.rect(Grid,color[sprite[1]+"_"+player["spriteDirection"]+"_"+str(player["spriteState"])],((player["gridX"])-(math.floor(player["spriteWidth"]/2)),(player["gridY"])-player["spriteHeight"],player["spriteWidth"],player["spriteHeight"]))
        elif sprite[0] == "asset":
            Grid.blit(asset[sprite[1]][sprite[2]+"_"+player["spriteDirection"]+"_"+str(player["spriteState"])],(((player["gridX"])-(math.floor(player["spriteWidth"]/2))),(player["gridY"]-player["spriteHeight"])))

    Grid_Blit_RenderLayer(0)
    Grid_Blit_RenderLayer(1)
    Grid_Blit_RenderLayer(2)
    Grid_Blit_RenderPlayer()
    Grid_Blit_RenderLayer(3)
    Grid_Blit_RenderLayer(4)

    Window.blit(pygame.transform.scale(Grid,(((display["grid"]["width"])*display["grid"]["tileSize"])*display["grid"]["scale"],((display["grid"]["height"])*display["grid"]["tileSize"])*display["grid"]["scale"])),(0,0))