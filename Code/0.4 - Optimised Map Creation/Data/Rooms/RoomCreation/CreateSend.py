from Data.Variables import *
from Data.Assets import *

def Room_CreateSend(SendRoom,SendID,SendX,SendY,SendFill,SpawnRoom,SpawnID):

    room[SendRoom][f"0_{str(SendX)}_{str(SendY)}"] = SendFill
    room[SendRoom][f"state_{str(SendX)}_{str(SendY)}"] = "send"
    room[SendRoom][f"send_{str(SendID)}_X"] = SendX
    room[SendRoom][f"send_{str(SendID)}_Y"] = SendY
    room[SendRoom][f"send_{str(SendID)}_room"] = SpawnRoom
    room[SendRoom][f"send_{str(SendID)}_spawn"] = SpawnID