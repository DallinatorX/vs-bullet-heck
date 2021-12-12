from game.actors.actor import Actor
from game import constants
from game.services.point import Point

class Welcome_Screen(Actor):
    """
    This is the Welcome screen to the game.
    """
    def __init__(self):
        super().__init__()
        self.set_text("\n\nBullet \"Nether\" (BYUI Safe) \n\n\n The game is simple, one player is the Hero and the other is the Villain.\n\n The Hero uses the arrow keys to move and shift to fire.\n\n The Villain uses 'a' and 'd' to controll,\n space to fire,\n and the number keys to change guns.\n\n\n Press 'Enter' to start")
        self.set_position(Point(0,0))
        self._open = True

    def close_welcome_screen(self):
        self.set_position(Point(0,constants.MAX_Y +1))
        self._open = False

    def is_closed(self):
        return not self._open