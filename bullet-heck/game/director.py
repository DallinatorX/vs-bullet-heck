
import raylibpy
from game import constants
from game.services.input_service import InputService
from game.actors.player_one_ship import Player_One_Ship
from game.actors.player_two_ship import Player_Two_Ship



class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast : The game actors {key: name, value: object}
        _script: The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast: The game actors {key: tag, value: list}.
            script: The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        self._input_service = InputService()
        
    def start_game(self):
        """
        Starts the game loop to control the sequence of play.
        """
        self.handle_welcome_screen()
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            #handles the window closeing
            if raylibpy.window_should_close():
                self._keep_playing = False


            #handles Gameovers
            if len(self._cast["p2_ship"]) == 0 :
                self.handle_gameover_screen(1)
            if len(self._cast["p1_ship"]) == 0 :
                self.handle_gameover_screen(2)



    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)



    def handle_welcome_screen(self):
        """
        Shows the welcome screen at the start of the game.
        It uses Input service and call the Welcome Screen class
        """
        pressed_enter = False
        welcome_screen = self._cast["welcome_screen"][0]
        while not pressed_enter:
            self._cue_action("output")
            pressed_enter = self._input_service.is_enter_down()
            if raylibpy.window_should_close():
                self._keep_playing = False
                pressed_enter = True
        welcome_screen.close_welcome_screen()


    def handle_gameover_screen(self, winner):
        """
        Shows the Game over screen and who won,
        It then lets the players decied if they 
        want to play again

        uses input service and the gameover screen class
        
        Winner is just a 1 or a 2 telling who won
        """
        gameover_screen = self._cast["gameover_screen"][0]
        gameover_screen.open_gameover_screen(winner)

        #Close the Game
        if self._input_service.get_key_press() == "n":
            self._keep_playing = False

        #Restart the Game
        if self._input_service.get_key_press() == "y":
            if winner == 1:
                p2_ship = Player_Two_Ship()
                self._cast["p2_ship"] = [p2_ship]
            if winner == 2:
                p1_ship = Player_One_Ship()
                self._cast["p1_ship"] = [p1_ship]
                self._cast["p2_ship"][0].set_hp(constants.P2_HP)
            gameover_screen.close_gameover_screen()

