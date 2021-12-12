from game.actors.actor import Actor

class Bullet(Actor):
    def __init__(self):
        """
        This is the class used for all bullets in the game
        """
        super().__init__()
        self._player = 0
        self.set_height(5)
        self.set_width(5)

    def set_player(self, player):
        """
        This sets which player the bullet can hurt
        """
        self._player = player

    def return_player(self):
        """
        This returns which player the bullet can hurt.
        """
        return self._player