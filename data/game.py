import pygame
from data.ball import Ball
from lib.scene import Scene
from data.playerone import PlayerOne
from data.playertwo import PlayerTwo
from lib.text import Text

class Game(Scene):

    def __init__(self, core):
        self.core = core
        super().__init__()
        self.players = None
        self.ball = None
        self.scoretext = None
        self.started = False
        self.bg = None

    def loop(self):
        for event in self.core.events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.started = True
        self.showBg()
        self.initPlayers()
        self.showScoretext()
        self.initBall()
        self.checkCollision()
        self.checkScoring()
        super().loop()

    def initPlayers(self):
        if self.players is None:
            self.players = [
                PlayerOne(self.core),
                PlayerTwo(self.core)
            ]
            for player in self.players:
                self.add(player)

    def initBall(self):
        if self.ball is None:
            self.ball = Ball(self.core)
            self.add(self.ball)
        self.ball.updateRect()

    def checkCollision(self):
        for player in self.players:
            if player.rect.colliderect(self.ball.rect):
                if self.ball.y < player.y + (player.rect.h / 2):
                    print(f"hit top")
                    self.ball.goup()
                else:
                    print("hit bottom")
                    self.ball.godown()
                self.ball.changedirection()
                break
        
    def checkScoring(self):
        if self.ball.x < 0 - self.ball.ballimg.get_width():
            self.players[1].points += 1
            self.ball.reset()
            self.started = False
        if self.ball.x > self.core.screen.get_width():
            self.players[0].points += 1
            self.ball.reset()
            self.started = False

    def showScoretext(self):
        if self.scoretext is None:
            self.scoretext = Text(self.core, "", (-600, 0))
            self.add(self.scoretext)
        if not self.started:
            text = "PRESS SPACE TO BEGIN"
        else:
            text = f"{self.players[0].points} | {self.players[1].points}"
        self.scoretext.text = text

    def showBg(self):
        if self.bg is None:
            self.bg = pygame.image.load("data/assets/background.png")
        self.core.screen.blit(self.bg, (0, 0))
