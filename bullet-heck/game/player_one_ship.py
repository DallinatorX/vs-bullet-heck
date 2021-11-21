from game.actor import Actor
from game.point import Point
from game import constants


class Player_One_Ship(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(50)
        self.set_height(50)
        self.set_type("p1_ship")
        self.set_position(Point(constants.MAX_X / 2, constants.MAX_Y / 2))