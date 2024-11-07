from asyncio.windows_events import NULL
import pygame
import math
import array
import time
from Script import data_init

if data_init == False:
    from Data.Main import *
    from Data.Assets import *
    from Data.Rooms._0 import *
    from Data.Rooms._1 import *
else:
    import Data.Main
    import Data.Assets
    import Data.Rooms._0
    import Data.Rooms._1


