from game.action import Action

class Update_Hp(Action):
    def execute(self, cast):
        Hp = cast["hp"][0]
        if len(cast["p1_ship"]) == 0 or len(cast["p2_ship"]) == 0:
            Hp.set_Hp(0)
            return
        p2 = cast["p2_ship"][0]
        Hp.set_Hp(p2.get_hp())
