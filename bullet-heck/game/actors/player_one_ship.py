from game.actors.actor import Actor
from game.services.point import Point
from game import constants


class Player_One_Ship(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(50)
        self.set_height(50)
        self.set_type("p1_ship")
        self.set_position(Point(constants.MAX_X / 2, constants.MAX_Y / 2))
        self._frames_past_fire = 100

    def add_frame_past_fire(self):
        self._frames_past_fire +=1

    def get_frames_past_fire(self):
        return self._frames_past_fire

    def reset_frames_past_fire(self):
        self._frames_past_fire = 0