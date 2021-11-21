from game.action import Action
from game.point import Point
from game import constants

class Handle_Off_Screen_Action(Action):
    """
    This class recives the cast and if any member is set to bonce on edage
    then it changes its veloicty
    """

    def execute(self, cast):
        """
        Makes objects bounce on the edge
        """
        for group in cast.values():
            for actor in group:
                if actor.get_bounce_on_edge():
                    if actor.get_position_y() < 0:
                        dx = actor.get_velocity_x()
                        dy = (actor.get_velocity_y()) * -1
                        actor.set_velocity(Point(dx,dy))
                    if actor.get_position_x() + actor.get_width() > constants.MAX_X or actor.get_position_x() < 0:
                        dx = (actor.get_velocity_x()) * -1
                        dy = actor.get_velocity_y()
                        actor.set_velocity(Point(dx,dy))
                if actor.get_position_y() > constants.MAX_Y:
                    cast["ball"].remove(actor)