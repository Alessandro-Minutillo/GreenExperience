from datetime import datetime
from util.simple_model import Simple_Model
from lotto.model.lista_lotti import Lista_Lotti
from attuatore_generico.temp_reg.model.lista_temp_reg import Lista_Temp_Reg
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2
from attuatore_generico.umid.model.lista_umid import Lista_Umid
from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe
from colture.model.lista_colture import Lista_Colture
import locale


# Model di un settore: aggrega lotti, coltura e attuatori, e ne valuta lo stato e i consumi.
class Model_Settore(Simple_Model):

    # Carica i lotti, la coltura e gli attuatori del settore.
    def __init__(self, id):
        super().__init__("Settore", id)
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
        id_lotti = self.retrieve_all_data("Lotto","id",'id_settore',id)
        self.lotti = [ Lista_Lotti().get_by_id(d["id"]) for d in id_lotti]
        self.coltura = Lista_Colture().get_by_id(self.info["id_coltura"])
        self.temp_reg = Lista_Temp_Reg().get_by_id(self.info["id_temp_reg"])
        self.umid = Lista_Umid().get_by_id(self.info["id_umid"])
        self.serbCO2 = Lista_SerbCO2().get_by_id(self.info["id_serbco2"])
        self.pompa = Lista_Pompe().get_by_id(self.info["id_pompa"])

    # Restituisce la lista dei model dei lotti del settore.
    def get_lotti(self):
        return self.lotti

    # Restituisce l'id dell'umidificatore del settore.
    def get_id_umid(self):
        return self.umid.get_id()

    # Restituisce l'id del regolatore di temperatura del settore.
    def get_id_temp_reg(self):
        return self.temp_reg.get_id()

    # Restituisce l'id del serbatoio di CO2 del settore.
    def get_id_serbCO2(self):
        return self.serbCO2.get_id()

    # Restituisce gli id di tutti i lotti del settore.
    def get_ids(self):
        return [d.get_id() for d in self.lotti]

    # Restituisce lo stato di tutti i lotti del settore.
    def get_status_lotti(self):
        return [d.get_status() for d in self.lotti]

    # Restituisce la salute di tutti i lotti del settore.
    def get_salute_lotti(self):
        return [d.get_salute() for d in self.lotti]

    # Restituisce le soglie di salute minima di tutti i lotti del settore.
    def get_soglia_salute_lotti(self):
        return [d.get_salute_threshold() for d in self.lotti]

    # Restituisce le date di raccolta previste di tutti i lotti del settore.
    def get_date_fine(self):
        return [d.get_fine() for d in self.lotti]

    # Restituisce il nome della coltura del settore.
    def get_name_coltura(self):
        return self.coltura.get_name()

    # Raccoglie tutti i lotti raccoglibili; restituisce il numero di lotti raccolti.
    def raccogli_tutto(self, time):
        num = 0
        for l in self.lotti:
            if l.raccogli(time):
                num += 1
        return num

    # Pianta la coltura nei lotti disponibili; restituisce il numero di lotti piantati.
    def pianta_tutto(self, id_coltura, time):
        num = 0
        old_id_coltura = self.lotti[0].get_id_coltura()
        cond1 = not any([not l.is_empty() for l in self.lotti])
        for l in self.lotti:
            cond2 = cond1 or old_id_coltura == id_coltura
            if cond1:
                l.change_coltura(id_coltura)
            if cond2:
                if l.pianta(time):
                    num += 1
        return num

    # Cambia la coltura del settore e la propaga agli attuatori.
    def change_coltura(self,id_coltura):
        self.info["id_coltura"] = id_coltura
        self.coltura = Lista_Colture().get_by_id(id_coltura)
        self.serbCO2.set_coltura(self.coltura)
        self.umid.set_coltura(self.coltura)
        self.temp_reg.set_coltura(self.coltura)
        self.pompa.set_coltura(self.coltura)

    # True se nessun lotto ha problemi e tutti gli attuatori sono sui valori consigliati.
    def is_ok(self, time):

        return (not any(
                            [
                                lotto.get_status() == 'coltivato' and
                                (
                                    lotto.get_salute() < lotto.get_salute_threshold() or
                                    ( lotto.get_fine() != "mancante" and datetime.strptime(lotto.get_fine(), "%d %b %Y, %a %H:%M") < time )
                                )
                            for lotto in self.lotti
                            ]
                        )) and (not self.serbCO2.is_oor()) and (not self.umid.is_oor()) and (not self.temp_reg.is_oor()) and (not self.pompa.is_oor())

    # True se tutti i lotti del settore sono vuoti.
    def is_empty(self):
        return not any([lotto.get_status() != 'vuoto'
                            for lotto in self.lotti])

    # True se la pompa è accesa.
    def is_pompa_on(self):
        return self.pompa.get_switch()

    # True se il serbatoio di CO2 è acceso.
    def is_serb_on(self):
        return self.serbCO2.get_switch()

    # True se il regolatore di temperatura è acceso.
    def is_temp_reg_on(self):
        return self.temp_reg.get_switch()

    # True se l'umidificatore è acceso.
    def is_umid_on(self):
        return self.umid.get_switch()

    # True se la pompa non è impostata sui valori consigliati.
    def is_pompa_oor(self):
        return self.pompa.is_oor()

    # True se il serbatoio di CO2 non è impostato sui valori consigliati.
    def is_serb_oor(self):
        return self.serbCO2.is_oor()

    # True se il regolatore di temperatura non è impostato sui valori consigliati.
    def is_temp_reg_oor(self):
        return self.temp_reg.is_oor()

    # True se l'umidificatore non è impostato sui valori consigliati.
    def is_umid_oor(self):
        return self.umid.is_oor()

    # Restituisce il model della coltura del settore.
    def get_coltura(self):
        return self.coltura

    # Consumo elettrico totale del settore: attuatori più illuminazione dei lotti.
    def get_cons_el(self):
        electric=self.pompa.get_consumo_el()+self.umid.get_consumo()+self.temp_reg.get_consumo()+self.serbCO2.get_consumo()
        consumoluce=0
        for i in  self.lotti:
            consumoluce+=i.luce_reg.get_consumo()
        electric+=consumoluce
        return electric

    # Consumo idrico totale del settore (pompa).
    def get_cons_idro(self):
        return self.pompa.get_consumo_idro()
