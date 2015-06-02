import SnakeBlock
import EmptyBlock
#controls snake movement, growing

class Snake():

    def __init__(self, size, position, level):
        self.__speed = [1, 1]            #number of blocks to move past
        self.__movementVector = [0, 0]   #direction and distance to move snake
        self.__map = []                  #map on which snake moves
        self.__body = []                 #list of snakes body elements
        self.__body.append(SnakeBlock.SnakeBlock(size, position))
        self.__isDead = False            #flag for snakes life
        self.__size = size               #block size
        self.__level = level             #pointer to level to call its stuff

    def move(self):
        #if movement happens
        if(self.getMovementVector()[0] != 0 or self.getMovementVector()[1] != 0):
            #head coords
            head = self.getBody()[0]
            oldPosition = head.getPosition()
            newPosition = [oldPosition[0] + self.getMovementVector()[0] * self.getSpeed()[0],
                           oldPosition[1] + self.getMovementVector()[1] * self.getSpeed()[1]]
            #check head intersection
            food = False
            if(self.checkSolidBlock(newPosition) == True):
                if(self.checkFood(newPosition) == True):
                    food = True
                else:
                    self.__isDead = True
            #print("snake: newPosition=" + str(newPosition) + " food=" + str(food) + " isDead=" + str(self.__isDead) + "\n")
            if(self.__isDead == False):
                #move head
                block = self.getMap()[newPosition[0]][newPosition[1]]
                self.getMap()[newPosition[0]][newPosition[1]] = head
                head.setPosition(newPosition)
                #move body
                if(len(self.getBody()) > 1):
                    for x in range(1, len(self.getBody())):
                        block = self.getBody()[x]
                        newPosition = list(oldPosition)
                        oldPosition = block.getPosition()
                        self.getMap()[newPosition[0]][newPosition[1]] = block
                        block.setPosition(newPosition)
                #tail
                if(food == True):
                    snakeBlock = SnakeBlock.SnakeBlock(self.getSize(), oldPosition)
                    self.getMap()[oldPosition[0]][oldPosition[1]] = snakeBlock
                    self.getBody().append(snakeBlock)
                    self.getLevel().spawnFood()
                else:
                    self.getMap()[oldPosition[0]][oldPosition[1]] = EmptyBlock.EmptyBlock(self.getSize(), oldPosition)

    #check if snake hits wall or itself
    def checkSolidBlock(self, newPosition):
        block = self.getMap()[newPosition[0]][newPosition[1]]
        #print(block.toString())
        if(block.getSolid() == True):
            return True
        else:
            return False

    #check if snake eats food
    def checkFood(self, newPosition):
        block = self.getMap()[newPosition[0]][newPosition[1]]
        if(block.getRemovable() == True):
            return True
        else:
            return False

    #getters
    def getSpeed(self):
        return self.__speed
    def getMovementVector(self):
        return self.__movementVector
    def getMap(self):
        return self.__map
    def getBodyLength(self):
        return len(self.__body)
    def getHead(self):
        return self.__body[0]
    def getBody(self):
        return self.__body
    def isDead(self):
        return self.__isDead
    def getLevel(self):
        return self.__level
    def getSize(self):
        return self.__size


    #setters
    def setSpeed(self, speed):
        self.__speed = list(speed)
    def setMovementVector(self, movementVector):
        self.__movementVector = list(movementVector)
    def setMap(self, map):
        self.__map = map
    def setLevel(self, level):
        self.__level = level