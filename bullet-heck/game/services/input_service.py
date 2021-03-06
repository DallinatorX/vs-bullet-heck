import sys
from game.services.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
        
    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if self.is_left_pressed():
            dx = -1
        
        if self.is_right_pressed():
            dx = 1
        
        if self.is_up_pressed():
            dy = -1
        
        if self.is_down_pressed():
            dy = 1

        direction = Point(dx, dy)
        return direction

    def is_left_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_LEFT)

    def is_right_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT)

    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_UP)

    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)

    def is_a_key_down(self):
        return raylibpy.is_key_down(raylibpy.KEY_A)

    def is_d_key_down(self):
        return raylibpy.is_key_down(raylibpy.KEY_D)
    
    def is_space_down(self):
        return raylibpy.is_key_down(raylibpy.KEY_SPACE)

    def is_shift_down(self):
        return raylibpy.is_key_down(raylibpy.KEY_RIGHT_SHIFT)

    def is_enter_down(self):
        return raylibpy.is_key_down(raylibpy.KEY_ENTER)


    def window_should_close(self):
        return raylibpy.window_should_close()

    def get_key_press(self):
        """
        Gets any key pressed
        """
        key_int = raylibpy.get_key_pressed()

        key_string = None

        if key_int != -1:
            key_string = chr(key_int)
        
        return key_string

    def get_number_key(self):
        """
        Gets a number key from the top row
        """
        number = -1
        if raylibpy.is_key_down(raylibpy.KEY_ONE):
            number = 1
        if raylibpy.is_key_down(raylibpy.KEY_TWO):
            number = 2
        if raylibpy.is_key_down(raylibpy.KEY_THREE):
            number = 3
        if raylibpy.is_key_down(raylibpy.KEY_FOUR):
            number = 4
        if raylibpy.is_key_down(raylibpy.KEY_FIVE):
            number = 5
        if raylibpy.is_key_down(raylibpy.KEY_SIX):
            number = 6
        if raylibpy.is_key_down(raylibpy.KEY_SEVEN):
            number = 7
        if raylibpy.is_key_down(raylibpy.KEY_EIGHT):
            number = 8
        if raylibpy.is_key_down(raylibpy.KEY_NINE):
            number = 9
        if raylibpy.is_key_down(raylibpy.KEY_ZERO):
            number = 0

        return number