from game.actions.action import Action
from game.services.point import Point
from game import constants

class Handle_Collisions_Action(Action):
    """
    This class handles any action that an actor may need preformed
    """
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service


    def execute(self, cast):
        """
        Handles all bullets and checks if they have hit a player
        if they hit player 2 they remove hp 
        if they hit player 1 they remove the player one actor
        """
        if len(cast["p1_ship"]) == 0 or len(cast["p2_ship"]) == 0:
            return
        p1 = cast["p1_ship"][0] 
        p2 = cast["p2_ship"][0]
        bullets = cast["bullets"]
        if self._physics_service.is_collision(p1, p2):
            cast["p1_ship"].remove(p1)


        for bullet in bullets:
            if self._physics_service.is_collision(bullet, p1):
                if bullet.return_player() == 1:
                    cast["bullets"].remove(bullet)
                    cast["p1_ship"].remove(p1)
            
            if self._physics_service.is_collision(bullet, p2):
                if bullet.return_player() == 2:
                    cast["bullets"].remove(bullet)
                    p2.take_dammage(1)
                    if p2.get_hp() == 0:
                        cast["p2_ship"].remove(p2)