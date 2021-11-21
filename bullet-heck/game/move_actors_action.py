from game.action import Action
from game.point import Point

class Move_Actors_Action(Action):
    """
    This moves the actor
    """
    
    def execute(self, cast):
        """
        It takes the cast and adds the veloicty to the position 
        in oder to move the actor
        """
        pause_menu = cast["pause_menu"][0]
        if(pause_menu.is_paused()):
            pass
        else:
            for group in cast.values():
                for actor in group:
                    x = actor._position.get_x()
                    y = actor._position.get_y()
                    dx = actor._velocity.get_x()
                    dy = actor._velocity.get_y()
                    x = (x + dx) #% constants.MAX_X
                    y = (y + dy) #% constants.MAX_Y

                    position = Point(x, y)
                    actor.set_position(position)
