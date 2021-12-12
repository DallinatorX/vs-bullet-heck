from game.actions.action import Action

class Update_Hp(Action):
    """
    This gets player two's HP and gives it to 
    the HP actor that stays in the Top right
    """
    def execute(self, cast):
        Hp = cast["hp"][0]
        if len(cast["p2_ship"]) == 0:
            Hp.set_Hp(0)
            return
        p2 = cast["p2_ship"][0]
        Hp.set_Hp(p2.get_hp())
