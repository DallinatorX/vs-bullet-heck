from game.action import Action
from game.point import Point
from game import constants
from game.bullet import Bullet

class Fire_Bullet(Action):
    def __init__(self,input_servce):
        super().__init__()
        #self._bullet = Bullet()
        self._input_service = input_servce

    def execute(self, cast):
        """
        
        """
        if len(cast["p1_ship"]) == 0 or len(cast["p2_ship"]) == 0:
            return

        p1 = cast["p1_ship"][0] 
        p1.add_frame_past_fire()
    
        p2 = cast["p2_ship"][0]
        p2.add_frame_past_fire()

        
        bullets = cast["bullets"]
        if (self._input_service.is_shift_down() and
            p1.get_frames_past_fire() > constants.P1_BULLET_COOL_DOWN):
            bullet = Bullet()
            bullet.set_player(2)
            bullet.set_velocity(Point(0,-constants.P1_BULLET_SPEED))
            bullet.set_position(Point(p1.get_position_x()+(p1.get_width()/2),p1.get_position_y()))
            bullets.append(bullet)
            p1.reset_frames_past_fire()

        if (p2.get_frames_past_fire() > constants.P2_BULLET_COOL_DOWN):
            bullet = Bullet()
            bullet.set_player(1)
            bullet.set_velocity(Point(0,constants.P2_BULLET_SPEED))
            bullet.set_position(Point(p2.get_position_x()+(p2.get_width()/2),
                                      (p2.get_position_y()) + (p2.get_height())))
            bullets.append(bullet)
            p2.reset_frames_past_fire()