import Block
#snakes body segment
class SnakeBlock(Block.Block):
    def __init__(self, size, position):
        solid = True
        removable = False
        color = (0, 153, 0)
        super(SnakeBlock, self).__init__(solid, removable, position, size, color)
