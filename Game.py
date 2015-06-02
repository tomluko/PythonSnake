import pygame
import Level
class Game():

    def __init__(self, fileName):
        self.__GameOver = False
        self.__FPS = 5
        #status = pygame.init();
        #print(status)
        pygame.init()
        self.__font = pygame.font.SysFont(None, 20)
        self.__level = Level.Level()
        self.__level.generateMap(fileName)
        self.__level.spawnFood()
        self.__display = pygame.display.set_mode(self.__level.getScreenSize())
        pygame.display.set_caption("PythonSnake by Tomas Lukošius")

    def run(self):
        clock = pygame.time.Clock()
        #main game loop
        while(not self.__GameOver):

            #button logics
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    self.__GameOver = True
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_a):
                        self.__level.getSnake().setMovementVector([-1, 0])
                    elif(event.key == pygame.K_d):
                        self.__level.getSnake().setMovementVector([1, 0])
                    elif(event.key == pygame.K_w):
                        self.__level.getSnake().setMovementVector([0, -1])
                    elif(event.key == pygame.K_s):
                        self.__level.getSnake().setMovementVector([0, 1])

            #game logics
            self.__level.getSnake().move()
            if(self.__level.getSnake().isDead()):
                self.__GameOver = True

            #draw image
            self.draw()
            pygame.display.update()
            clock.tick(self.__FPS)
        #end of while loop
        pygame.quit()

    def draw(self):
        self.__level.draw(self.__display)
        score = self.getLevel().getSnake().getBodyLength()
        scoreText = self.__font.render("Score: " + str(score), True, (204, 255, 51))
        self.__display.blit(scoreText, [5, 5])

    #getters
    def getLevel(self):
        return self.__level