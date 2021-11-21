from game.action import Action
from game.point import Point
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
        It takes the cast and makes the ball bounce off of bricks and paddles. 
        It rmoves the brick from the list if it hit a brick
        """
        if len(cast["ball"]) == 0:
            return
        ball = cast["ball"][0] 
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        if self._physics_service.is_collision(paddle, ball):
            ball_on_paddle = ball.get_position_x() - paddle.get_position_x()
            if ball_on_paddle == (paddle.get_width() / 2) - (ball.get_width() / 2):
                dx = 0
                dy = -constants.BALL_DY
            elif ball_on_paddle < (paddle.get_width() / 2):
                dx = -constants.BALL_DX * (((paddle.get_width() / 2) - ball_on_paddle) / (paddle.get_width() / 2))
                dy = -constants.BALL_DY
            elif ball_on_paddle > (paddle.get_width() / 2):
                dx = -constants.BALL_DX * (((paddle.get_width() / 2) - ball_on_paddle) / (paddle.get_width() / 2))
                dy = -constants.BALL_DY





            ball.set_velocity(Point(dx,dy))
            self._audio_service.play_sound(constants.SOUND_BOUNCE)
        for brick in bricks:
            if self._physics_service.is_collision(brick, ball):
                dx = ball.get_velocity_x()
                dy = (ball.get_velocity_y()) * -1
                ball.set_velocity(Point(dx,dy))
                self._audio_service.play_sound(constants.SOUND_BOUNCE)
                cast["bricks"].remove(brick)

