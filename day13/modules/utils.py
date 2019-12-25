from day13.modules.screen import Screen

def CountBlockTiles(screen: Screen):
    ''' Count Block tiles '''
    i = 0
    for tile in screen.grid.keys():
        if screen.grid[tile].type == 2: i += 1
    print("There are {} blocks on the screen.".format(i))