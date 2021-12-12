from game.actors.actor import Actor
from game import constants
from game.services.point import Point

class Gameover_Screen(Actor):
    """
    This is an actor that shows the game over at the 
    end of the game.
    """
    def __init__(self):
        super().__init__()
        self.set_text("")
        self.set_position(Point(0,constants.MAX_Y +1))
        self._open = True

    def close_gameover_screen(self):
        """
        This moves the actor off of the screen where it 
        can not be seen.
        """
        self.set_position(Point(0,constants.MAX_Y +1))
        self._open = False

    def is_closed(self):
        """
        Returns if the game overs screen is being displayed
        """
        return not self._open

    def open_gameover_screen(self,winner):
        """
        This moves the game over screen to the center 
        of the screen and given the winner it displays 
        a winning message to the screen
        """
        self.set_position(Point(constants.MAX_X / 2 -100,constants.MAX_Y / 3))
        self._open = True
        self.set_text(f"Player {winner} Wins!\n\nPlay Again?\n'Y' or 'N'")