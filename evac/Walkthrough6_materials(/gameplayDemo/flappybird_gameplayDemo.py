import pygame
import sys
import numpy as np

pygame.init()

class FlappyBird:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 708))
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.background = pygame.image.load("assets/background.png").convert()
        self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                            pygame.image.load("assets/2.png").convert_alpha(),
                            pygame.image.load("assets/dead.png")]
        self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
        self.wallDown = pygame.image.load("assets/top.png").convert_alpha()
        self.gap = 130 # 130 is possible
        self.gravity = 5
        self.restart()

    def updateWalls(self):
        self.wallx -= 5   #Speed of wall movement
        self.distanceMoved += 5
        if self.wallx < -80:
            self.wallx = 400
            self.counter += 1
            self.offset = np.random.randint(-180, 200)

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY
        upRect = pygame.Rect(self.wallx,
                             360 + self.gap - self.offset + 10,
                             self.wallUp.get_width() - 10,
                             self.wallUp.get_height())
        downRect = pygame.Rect(self.wallx,
                               0 - self.gap - self.offset - 10,
                               self.wallDown.get_width() - 10,
                               self.wallDown.get_height())

        # Collision detection between birth and pipes
        if upRect.colliderect(self.bird):
            self.dead = True
        if downRect.colliderect(self.bird):
            self.dead = True

        if not 0 < self.bird[1] < 720:
            self.dead = True

    def updateScreen(self):
        font = pygame.font.SysFont("Arial", 50)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        self.wallUpY = 360 + self.gap - self.offset
        self.wallDownY = 0 - self.gap - self.offset
        self.screen.blit(self.wallUp, (self.wallx, self.wallUpY))
        self.screen.blit(self.wallDown, (self.wallx, self.wallDownY))
        self.screen.blit(font.render(str(self.counter), -1, (255, 255, 255)),(200, 50))
        self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))

    def makeJump(self):
        self.jump = 17
        self.gravity = 5
        self.jumpSpeed = 10

    def restart(self):
        self.wallx = 400
        self.wallUpY = 0
        self.wallDownY = 0
        self.birdY = 400
        self.jump = 0 # A timer for the jump
        self.jumpSpeed = 10
        self.dead = False
        self.sprite = 1
        self.distanceMoved = 0
        self.counter = 0
        self.stepsSinceLastJump = 0
        self.offset = np.random.randint(-180, 300)


    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                    self.jump = 17
                    self.gravity = 5
                    self.jumpSpeed = 10

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.wallUp,
                             (self.wallx, 360 + self.gap - self.offset))
            self.screen.blit(self.wallDown,
                             (self.wallx, 0 - self.gap - self.offset))
            self.screen.blit(font.render(str(self.counter),
                                         -1,
                                         (255, 255, 255)),
                             (200, 50))
            if self.dead:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1

            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))
            if not self.dead:
                self.sprite = 0
            self.updateWalls()
            self.birdUpdate()

            if self.dead: self.restart()

            pygame.display.update()

if __name__ == "__main__":
    FlappyBird().run()
