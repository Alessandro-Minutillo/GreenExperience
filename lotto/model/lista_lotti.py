from lotto.model.model_lotto import Model_Lotto
from util.lista import Lista
from util.singleton import Singleton
from datetime import datetime
import locale


# Lista singleton dei lotti (tabella "Lotto").
@Singleton
class Lista_Lotti(Lista):

    def __init__(self):
        super().__init__(Model_Lotto, "Lotto")
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")

    # Dizionario {id: True se il lotto è coltivato e oltre la data di raccolta prevista}.
    def get_diz_time_out_lotti(self, time):
        return { d.get_id() : d.get_inizio() != "mancante" and d.get_status() != "raccogliendo" and datetime.strptime(d.get_fine(),"%d %b %Y, %a %H:%M") < time for d in self.lista.values()}

    # Dizionario {id: (True se coltivato con salute sotto soglia, valore di salute)}.
    def get_diz_low_salute_lotti(self):
        return { d.get_id() : (d.get_status() == "coltivato" and d.get_salute() < d.get_salute_threshold(), d.get_salute()) for d in self.lista.values()}

    # Dizionario {id: True se il lotto è vuoto}.
    def get_diz_lotti_vuoti(self):
        return { d.get_id() : d.get_status() == "vuoto" for d in self.lista.values() }

    # Restituisce l'indicatore di salute del lotto indicato.
    def get_salute_lotto(self, id):
        return self.lista[id].get_salute()

    # Restituisce l'id del settore del lotto indicato.
    def get_id_settore(self, id):
        return self.lista[id].get_id_settore()

    # Dizionario {id: True se l'impianto di illuminazione del lotto è spento}.
    def get_diz_off(self):
        return { d.get_id() : not d.luce_reg.get_switch() for d in self.lista.values()}

    # Dizionario {id: True se l'illuminazione del lotto non è sui valori consigliati}.
    def get_diz_oor(self):
        return { d.get_id() : d.is_oor() for d in self.lista.values()}
