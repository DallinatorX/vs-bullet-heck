from game.actions.action import Action
from game.services.input_service import InputService    
from game.actors.bullet import Bullet
from game.services.point import Point
from game import constants
import math


class Circle_Fire(Action):
    """
    This allows Player two to fire in a 
    Circle like pattern.
    """
    def __init__(self,input_servce):
        self._input_service = input_servce

    def execute(self, cast):
        if len(cast["p2_ship"]) == 0:
            return
        p2 = cast["p2_ship"][0]
        bullets = cast["bullets"]
        fire_type = 3

        if (self._input_service.is_space_down() and 
            p2.get_bullet_type() == fire_type and
            p2.get_frames_past_fire(fire_type) > constants.P2_CIRCLE_FIRE_COOL_DOWN):


            i = 0
            number_of_bullets = constants.P2_CIRCLE_FIRE_BULLET_COUNT
            while i <= number_of_bullets:
                # Calculateing the angle to fire each bullet
                x_angle = -math.cos(math.radians(180 + (i*(180 / number_of_bullets))))
                y_angle = -math.sin(math.radians(180 + (i*(180 / number_of_bullets))))
                bullet = self.fire_bullet(Point(x_angle * constants.P2_BULLET_SPEED,y_angle * constants.P2_BULLET_SPEED),p2)


                bullets.append(bullet)
                i += 1
            p2.reset_frames_past_fire(fire_type)

    def fire_bullet(self,velocity,p2):
        """
        Sets the bullets Veloicty and which player
        it can do dammage to.
        It is given the needed speed and the currenet
        player so that it knows where to place the bullet
        """
        bullet = Bullet()
        bullet.set_player(1)


        bullet.set_position(Point(p2.get_position_x()+(p2.get_width()/2),
                           (p2.get_position_y()) + (p2.get_height())))
        bullet.set_velocity(velocity)
        return bullet