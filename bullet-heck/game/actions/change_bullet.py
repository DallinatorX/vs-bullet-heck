from game.actions.action import Action

class Change_Bullet(Action):
    def __init__(self,input_servce):
        self._input_service = input_servce

    def execute(self, cast):
        p2 = cast["p2_ship"][0]

        new_type = self._input_service.get_number_key()
        if (new_type != -1):
            p2.set_bullet_type(new_type)
