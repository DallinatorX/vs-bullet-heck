from game.actor import Actor
from game.point import Point
from game import constants

class Pause_Menu_Actor(Actor):
    """
    This is the pause menu actor. It is always in the game
    It is just moved in to the center when pause is active
    """
    def __init__(self):
        super().__init__()
        self.set_text("PAUSED")
        self.set_position(Point(constants.MAX_X / 2 - 40, 
                                constants.MAX_Y / 2))
        self._paused = True

    def is_paused(self):
        return self._paused

    def set_pause(self, pause):
        """
        Moves the pause menu on or off the screen
        when it is called
        """
        self._paused = pause
        if pause:
            self.set_position(Point(constants.MAX_X / 2 - 40, 
                                    constants.MAX_Y / 2))
        else:
            self.set_position(Point(-50,-50))