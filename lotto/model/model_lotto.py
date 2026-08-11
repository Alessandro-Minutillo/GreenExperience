from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe
from colture.model.lista_soluzioni import Lista_Soluzioni
from colture.model.lista_profili_luce import Lista_Profili_Luce
from util.simple_model import Simple_Model
from colture.model.lista_colture import Lista_Colture
from attuatore_generico.luce_reg.model.lista_luce_reg import Lista_Luce_Reg
from centralina.model.lista_centraline import Lista_Centraline
from datetime import datetime, timedelta
from math import exp
from produttività.model.lista_prod import Lista_Prod
from produttività.model.model_prod import Model_Prod
import locale


# Model di un lotto coltivato: gestisce ciclo colturale, salute e raccolta.
class Model_Lotto(Simple_Model):

    # Carica il lotto con coltura, attuatori collegati e le date di ciclo/operazione.
    def __init__(self, id):
        super().__init__("Lotto",id)
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
        self.salute_threshold = 50
        ret = self.retrieve_data("Settore","id_coltura, id_pompa","id",self.info["id_settore"])

        id_coltura = ret["id_coltura"]
        id_pompa = ret["id_pompa"]

        self.coltura = Lista_Colture().get_by_id(id_coltura)
        self.centralina = Lista_Centraline().get_by_id(self.info["id_centralina"])
        self.luce_reg = Lista_Luce_Reg().get_by_id(self.info["id_luce_reg"])
        self.pompa = Lista_Pompe().get_by_id(id_pompa)

        id_soluzione =    self.retrieve_data("Coltura", "id_soluzione_circolante", "id",id_coltura )["id_soluzione_circolante"]
        id_profilo_luce = self.retrieve_data("Coltura", "id_profilo_luce", "id",id_coltura)["id_profilo_luce"]

        self.profilo_luce = Lista_Profili_Luce().get_by_id(id_profilo_luce)
        self.soluzione = Lista_Soluzioni().get_by_id(id_soluzione)

        try:
                self.data_op = datetime.strptime(self.info["data_op"], "%d %b %Y, %a %H:%M")
        except Exception as e:
                self.data_op = None
        try:
            self.inizio = datetime.strptime(self.info["data_inizio"],"%d %b %Y, %a %H:%M")
            self.fine = datetime.strptime(self.info["data_fine"], "%d %b %Y, %a %H:%M")
        except Exception as e:
            self.inizio = None
            self.fine = None

    # Restituisce l'id della coltura del lotto.
    def get_id_coltura(self):
        return self.coltura.get_id()

    # Restituisce l'id del settore che contiene il lotto.
    def get_id_settore(self):
        return self.info["id_settore"]

    # Restituisce la soglia di salute minima ammessa.
    def get_salute_threshold(self):
        return self.salute_threshold

    # Restituisce la durata media della coltura (giorni).
    def get_durata(self):
        return self.coltura.get_durata()

    # Restituisce l'id dell'impianto di illuminazione del lotto.
    def get_luce_id(self):
        return self.luce_reg.get_id()

    # Restituisce l'id della centralina del lotto.
    def get_centralina_id(self):
        return self.centralina.get_id()

    # Restituisce lo stato del lotto (vuoto/piantando/coltivato/raccogliendo).
    def get_status(self):
        return self.info["status"]

    # Imposta lo stato del lotto.
    def set_status(self, new_status):
        self.info["status"] = new_status

    # Restituisce l'indicatore di salute del lotto.
    def get_salute(self):
        return float(self.info["salute"])

    # Imposta l'indicatore di salute del lotto.
    def set_salute(self,new_salute):
        self.info["salute"] = new_salute

    # Restituisce la fase fenologica attuale.
    def get_fasef(self):
        return self.info["fase_fenologica"]

    # Imposta la fase fenologica.
    def set_fasef(self, new_fasef):
        self.info["fase_fenologica"] = new_fasef

    # Restituisce la luce consigliata per la fase fenologica attuale.
    def get_luce_cons(self):
        if self.get_fasef() == "mancante" :
            return "mancante"
        else:
            return self.profilo_luce.get_luce_per_fase(self.get_fasef())

    # Restituisce la data di inizio coltivazione.
    def get_inizio(self):
        return self.info["data_inizio"]

    # Imposta la data di inizio coltivazione ("mancante" se None).
    def set_inizio(self, new_inizio):
        self.inizio = new_inizio
        if new_inizio is None:
            self.info["data_inizio"] = "mancante"
        else:
            self.info["data_inizio"] = datetime.strftime(new_inizio,"%d %b %Y, %a %H:%M")

    # Restituisce la data prevista per la raccolta.
    def get_fine(self):
        return self.info["data_fine"]

    # Imposta la data prevista per la raccolta ("mancante" se None).
    def set_fine(self, new_fine):
        self.fine = new_fine
        if new_fine is None:
            self.info["data_fine"] = "mancante"
        else:
            self.info["data_fine"] = datetime.strftime(new_fine,"%d %b %Y, %a %H:%M")

    # Restituisce le note del lotto.
    def get_note(self):
        return self.info["note"]

    # Imposta le note del lotto.
    def change_note(self,note):
        self.info["note"] = note

    # Cambia la coltura del lotto.
    def change_coltura(self,id_coltura):
        self.coltura = Lista_Colture().get_by_id(id_coltura)

    # True se il lotto è coltivato.
    def is_full(self):
        return self.info["status"] == "coltivato"

    # True se il lotto è in fase di raccolta.
    def is_raccogliendo(self):
        return self.info["status"] == "raccogliendo"

    # True se il lotto è in fase di piantumazione.
    def is_piantando(self):
        return self.info["status"] == "piantando"

    # True se il lotto è vuoto.
    def is_empty(self):
        return self.info["status"] == "vuoto"

    # Restituisce la data dell'operazione in corso (piantumazione o raccolta).
    def get_data_op(self):
        return self.info["data_op"]

    # Imposta la data dell'operazione in corso ("mancante" se None).
    def set_data_op(self, new_data_op):
        self.data_op = new_data_op
        if new_data_op is None:
            self.info["data_op"] = "mancante"
        else:
            self.info["data_op"] = datetime.strftime(new_data_op,"%d %b %Y, %a %H:%M")

    # Avvia la raccolta se il lotto è coltivato e in fase riproduttiva; restituisce l'esito.
    def raccogli(self, time):
        flag = self.is_full() and self.get_fasef() == "riproduttiva"
        if flag:
            self.set_data_op(time)
            self.set_status("raccogliendo")
        return flag

    # Avvia la piantumazione se il lotto è vuoto; restituisce l'esito.
    def pianta(self, time):
        flag = self.is_empty()
        if flag:
            self.set_data_op(time)
            self.set_status("piantando")
        return flag

    # Calcola la salute del lotto in base a parametri ambientali, soluzione, luce e ritardo di raccolta.
    def calc_health(self, time_diff):

        temp = float(self.centralina.get_temp())
        umid = float(self.centralina.get_umid())
        liv_co2 = float(self.centralina.get_liv_co2())

        temp_cons = float(self.coltura.get_temp_cons())
        umid_cons = float(self.coltura.get_umid_cons())
        liv_co2_cons = float(self.coltura.get_co2_cons())

        flag_pompa = self.centralina.get_flag_pompa()

        luce = str(self.luce_reg.get_luce())
        fase = str(self.get_fasef())
        luce_cons = str(self.profilo_luce.get_luce_per_fase(fase))
        luce_flag = self.luce_reg.get_switch()

        sol_cons = self.soluzione.get_id()
        sol = self.pompa.get_sol().get_id()

        w_temp = abs(temp-temp_cons)/temp_cons
        w_umid = abs(umid-umid_cons)/umid_cons
        w_liv_co2 = abs(liv_co2-liv_co2_cons)/liv_co2_cons
        w_luce = 0 if luce == luce_cons and luce_flag else 0.16
        w_pompa = 0 if sol == sol_cons and flag_pompa else 0.16
        delta = min(-time_diff/(3600*24*7) - 1, 0)
        w_time = exp(4*delta) if time_diff < 0 else 0

        salute = min(92.5, max(7.5 , (1 - w_time - w_temp - w_umid - w_liv_co2 - w_luce - w_pompa)*100))
        return salute

    # Crea e registra un nuovo prodotto raccolto, con quantità pesata su salute e tempestività.
    def stock_prod(self, time):
        salute = self.get_salute()
        durata = timedelta(days = self.get_durata())
        time_fact = max(0.0, 1.0 - float((time - self.fine).total_seconds()) / float(durata.total_seconds()))
        salute_fact = salute / 100.0
        quant = float (self.coltura.get_prod_per_lotto()) * salute_fact * time_fact
        last_id=Lista_Prod().get_last_id()
        new_prod = Model_Prod()
        new_prod.set_new_model(last_id+1, self.get_id(), self.coltura.get_id(), quant, datetime.strftime(time,"%d %b %Y, %a %H:%M"))
        Lista_Prod().add(new_prod)

    # Fa avanzare il ciclo del lotto: completa operazioni, aggiorna fase fenologica e salute.
    def update(self, time):

        day = timedelta(days = 1)
        if self.data_op is not None and time > self.data_op + day:

            if self.get_status() == "raccogliendo":
                self.stock_prod(self.data_op + day)
                self.set_status("vuoto")
                self.set_inizio(None)
                self.set_fine(None)


            if self.get_status() == "piantando":
                self.set_status("coltivato")
                self.set_inizio(self.data_op + day)
                self.set_fine(self.inizio + timedelta( days = int(self.coltura.get_durata())))

            self.set_data_op(None)

        if self.inizio is not None and self.fine is not None:

            if self.get_status() == "coltivato":
                time_delta = timedelta( days = int(self.coltura.get_durata()) ) * 0.5

                if self.fine > time:
                    time_diff = (self.fine - time).total_seconds()
                else:
                    time_diff = -(time-self.fine).total_seconds()

                if time < self.inizio + time_delta:
                    self.set_fasef("vegetativa")
                else :
                    self.set_fasef("riproduttiva")

                self.set_salute(self.calc_health(time_diff))

        else :
            self.set_fasef("mancante")
            self.set_salute(0)

    # True se esiste una luce consigliata e quella impostata non vi corrisponde.
    def is_oor(self):
        return self.get_luce_cons() != "mancante" and self.luce_reg.get_luce() != self.get_luce_cons()
