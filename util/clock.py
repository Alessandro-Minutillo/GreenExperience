from datetime import datetime, timedelta
from util.simple_model import Simple_Model
from util.singleton import Singleton
import locale


# Orologio di sistema singleton: gestisce il tempo simulato dell'applicazione.
@Singleton
class Clock(Simple_Model):

    # Calcola l'orario corrente simulato a partire dall'ultimo salvataggio e dal moltiplicatore.
    def __init__(self,id = 1):
       super().__init__("Tempo",id)
       locale.setlocale(locale.LC_TIME,"it_IT.utf8")
       self.clock = 0.5
       self.fact = float(self.info["multiplier"])
       self.user_time = datetime.strptime(self.info["usertime"],"%d %b %Y, %a %H:%M")
       self.now_time = datetime.now()
       time_delta = timedelta( seconds = self.get_time_diff_sec() ) * self.fact
       self.cur_time = datetime.strptime(self.info["realtime"], "%d %b %Y, %a %H:%M" ) + time_delta

    # Secondi reali trascorsi dall'ultima chiusura del programma.
    def get_time_diff_sec(self):
        return (self.now_time - self.user_time).total_seconds()

    # Restituisce l'orario simulato corrente.
    def get_cur_time(self):
        return self.cur_time

    # Avanza l'orario simulato di un tick, scalato per il fattore di conversione.
    def tick(self):
        self.cur_time += timedelta( seconds = self.clock ) * self.fact

    # Restituisce il fattore di conversione tempo reale/simulato.
    def get_fact(self):
        return self.fact

    # Registra l'ora reale attuale come istante dell'ultimo salvataggio.
    def set_user_time(self):
        self.info["usertime"] = datetime.strftime(datetime.now(), "%d %b %Y, %a %H:%M")

    # Registra l'orario simulato corrente da persistere su database.
    def set_real_time(self):
        self.info["realtime"] = datetime.strftime(self.cur_time, "%d %b %Y, %a %H:%M")
