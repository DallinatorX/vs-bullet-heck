import os
os.environ['RAYLIB_BIN_PATH'] = "./bullet-heck/lib/raylib"

import random
from game import constants
from game.director import Director
from game.actors.actor import Actor
from game.services.point import Point
from game.actions.draw_actors_action import DrawActorsAction
from game.services.input_service import InputService
from game.services.output_service import OutputService
from game.services.physics_service import PhysicsService
from game.services.audio_service import AudioService
from game.actions.move_actors_action import Move_Actors_Action
from game.actions.handle_off_screen_action import Handle_Off_Screen_Action
from game.actions.control_actors_action import Control_Actors_Action
from game.actions.handle_collisions_action import Handle_Collisions_Action
from game.actors.pause_menu_actor import Pause_Menu_Actor
from game.actors.player_one_ship import Player_One_Ship
from game.actors.player_two_ship import Player_Two_Ship
from game.actors.bullet import Bullet
from game.actions.fire_bullet import Fire_Bullet
from game.actors.hp import Hp
from game.actions.update_hp import Update_Hp
from game.actions.bullet_patterns.angle_fire_right_pattern import Angle_Fire_Right_Pattern
from game.actions.bullet_patterns.angle_fire_left_pattern import Angle_Fire_Left_Pattern
from game.actions.change_bullet import Change_Bullet
from game.actions.bullet_patterns.circle_fire_pattern import Circle_Fire





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

    cast["bullets"] = []

    helth = Hp()
    cast["hp"] = [helth]


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()


    draw_actors_action = DrawActorsAction(output_service)
    


    # TODO: Create additional actions here and add them to the script

    script["input"] = [Control_Actors_Action(),
                        Fire_Bullet(input_service),
                        Angle_Fire_Right_Pattern (input_service),
                        Angle_Fire_Left_Pattern (input_service),
                        Change_Bullet(input_service),
                        Circle_Fire(input_service) ]

    script["update"] = [Move_Actors_Action(),
                        Handle_Off_Screen_Action(),
                        Handle_Collisions_Action(physics_service,audio_service),
                        Update_Hp()]

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
