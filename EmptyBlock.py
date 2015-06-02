import Block
#basic empty block
class EmptyBlock(Block.Block):
    def __init__(self, size, position):
        solid = False
        removable = True
        color = (255, 255, 255)
        super(EmptyBlock, self).__init__(solid, removable, position, size, color)