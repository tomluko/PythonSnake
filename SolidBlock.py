import Block
#basic building block
class SolidBlock(Block.Block):
    def __init__(self, size, position):
        solid = True
        removable = False
        color = (59, 23, 11)
        super(SolidBlock, self).__init__(solid, removable, position, size, color)