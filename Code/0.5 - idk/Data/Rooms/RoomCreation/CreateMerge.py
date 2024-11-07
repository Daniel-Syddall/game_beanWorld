from Data.Variables import *
from Data.Assets import *

def Room_CreateMerge(RoomName,MergeName,layer,startX,startY):
    merge_Found = False
    merge_Count = 0
    while merge_Found == False:
        if mergeNameArray[merge_Count][0] == MergeName: merge_Found = True
        else: merge_Count += 1
    for x in range(mergeNameArray[merge_Count][1]):
        for y in range(mergeNameArray[merge_Count][2]):
            room[RoomName][f"{str(layer)}_{str(x+startX)}_{str(y+startY)}"] = f"asset_merge_{MergeName}_{str(x)}_{str(y)}"