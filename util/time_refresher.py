from util.clock import Clock
from util.simple_refresher import Simple_Refresher


# Thread che aggiorna periodicamente data e ora mostrate nelle view.
class Time_Refresher(Simple_Refresher):

    multiplier = 5

    def __init__(self):
        super().__init__(self.multiplier)

    # Restituisce l'orario di sistema corrente.
    def get_time(self):
        return Clock().get_cur_time()
