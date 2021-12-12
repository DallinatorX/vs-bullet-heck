from game.actors.actor import Actor
from game.services.point import Point
from game import constants


class Player_Two_Ship(Actor):
    """
    This is the Player 2 Ship (The Villain)
    """
    def __init__(self):
        super().__init__()
        self.set_width(200)
        self.set_height(50)
        self.set_type("p2_ship")
        self.set_position(Point(constants.MAX_X / 2 , 0))
        self._hp = constants.P2_HP
        self._bullet_type = 2
        self.set_image(constants.P2_SHIP_IMAGE)


        self._frames_past_fire = [100,100,100,100,100,100,100,100,100,100]

    def add_frame_past_fire(self):
        """
        This counts how many frames have passed since a 
        Given Shot
        """
        i = 0
        while i < len(self._frames_past_fire):
            self._frames_past_fire[i] += 1
            i += 1

    def get_frames_past_fire(self,type):
        """
        Given the type of Shot 0 - 9
        returns the frames past when it 
        was last used.
        """
        return self._frames_past_fire[type]

    def reset_frames_past_fire(self,type):
        """
        Given the Type of Shot it sets the frames past
        last fire to 0
        """
        self._frames_past_fire[type] = 0

    def take_dammage(self, dammage):
        """
        Given the ammount of dammage to be taken
        sutracts it from the current hp
        """
        self._hp -= dammage

    def get_hp(self):
        """
        Returns HP
        """
        return self._hp

    def get_bullet_type(self):
        """
        Returns a number 0-9 of what 
        shot is currently set
        """
        return self._bullet_type

    def set_bullet_type(self,bullet_type):
        """
        Given a Number 0-9 sets the current shot type
        """
        self._bullet_type = bullet_type

    def set_hp(self,hp):
        """
        Sets the HP to a given number
        """
        self._hp = hp