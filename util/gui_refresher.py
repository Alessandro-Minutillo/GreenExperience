from util.simple_refresher import Simple_Refresher


# Thread dedicato al refresh periodico della GUI.
class Gui_Refresher(Simple_Refresher):

    def __init__(self, multiplier = 20):
        super().__init__(multiplier)
