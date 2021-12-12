from game.actions.action import Action
from game import constants
from game.services.point import Point
from game.actors.bullet import Bullet

class Angle_Fire_Left_Pattern(Action):
    """
    Fires the bullets and an angle the spreeds out in each
    driction while moveing downward.
    """
    def __init__(self,input_servce):
        self._input_service = input_servce


    def execute(self, cast):
        if len(cast["p2_ship"]) == 0:
            return

        fire_type = 2
        bullet_count = constants.P2_LEFT_ANGLE_FIRE_BULLET_COUNT

        p2 = cast["p2_ship"][0]
        bullets = cast["bullets"]

        if (self._input_service.is_space_down() and 
            p2.get_bullet_type() == fire_type and
            p2.get_frames_past_fire(fire_type) > constants.P2_LEFT_ANGLE_FIRE_COOL_DOWN):
            
            i = 0
            while i <= bullet_count:
                bullet = self.fire_bullet(Point(-(((2*i)-bullet_count)/bullet_count)*constants.P2_BULLET_SPEED,
                                                ((1-((2*i)-bullet_count)/bullet_count))* constants.P2_BULLET_SPEED),p2)
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
