from game.actor import Actor
from game.point import Point
from game import constants


class Player_Two_Ship(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(200)
        self.set_height(75)
        self.set_type("p2_ship")
        self.set_position(Point(constants.MAX_X / 2 , 0))