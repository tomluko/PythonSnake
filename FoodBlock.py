import Block
#snakes food block
class FoodBlock(Block.Block):
    def __init__(self, size, position):
        solid = True
        removable = True
        color = (255, 51, 0)
        super(FoodBlock, self).__init__(solid, removable, position, size, color)