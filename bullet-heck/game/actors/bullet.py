from game.actors.actor import Actor

class Bullet(Actor):
    def __init__(self):
        super().__init__()
        self._player = 0
    #temp
        self.set_height(5)
        self.set_width(5)

    def set_player(self, player):
        self._player = player

    def return_player(self):
        return self._player