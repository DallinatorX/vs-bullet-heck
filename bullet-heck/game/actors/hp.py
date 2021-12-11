from game.actors.actor import Actor
from game import constants

class Hp(Actor):
    def __init__(self):
        super().__init__()
        self.set_type("Hp")
        self.set_text(f"HP: {constants.P2_HP}")

    def set_Hp(self, hp):
        self.set_text(f"HP: {hp}")  

        