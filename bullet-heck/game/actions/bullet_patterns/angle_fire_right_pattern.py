from game.actions.action import Action
from game.services.input_service import InputService    
from game.actors.bullet import Bullet
from game.services.point import Point
from game import constants


class Angle_Fire_Right_Pattern(Action):
    def __init__(self,input_servce):
        self._input_service = input_servce

    def execute(self, cast):
        p2 = cast["p2_ship"][0]
        bullets = cast["bullets"]
        bullet_count = constants.P2_RIGHT_ANGLE_FIRE_BULLET_COUNT



        if (self._input_service.is_space_down() and 
            p2.get_bullet_type() == 1 and
            p2.get_frames_past_fire(1) > constants.P2_RIGHT_ANGLE_FIRE_COOL_DOWN):
            i = 0
            while i <= bullet_count:
                bullet = self.fire_bullet(Point((((i*2)-bullet_count)/bullet_count)*constants.P2_BULLET_SPEED,
                                                ((1-((i*2)-bullet_count)/bullet_count))* constants.P2_BULLET_SPEED),p2)
                bullets.append(bullet)
                i += 1
            p2.reset_frames_past_fire(1)

    def fire_bullet(self,velocity,p2):
        bullet = Bullet()
        bullet.set_player(1)
        bullet.set_position(Point(p2.get_position_x()+(p2.get_width()/2),
                          (p2.get_position_y()) + (p2.get_height())))
        bullet.set_velocity(velocity)
        return bullet