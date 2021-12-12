from game.actors.actor import Actor
from game.services.point import Point
from game import constants


class Player_One_Ship(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(35)
        self.set_height(40)
        self.set_type("p1_ship")
        self.set_position(Point(constants.MAX_X / 2, constants.MAX_Y / 2))
        self._frames_past_fire = 100
        self.set_image(constants.P1_SHIP_IMAGE)


    def add_frame_past_fire(self):
        """
        Adds one to a counter to keep track of
        how many frames have passed since last
        fire.
        """
        self._frames_past_fire += 1

    def get_frames_past_fire(self):
        """
        Returns the Number of frames past last Fire
        """
        return self._frames_past_fire

    def reset_frames_past_fire(self):
        """
        Sets the numbers of frames past last fire to 0
        """
        self._frames_past_fire = 0