from game.actions.action import Action

class Change_Bullet(Action):
    """
    Gets and input 0-9 and set the type of 
    shot player 2 is firing to that type
    """
    def __init__(self,input_servce):
        self._input_service = input_servce

    def execute(self, cast):
        if len(cast["p2_ship"]) == 0:
            return
            
        p2 = cast["p2_ship"][0]

        new_type = self._input_service.get_number_key()
        if (new_type != -1):
            p2.set_bullet_type(new_type)
