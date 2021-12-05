import os
os.environ['RAYLIB_BIN_PATH'] = "./bullet-heck/lib/raylib"

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
from game.player_one_ship import Player_One_Ship
from game.player_two_ship import Player_Two_Ship
from game.bullet import Bullet
from game.fire_bullet import Fire_Bullet





def main():
    # create the cast {key: tag, value: list}
    cast = {}

    # bricks = [] 

    # cast["bricks"] = bricks

    # ball = []

    # cast["ball"] = [ball]
    # paddle = []

    # cast["paddle"] = [paddle]
    pause_menu = Pause_Menu_Actor()
    cast["pause_menu"] = [pause_menu]

    p1_ship = Player_One_Ship()
    cast["p1_ship"] = [p1_ship]

    p2_ship = Player_Two_Ship()
    cast["p2_ship"] = [p2_ship]

    bullet = Bullet()
    bullet.set_player(2)
    cast["bullets"] = [bullet]


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()


    draw_actors_action = DrawActorsAction(output_service)
    


    # TODO: Create additional actions here and add them to the script

    script["input"] = [Control_Actors_Action(),
                        Fire_Bullet(input_service)]
    script["update"] = [Move_Actors_Action(),
                        Handle_Off_Screen_Action(),
                        Handle_Collisions_Action(physics_service,audio_service)]
    script["output"] = [draw_actors_action]


    # Start the game
    output_service.open_window("Bullet \"Nether\" (BYUI Safe)");
    audio_service.start_audio()
    #audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
