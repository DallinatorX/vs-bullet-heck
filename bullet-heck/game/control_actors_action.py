from game.action import Action
from game.input_service import InputService
from game.point import Point
from game import constants

class Control_Actors_Action(Action):
    """
    This class recives the cast and if any member is set to player
    control then in moves that actor
    """
    def __init__(self):
        self._input_service = InputService()
        self._is_paused = True
        

    def execute(self, cast):
        """
        This gets the actors and checks if they should be controlled 
        by the player. If so it changes the Veloicty
        """
        pause_menu = cast["pause_menu"][0]
        if self._input_service.get_key_press() == " ":
            pause_menu.set_pause(True)
        for group in cast.values():
            for actor in group:
                if actor.is_player_controlled():
                    if self._input_service.is_left_pressed():
                        actor.set_velocity(Point(-constants.PADDLE_SPEED,0))
                        pause_menu.set_pause(False)
                    elif self._input_service.is_right_pressed():
                        actor.set_velocity(Point(constants.PADDLE_SPEED,0))
                        pause_menu.set_pause(False)
                    else:
                        actor.set_velocity(Point(0,0))