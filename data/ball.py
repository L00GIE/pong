import pygame, random

class Ball:

    def __init__(self, core):
        self.core = core
        self.initImages()
        self.ballimg = self.ballimgs[0]
        self.x = (self.core.screen.get_width() / 2) - (self.ballimg.get_width() / 2)
        self.y = (self.core.screen.get_height() / 2) - (self.ballimg.get_height() / 2)
        self.speed = 5
        self.direction = random.randint(0,1)
        self.goingup = False
        self.goingdown = False
        self.started = False
        self.colorindex = 0
        self.rect = pygame.Rect(self.x, self.y, self.ballimg.get_width(), self.ballimg.get_height())

    def loop(self):
        if self.core.scene.started:
            if self.direction == 0:
                self.x -= self.speed
            else:
                self.x += self.speed
            if self.goingup:
                self.y -= self.speed
                if self.y <= 0:
                    self.godown()
            elif self.goingdown:
                self.y += self.speed
                if self.y >= self.core.screen.get_height() - self.ballimg.get_height():
                    self.goup()
            self.updateRect()
        self.core.screen.blit(self.ballimg, (self.x, self.y))

    def initImages(self):
        self.ballimgs = [
            pygame.image.load("data/assets/ball/ball-red.png"),
            pygame.image.load("data/assets/ball/ball-orange.png"),
            pygame.image.load("data/assets/ball/ball-yellow.png"),
            pygame.image.load("data/assets/ball/ball-green.png"),
            pygame.image.load("data/assets/ball/ball-blue.png"),
            pygame.image.load("data/assets/ball/ball-violet.png")
        ]

    def updateRect(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.w = self.ballimg.get_width()
        self.rect.h = self.ballimg.get_height()

    def changedirection(self):
        self.direction = 0 if self.direction == 1 else 1
        self.colorindex += 1
        if self.colorindex >= len(self.ballimgs):
            self.colorindex = 0
        self.ballimg = self.ballimgs[self.colorindex]
        self.speed += 1

    def goup(self):
        self.goingup = True
        self.goingdown = False

    def godown(self):
        self.goingup = False
        self.goingdown = True

    def reset(self):
        self.x = (self.core.screen.get_width() / 2) - (self.ballimg.get_width() / 2)
        self.y = (self.core.screen.get_height() / 2) - (self.ballimg.get_height() / 2)
        self.speed = 5
        self.changedirection()
