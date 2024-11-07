from Data.Variables import *
from Data.Assets import *

def Room_CreateSpawn(SpawnRoom,SpawnID,SpawnX,SpawnY):

    room[SpawnRoom][f"spawn_{str(SpawnID)}_X"] = SpawnX
    room[SpawnRoom][f"spawn_{str(SpawnID)}_Y"] = SpawnY