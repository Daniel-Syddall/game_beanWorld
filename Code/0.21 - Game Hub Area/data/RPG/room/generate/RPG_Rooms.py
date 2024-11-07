from data.RPG.room.Builder import *

def roomBuild(self):

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # -= ROOM 0 =- #
    Room_Build(self,"room0",17,30,"","")
    Room_CreateWall(self,"room0",0,0,0,17,30,"rgba_0_0_0_255","na")
    Room_CreateWall(self,"room0",5,0,0,16,29,f"overlay_hue_0_0_0_-100","na")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # START LAND #
    Room_SetEdge(self,"room0",4,3,12,9,"0","0")
    Room_ChangeState(self,"room0","pass",4,3,12,9)

    # START PATHWAY #
    Room_SetEdge(self,"room0",7,9,9,29,"0","0")
    Room_ChangeState(self,"room0","pass",7,9,9,29)
    for i in range(3): Room_CreateSend(self,"room0",7+i,29,"room1",9+i,1)
    Room_CreateBlock(self,"room0",2,7,9,"tile_ground_0_downLeft","na")
    Room_CreateBlock(self,"room0",2,8,9,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room0",2,9,9,"tile_ground_0_downRight","na")
    Room_CreateBlock(self,"room0",2,7,29,"tile_ground_0_left","na")
    Room_CreateBlock(self,"room0",2,8,29,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room0",2,9,29,"tile_ground_0_right","na")
    Room_CreateBlock(self,"room0",1,7,29,"tile_edge_0_left","na")
    Room_CreateBlock(self,"room0",1,9,29,"tile_edge_0_right","na")

    # HUE MODIFICATIONS #
    Room_ChangeHue(self,"room0",0,0,0,16,29,"0_0_25_0")
    for i in range(2): 
        Room_ChangeHue(self,"room0",1+i,0,0,16,29,"-150_-150_150_0")
        Room_ChangeHue(self,"room0",1+i,7,27,9,27,"10_5_-15_0")
        Room_ChangeHue(self,"room0",1+i,7,28,9,28,"20_10_-30_0")
        Room_ChangeHue(self,"room0",1+i,7,29,9,29,"30_15_-45_0")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # -= ROOM 1 =- #
    Room_Build(self,"room1",31,28,"","")
    Room_CreateWall(self,"room1",0,0,0,30,29,"rgba_0_0_0_255","")
    Room_CreateWall(self,"room1",5,0,0,30,29,f"overlay_hue_0_0_0_-200","na")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # INTRO PATHWAY # 
    Room_SetEdge(self,"room1",9,0,11,9,"0","0")
    Room_ChangeState(self,"room1","pass",9,0,11,8)
    for i in range(3): Room_CreateSend(self,"room1",9+i,0,"room0",7+i,28)
    Room_CreateBlock(self,"room1",2,9,0,"tile_ground_0_left","na")
    Room_CreateBlock(self,"room1",2,10,0,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,11,0,"tile_ground_0_right","na")
    Room_CreateBlock(self,"room1",1,9,0,"tile_edge_0_left","na")
    Room_CreateBlock(self,"room1",1,11,0,"tile_edge_0_right","na")

    # MAIN LAND #
    Room_SetEdge(self,"room1",8,9,22,19,"0","0")
    Room_ChangeState(self,"room1","pass",8,9,22,19)
    Room_CreateBlock(self,"room1",2,9,9,"tile_ground_0_upLeft","na")
    Room_CreateBlock(self,"room1",2,10,9,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,11,9,"tile_ground_0_upRight","na")

    # LEFT PATHWAY #
    Room_SetEdge(self,"room1",0,13,8,15,"0","0")
    Room_ChangeState(self,"room1","pass",0,13,8,15)
    Room_CreateBlock(self,"room1",2,8,13,"tile_ground_0_upLeft","na")
    Room_CreateBlock(self,"room1",2,8,14,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,8,15,"tile_ground_0_downLeft","na")
    Room_CreateBlock(self,"room1",2,0,13,"tile_ground_0_up","na")
    Room_CreateBlock(self,"room1",2,0,14,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,0,15,"tile_ground_0_down","na")
    Room_CreateBlock(self,"room1",1,8,16,"tile_edge_0_left","na")
    Room_CreateBlock(self,"room1",1,0,13,"tile_edge_0_up","na")
    Room_CreateBlock(self,"room1",1,0,15,"tile_edge_0_down-0","na")
    Room_CreateBlock(self,"room1",1,0,16,"tile_edge_0_down-1","na")

    # RIGHT PATHWAY #
    Room_SetEdge(self,"room1",22,13,30,15,"0","0")
    Room_ChangeState(self,"room1","pass",22,13,30,15)
    Room_CreateBlock(self,"room1",2,22,13,"tile_ground_0_upRight","na")
    Room_CreateBlock(self,"room1",2,22,14,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,22,15,"tile_ground_0_downRight","na")
    Room_CreateBlock(self,"room1",2,30,13,"tile_ground_0_up","na")
    Room_CreateBlock(self,"room1",2,30,14,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,30,15,"tile_ground_0_down","na")
    Room_CreateBlock(self,"room1",1,22,16,"tile_edge_0_right","na")
    Room_CreateBlock(self,"room1",1,30,13,"tile_edge_0_up","na")
    Room_CreateBlock(self,"room1",1,30,15,"tile_edge_0_down-0","na")
    Room_CreateBlock(self,"room1",1,30,16,"tile_edge_0_down-1","na")

    # DECOR TILES #
    Room_CreateBlock(self,"room1",4,13,9,f"tile_decor_tree0","")
    Room_CreateBlock(self,"room1",3,13,9,f"shadow_default2_7_10","na")
    Room_CreateBlock(self,"room1",4,13,9,f"tile_decor_tree0","")
    Room_CreateBlock(self,"room1",3,13,9,f"shadow_default2_7_10","na")

    # HUE MODIFICATIONS #
    Room_ChangeHue(self,"room1",0,0,0,30,28,"25_0_-25_0")
    for i in range(2): 
        Room_ChangeHue(self,"room1",1+i,0,0,30,28,"50_0_-50_0")
        # INTRO PATHWAY HUE MOD #
        Room_ChangeHue(self,"room1",1+i,9,0,11,0,"-60_-30_60_0")
        Room_ChangeHue(self,"room1",1+i,9,1,11,1,"-40_-20_40_0")
        Room_ChangeHue(self,"room1",1+i,9,2,11,2,"-20_-10_20_0")
        # LEFT PATHWAY HUE MOD #
        Room_ChangeHue(self,"room1",1+i,0,13,0,16,"-60_-60_-60_0")
        Room_ChangeHue(self,"room1",1+i,1,13,1,16,"-40_-40_-40_0")
        Room_ChangeHue(self,"room1",1+i,2,13,2,16,"-20_-20_-20_0")
        # RIGHT PATHWAY HUE MOD #
        Room_ChangeHue(self,"room1",1+i,30,13,30,16,"60_-60_60_0")
        Room_ChangeHue(self,"room1",1+i,29,13,29,16,"40_-40_40_0")
        Room_ChangeHue(self,"room1",1+i,28,13,28,16,"20_-20_20_0")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #


    