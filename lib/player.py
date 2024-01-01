import pygame

class Player:

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.points = 0

    def updateRect(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.w = self.w
        self.rect.h = self.h