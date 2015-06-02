from random import randrange
import SolidBlock
import EmptyBlock
import FoodBlock
import FileIO
import Snake
class Level():

    def __init__(self):
        self.__size = [30, 30]
        self.__map = []
        self.__FileIO = FileIO.FileIO()
        self.__snake = None
        self.__screenSize = []

    def generateMap(self, fileName):
        #read map from file
        if(self.__FileIO == None):
            return
        mapTemplate = self.__FileIO.readLevel(fileName)
        #mirror map diagonaly to adapt to pygame screen coords system. 0, 0 is top left corner of render window
        mapTransformed = []
        x_length = len(mapTemplate)
        if(x_length < 1):
            return
        y_length = len(mapTemplate[0])
        for y in range(0, y_length):
            mapTransformed.append([])
            for x in range(0, x_length):
                mapTransformed[y].append(mapTemplate[x][y])
        #calculate screensize for render window from map
        self.__screenSize = [y_length * self.__size[1], x_length * self.__size[0]]
        #fill map with objects
        for x in range(0, len(mapTransformed)):
            mapObjects = []
            for y in range(0, len(mapTransformed[x])):
                if(mapTransformed[x][y] == "0"):
                    mapObjects.append(EmptyBlock.EmptyBlock(self.getSize(), [x, y]))
                elif(mapTransformed[x][y] == "1"):
                    mapObjects.append(SolidBlock.SolidBlock(self.getSize(), [x, y]))
                elif(mapTransformed[x][y] == "2"):
                    self.setSnake(Snake.Snake(self.getSize(), [x, y], self))
                    mapObjects.append(self.getSnake().getHead())
            self.__map.append(mapObjects)
        self.getSnake().setMap(self.getMap())

    def spawnFood(self):
        canBePlaced = False
        while(canBePlaced != True):
            newPosition = [randrange(0, len(self.getMap())), randrange(0, len(self.getMap()[0]))]
            if(self.checkSolidBlock(newPosition) == False):
                canBePlaced = True
        self.getMap()[newPosition[0]][newPosition[1]] = FoodBlock.FoodBlock(self.getSize(), newPosition)

    #check if block is solid
    def checkSolidBlock(self, newPosition):
        block = self.getMap()[newPosition[0]][newPosition[1]]
        #print(block.toString())
        if(block.getSolid() == True):
            return True
        else:
            return False

    #draw all map objects
    def draw(self, display):
        if(self.getMap() == None):
            return
        for line in self.getMap():
            for block in line:
                block.draw(display)

    #getters
    def getMap(self):
        return self.__map
    def getSize(self):
        return self.__size
    def getSnake(self):
        return self.__snake
    def getScreenSize(self):
        return self.__screenSize

    #setters
    def setMap(self, map):
        self.__map = map
    def setSize(self, size):
        self.__size = list(size)
    def setSnake(self, snake):
        self.__snake = snake