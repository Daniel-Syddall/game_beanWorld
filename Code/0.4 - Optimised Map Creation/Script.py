from Imports.Data import *
data["varInit"] = True
from Game.Update import *
Update()
data["init"] = True

def Script():

    while True:
        pygame.time.delay(math.floor(1000/60))
        Controller()
        Update()