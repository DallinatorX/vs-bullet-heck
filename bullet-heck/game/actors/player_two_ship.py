from game.actors.actor import Actor
from game.services.point import Point
from game import constants


class Player_Two_Ship(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(200)
        self.set_height(75)
        self.set_type("p2_ship")
        self.set_position(Point(constants.MAX_X / 2 , 0))
        self._hp = constants.P2_HP
        self._bullet_type = 2

        self._frames_past_fire = [100,100,100,100,100,100,100,100,100,100]

    def add_frame_past_fire(self):
        i = 0
        while i < len(self._frames_past_fire):
            self._frames_past_fire[i] += 1
            i += 1

    def get_frames_past_fire(self,type):
        return self._frames_past_fire[type]

    def reset_frames_past_fire(self,type):
        self._frames_past_fire[type] = 0

    def take_dammage(self, dammage):
        self._hp -= dammage

    def get_hp(self):
        return self._hp

    def get_bullet_type(self):
        return self._bullet_type

    def set_bullet_type(self,bullet_type):
        self._bullet_type = bullet_type