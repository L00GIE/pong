import pygame

class Text:

    def __init__(self, core, text, coords, 
                 font="Impact", fontsize=64, 
                 color=(255,255,255)):
        self.core = core
        self.text = text
        self.color = color
        self.x = coords[0]
        self.y = coords[1]
        self.font = pygame.font.SysFont(font, fontsize)

    def loop(self):
        text_surface = self.font.render(self.text, True, self.color)
        if self.text == "PRESS SPACE TO BEGIN":
            self.x += 5
            if self.x > self.core.screen.get_width():
                self.x = -600
        else:
            self.x = (self.core.screen.get_width() / 2) - (text_surface.get_width() / 2)
        self.core.screen.blit(text_surface, (self.x, self.y))
