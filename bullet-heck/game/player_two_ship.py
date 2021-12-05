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
        self._hp = constants.P2_HP

        self._frames_past_fire = 100

    def add_frame_past_fire(self):
        self._frames_past_fire +=1

    def get_frames_past_fire(self):
        return self._frames_past_fire

    def reset_frames_past_fire(self):
        self._frames_past_fire = 0

    def take_dammage(self, dammage):
        self._hp -= dammage

    def get_hp(self):
        return self._hp