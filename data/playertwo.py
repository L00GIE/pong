import pygame
from lib.player import Player

class PlayerTwo(Player):

    def __init__(self, core):
        super().__init__()
        self.core = core
        self.paddleimg = pygame.image.load("data/assets/paddle-green.png")
        self.w = self.paddleimg.get_width()
        self.h = self.paddleimg.get_height()
        self.y = (self.core.screen.get_height() / 2) - (self.h / 2)
        self.x = self.core.screen.get_width() - self.w
        self.speed = 10

    def loop(self):
        self.getMovement()
        self.updateRect()
        self.core.screen.blit(self.paddleimg, (self.x, self.y))

    def getMovement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed