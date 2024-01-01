import pygame
from lib.player import Player

class PlayerOne(Player):

    def __init__(self, core):
        super().__init__()
        self.core = core
        self.paddleimg = pygame.image.load("data/assets/paddle-purple.png")
        self.w = self.paddleimg.get_width()
        self.h = self.paddleimg.get_height()
        self.y = (self.core.screen.get_height() / 2) - (self.h / 2)
        self.x = 10
        self.speed = 10

    def loop(self):
        self.getMovement()
        self.updateRect()
        self.core.screen.blit(self.paddleimg, (self.x, self.y))

    def getMovement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed