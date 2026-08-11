from lotto.model.lista_lotti import Lista_Lotti
from datetime import datetime
import locale


# Controller di un lotto: tramite tra la vista e Model_Lotto.
class Contr_Lotto():

    def __init__(self,id):
        self.model = Lista_Lotti().get_by_id(id)
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")

    # Restituisce l'id dell'impianto di illuminazione del lotto.
    def get_luce_id(self):
        return self.model.get_luce_id()

    # Restituisce l'id della centralina del lotto.
    def get_centralina_id(self):
        return self.model.get_centralina_id()

    # Restituisce l'indicatore di salute del lotto.
    def get_salute(self):
        return self.model.get_salute()

    # Restituisce lo stato del lotto.
    def get_status(self):
        return self.model.get_status()

    # Restituisce la fase fenologica del lotto.
    def get_fasef(self):
        return self.model.get_fasef()

    # Restituisce la luce consigliata per il lotto.
    def get_luce_cons(self):
        return self.model.get_luce_cons()

    # Restituisce la data di inizio coltivazione formattata gg/mm/aaaa.
    def get_inizio(self):
        return "mancante" if self.model.get_inizio() == "mancante" else datetime.strftime( datetime.strptime(self.model.get_inizio(), "%d %b %Y, %a %H:%M") , "%d/%m/%Y")

    # Restituisce la data di raccolta prevista formattata gg/mm/aaaa.
    def get_fine(self):
        return "mancante" if self.model.get_fine() == "mancante" else datetime.strftime( datetime.strptime(self.model.get_fine(), "%d %b %Y, %a %H:%M") , "%d/%m/%Y")

    # Restituisce le note del lotto.
    def get_note(self):
        return self.model.get_note()

    # Imposta le note del lotto.
    def change_note(self,note):
        self.model.change_note(note)

    # Restituisce il model del lotto.
    def get_model(self):
        return self.model

    # Pianta il lotto; restituisce l'esito.
    def pianta(self, time):
        return self.model.pianta(time)

    # Raccoglie il lotto; restituisce l'esito.
    def raccogli(self, time):
        return self.model.raccogli(time)

    # True se il lotto è coltivato o in fase di raccolta.
    def is_full_or_raccogliendo(self):
        return self.model.is_full() or self.model.is_raccogliendo()
