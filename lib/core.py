from data.game import Game

class Core:

    def __init__(self, screen):
        self.screen = screen
        self.scene = None

    def loop(self, events):
        self.events = events
        if self.scene is None:
            self.scene = Game(self)
        self.scene.loop()
