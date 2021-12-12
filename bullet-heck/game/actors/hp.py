from game.actors.actor import Actor
from game import constants

class Hp(Actor):
    """
    This is the test on the top left of the screen
    Showing player two's HP
    """
    def __init__(self):
        super().__init__()
        self.set_type("Hp")
        self.set_text(f"HP: {constants.P2_HP}")


    def set_Hp(self, hp):
        """
        Sets the HP given a number
        """
        self.set_text(f"HP: {hp}")  

        