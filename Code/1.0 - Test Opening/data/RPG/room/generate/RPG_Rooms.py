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
        Room_ChangeHue(self,"room0",1+i,0,0,16,29,"-40_-40_40_0")
        Room_ChangeHue(self,"room0",1+i,7,27,9,27,"11_7_-11_0")
        Room_ChangeHue(self,"room0",1+i,7,28,9,28,"22_14_-22_0")
        Room_ChangeHue(self,"room0",1+i,7,29,9,29,"33_21_-33_0")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # -= ROOM 1 =- #
    Room_Build(self,"room1",27,27,"","")
    Room_CreateWall(self,"room1",0,0,0,26,26,"rgba_0_0_0_255","")
    Room_CreateWall(self,"room1",5,0,0,26,26,f"overlay_hue_0_0_0_-200","na")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # INTRO PATHWAY # 
    Room_SetEdge(self,"room1",9,0,11,9,"0","0")
    Room_ChangeState(self,"room1","pass",9,0,11,9)
    for i in range(3): Room_CreateSend(self,"room1",9+i,0,"room0",7+i,28)
    Room_CreateBlock(self,"room1",2,9,0,"tile_ground_0_left","na")
    Room_CreateBlock(self,"room1",2,10,0,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,11,0,"tile_ground_0_right","na")
    Room_CreateBlock(self,"room1",1,9,0,"tile_edge_0_left","na")
    Room_CreateBlock(self,"room1",1,11,0,"tile_edge_0_right","na")

    # MAIN LAND #
    Room_SetEdge(self,"room1",8,9,18,19,"0","0")
    Room_ChangeState(self,"room1","pass",8,9,18,19)
    Room_CreateBlock(self,"room1",2,9,9,"tile_ground_0_upLeft","na")
    Room_CreateBlock(self,"room1",2,10,9,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,11,9,"tile_ground_0_upRight","na")

    # LEFT PATHWAY #
    Room_SetEdge(self,"room1",0,13,8,15,"0","0")
    Room_ChangeState(self,"room1","pass",0,13,8,15)
    for i in range(3): Room_CreateSend(self,"room1",0,13+i,"room1B0",59,49+i)
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
    Room_SetEdge(self,"room1",18,13,26,15,"0","0")
    Room_ChangeState(self,"room1","pass",18,13,26,15)
    Room_CreateBlock(self,"room1",2,18,13,"tile_ground_0_upRight","na")
    Room_CreateBlock(self,"room1",2,18,14,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,18,15,"tile_ground_0_downRight","na")
    Room_CreateBlock(self,"room1",2,26,13,"tile_ground_0_up","na")
    Room_CreateBlock(self,"room1",2,26,14,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,26,15,"tile_ground_0_down","na")
    Room_CreateBlock(self,"room1",1,18,16,"tile_edge_0_right","na")
    Room_CreateBlock(self,"room1",1,26,13,"tile_edge_0_up","na")
    Room_CreateBlock(self,"room1",1,26,15,"tile_edge_0_down-0","na")
    Room_CreateBlock(self,"room1",1,26,16,"tile_edge_0_down-1","na")

    # DOWN PATHWAY #
    Room_SetEdge(self,"room1",12,19,14,26,"0","0")
    Room_ChangeState(self,"room1","pass",12,19,14,26)
    Room_CreateBlock(self,"room1",2,12,19,"tile_ground_0_downLeft","na")
    Room_CreateBlock(self,"room1",2,13,19,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,14,19,"tile_ground_0_downRight","na")
    Room_CreateBlock(self,"room1",2,12,26,"tile_ground_0_left","na")
    Room_CreateBlock(self,"room1",2,13,26,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1",2,14,26,"tile_ground_0_right","na")
    Room_CreateBlock(self,"room1",1,12,26,"tile_edge_0_left","na")
    Room_CreateBlock(self,"room1",1,14,26,"tile_edge_0_right","na")

    # DECOR TILES #
    Room_CreateBlock(self,"room1",4,13,9,f"tile_decor_tree0","")
    Room_CreateBlock(self,"room1",3,13,9,f"shadow_default2_7_10","na")
    Room_CreateBlock(self,"room1",4,13,9,f"tile_decor_tree0","")
    Room_CreateBlock(self,"room1",3,13,9,f"shadow_default2_7_10","na")

    # HUE MODIFICATIONS #
    Room_ChangeHue(self,"room1",0,0,0,26,26,"25_13_0_0")
    for i in range(2): 
        Room_ChangeHue(self,"room1",1+i,0,0,26,26,"25_0_-25_0")
        # INTRO PATHWAY HUE MOD #
        Room_ChangeHue(self,"room1",1+i,9,0,11,0,"-33_-21_33_0")
        Room_ChangeHue(self,"room1",1+i,9,1,11,1,"-22_-14_22_0")
        Room_ChangeHue(self,"room1",1+i,9,2,11,2,"-11_-7_11_0")
        # LEFT PATHWAY HUE MOD #
        Room_ChangeHue(self,"room1",1+i,0,13,0,16,"-60_-60_-60_0")
        Room_ChangeHue(self,"room1",1+i,1,13,1,16,"-40_-40_-40_0")
        Room_ChangeHue(self,"room1",1+i,2,13,2,16,"-20_-20_-20_0")
        # RIGHT PATHWAY HUE MOD #
        Room_ChangeHue(self,"room1",1+i,26,13,26,16,"-60_-60_-60_0")
        Room_ChangeHue(self,"room1",1+i,25,13,25,16,"-40_-40_-40_0")
        Room_ChangeHue(self,"room1",1+i,24,13,24,16,"-20_-20_-20_0")
        # DOWN PATHWAY HUE MOD #
        Room_ChangeHue(self,"room1",1+i,12,26,14,26,"-60_-60_-60_0")
        Room_ChangeHue(self,"room1",1+i,12,25,14,25,"-40_-40_-40_0")
        Room_ChangeHue(self,"room1",1+i,12,24,14,24,"-20_-20_-20_0")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # -= ROOM 1B 0 =- #
    Room_Build(self,"room1B0",60,60,"","")
    Room_CreateWall(self,"room1B0",0,0,0,59,59,"rgba_0_0_0_255","")
    Room_CreateWall(self,"room1B0",5,0,0,59,59,f"pco_shadow_0_0_0_0","na")

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - #

    # RIGHT PATHWAY #
    Room_SetEdge(self,"room1B0",54,49,59,51,"0","0")
    Room_ChangeState(self,"room1B0","pass",54,49,59,51)
    for i in range(3): Room_CreateSend(self,"room1B0",59,49+i,"room1",0,13+i)
    Room_CreateBlock(self,"room1B0",2,54,49,"tile_ground_0_upRight","na")
    Room_CreateBlock(self,"room1B0",2,54,50,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1B0",2,54,51,"tile_ground_0_downRight","na")
    Room_CreateBlock(self,"room1B0",2,59,49,"tile_ground_0_up","na")
    Room_CreateBlock(self,"room1B0",2,59,50,"tile_ground_0_full","na")
    Room_CreateBlock(self,"room1B0",2,59,51,"tile_ground_0_down","na")
    Room_CreateBlock(self,"room1B0",1,59,49,"tile_edge_0_up","na")
    Room_CreateBlock(self,"room1B0",1,59,51,"tile_edge_0_down-0","na")
    Room_CreateBlock(self,"room1B0",1,59,52,"tile_edge_0_down-1","na")



    