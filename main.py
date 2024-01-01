import sys
sys.dont_write_bytecode = True

import pygame
from lib.core import Core

pygame.init()

screen = pygame.display.set_mode((1366, 768))
clock = pygame.time.Clock()
core = Core(screen)

running = True
while running:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            running = False
    if running:
        core.loop(ev)
        clock.tick(60)
        pygame.display.update()

pygame.quit()
sys.exit(0)