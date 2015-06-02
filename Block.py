#basic block
class Block():

    #init variables
    def __init__(self, solid, removable, position, size, color):
        self.__solid = solid            #material property
        self.__removable = removable    #material property
        self.__position = position
        self.__size = size
        self.__color = color            #material property

    #draw box
    def draw(self, display):
        x = self.getPosition()[0] * self.getSize()[0]
        y = self.getPosition()[1] * self.getSize()[1]
        display.fill(self.getColor(), rect=[x, y, self.getSize()[0], self.getSize()[1]])

    #returns objects state as string
    def toString(self):
        string = ("Solid: " + str(self.getSolid()) + "\n"
              "Removable: " + str(self.getRemovable()) + "\n"
              "Position: " + str(self.getPosition()) + "\n"
              "Size: " + str(self.getSize()) + "\n"
              "Color: " + str(self.getColor()))
        return string

    #setters
    def setSolid(self, solid):
        self.__solid = solid
    def setRemovable(self, removable):
        self.__removable = removable
    def setPosition(self, position):
        self.__position = list(position)
    def setSize(self, size):
        self.__size = list(size)
    def setColor(self, color):
        self.__color = tuple(color)

    #getters
    def getSolid(self):
        return self.__solid
    def getRemovable(self):
        return self.__removable
    def getPosition(self):
        return self.__position
    def getSize(self):
        return self.__size
    def getColor(self):
        return self.__color