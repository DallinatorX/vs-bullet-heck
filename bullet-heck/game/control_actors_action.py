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
        if self._input_service.get_key_press() == "p":
            pause_menu.invert_pause()

        for group in cast.values():
            for actor in group:
                if actor.get_type() == "p1_ship":
                    self.move_player_all(actor)

                if actor.get_type() == "p2_ship":
                    self.move_player_horizontal(actor)


    def move_player_all(self,actor):
        """
        Moves the player in any deriction
        """
        actor.set_velocity(Point(0,0))
        hit_edge = self.check_edge_collisions(actor)

        direction = self._input_service.get_direction()
        dx = direction.get_x() * constants.P1_SHIP_SPEED
        dy = direction.get_y() * constants.P1_SHIP_SPEED

        if dx < 0 and not hit_edge[0]:
            actor.set_velocity(Point(-constants.P1_SHIP_SPEED,
                                     actor.get_velocity_y()))
        if dx > 0 and not hit_edge[1]:
            actor.set_velocity(Point(constants.P1_SHIP_SPEED,
                                     actor.get_velocity_y()))
        if dy < 0 and not hit_edge[2]:
            actor.set_velocity(Point(actor.get_velocity_x(),
                                     -constants.P1_SHIP_SPEED))
        if dy > 0 and not hit_edge[3]:
            actor.set_velocity(Point(actor.get_velocity_x(),
                                     constants.P1_SHIP_SPEED))
    def move_player_horizontal(self,actor):
        """
        Moves the Player left or right
        """
        actor.set_velocity(Point(0,0))
        hit_edge = self.check_edge_collisions(actor)
        if self._input_service.is_left_pressed():
            if not hit_edge[0]:
                actor.set_velocity(Point(-constants.P2_SHIP_SPEED,0))
        elif self._input_service.is_right_pressed():
            if not hit_edge[1]:
                actor.set_velocity(Point(constants.P2_SHIP_SPEED,0))

    def check_edge_collisions(self,actor):
        """
        Checks to see if an actor is hitting the edge 
        and returns a list of what side or sides are
        being hit.

        List order
        0    1     2   3
        Left,Right,Top,Bottom
        """
        hit_edge = [False,False,False,False]
        if actor.get_position_x() <= 0:
            hit_edge[0] = True
        if actor.get_position_x() + actor.get_width() >= constants.MAX_X:
            hit_edge[1] = True
        if actor.get_position_y() <= 0:
            hit_edge[2] = True
        if actor.get_position_y() + actor.get_width() >= constants.MAX_Y:
            hit_edge[3] = True

        return hit_edge