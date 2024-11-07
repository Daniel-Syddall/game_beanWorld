from Imports.Data import *

def Grid_OffsetArrayDisplacement(Displacement):

    ArrayDisplacementStart = -8

    for _ in range(Displacement):
        ArrayDisplacementStart -= 1
        if ArrayDisplacementStart == -17: ArrayDisplacementStart = -1

    DisplacementArray = []
    for _ in range(16):
        ArrayDisplacementStart -= 1
        if ArrayDisplacementStart == -17: ArrayDisplacementStart = -1
        DisplacementArray.append(ArrayDisplacementStart)

    return DisplacementArray