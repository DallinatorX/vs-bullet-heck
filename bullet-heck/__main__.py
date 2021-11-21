import os
os.environ['RAYLIB_BIN_PATH'] = "./lib/raylib"

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.move_actors_action import Move_Actors_Action
from game.handle_off_screen_action import Handle_Off_Screen_Action
from game.control_actors_action import Control_Actors_Action
from game.handle_collisions_action import Handle_Collisions_Action
from game.pause_menu_actor import Pause_Menu_Actor





def main():
    # create the cast {key: tag, value: list}
    cast = {}




    bricks = [] 
    for n in range(constants.BRICK_COUNT_COLLUMS):
        for m in range(constants.BRICK_COUNT_ROWS):
            brick = Brick()
            brick.set_position(Point(((n+1) * (constants.MAX_X / 
                              (constants.BRICK_COUNT_COLLUMS + 1))
                              )-constants.BALL_WIDTH, m * ((constants.MAX_Y / 1.5) 
                              / (constants.BRICK_COUNT_ROWS + 1)) + 
                              constants.BALL_WIDTH))
            bricks.append(brick) 
    cast["bricks"] = bricks

    # TODO: Create bricks here and add them to the list
    ball = Ball()

    cast["ball"] = [ball]
    # TODO: Create a ball here and add it to the list
    paddle = Paddle()
    cast["paddle"] = [paddle]
    # TODO: Create a paddle here and add it to the list
    pause_menu = Pause_Menu_Actor()
    cast["pause_menu"] = [pause_menu]


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()


    draw_actors_action = DrawActorsAction(output_service)



    # TODO: Create additional actions here and add them to the script

    script["input"] = [Control_Actors_Action()]
    script["update"] = [Move_Actors_Action(),
                        Handle_Off_Screen_Action(),
                        Handle_Collisions_Action(physics_service,audio_service)]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter");
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
