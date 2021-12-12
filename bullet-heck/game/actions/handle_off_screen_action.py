from game.actions.action import Action
from game.services.point import Point
from game import constants

class Handle_Off_Screen_Action(Action):
    """
    This class recives the cast and handles all actions 
    related to actors on the ednge of the screen
    """

    def execute(self, cast):
        """
        Handles all off screen actions of the game.
        """

        ###This will be used in a later version of the game to let bullets bouce on edge
        # for group in cast.values():
        #     for actor in group:
        #         if actor.get_bounce_on_edge():
        #             if actor.get_position_y() < 0:
        #                 dx = actor.get_velocity_x()
        #                 dy = (actor.get_velocity_y()) * -1
        #                 actor.set_velocity(Point(dx,dy))
        #             if actor.get_position_x() + actor.get_width() > constants.MAX_X or actor.get_position_x() < 0:
        #                 dx = (actor.get_velocity_x()) * -1
        #                 dy = actor.get_velocity_y()
        #                 actor.set_velocity(Point(dx,dy))

        #Removes the Bullets that have gone off the side of the screen
        for group in cast.values():
            for actor in group:
                if (actor.get_position_x() < -100 or
                    actor.get_position_x() > constants.MAX_X + 100 or
                    actor.get_position_y() < -100 or
                    actor.get_position_y() > constants.MAX_Y + 100):
                    
                    cast["bullets"].remove(actor)
