from datetime import datetime, timedelta
from util.simple_model import Simple_Model
from util.singleton import Singleton
import locale

'''
    Implementazione della classe Clock
    Implementa l'orologio di sistema
'''

@Singleton
class Clock(Simple_Model):

    '''
        Costruttore
        Parametri:
            (int) id
    '''

    def __init__(self,id = 1):
       super().__init__("Tempo",id)
       locale.setlocale(locale.LC_TIME,"it_IT.utf8")
       self.clock = 0.5
       self.fact = float(self.info["multiplier"])
       self.user_time = datetime.strptime(self.info["usertime"],"%d %b %Y, %a %H:%M")
       self.now_time = datetime.now()
       time_delta = timedelta( seconds = self.get_time_diff_sec() ) * self.fact
       self.cur_time = datetime.strptime(self.info["realtime"], "%d %b %Y, %a %H:%M" ) + time_delta

    '''
        Restituisce il tempo in secondi trascorso dall'ultima esecuzione del programma
        Return:
            (int) secondi  
    '''

    def get_time_diff_sec(self):
        return (self.now_time - self.user_time).total_seconds()
    
    '''
        Restituisce il tempo attuale
        Return:
            (datetime) tempo attuale
    '''

    def get_cur_time(self):
        return self.cur_time
    
    '''
        L'orario di sistema aumenta di una quantità pari al clock per
        un fattore di conversione
    '''

    def tick(self):
        self.cur_time += timedelta( seconds = self.clock ) * self.fact
    
    '''
        Restituisce il fattore di conversione
        Return:
            (float) fattore
    '''

    def get_fact(self):
        return self.fact
    
    '''
        Setta il tempo utente
    '''

    def set_user_time(self):
        self.info["usertime"] = datetime.strftime(datetime.now(), "%d %b %Y, %a %H:%M")
    
    '''
        Setta il tempo fittizio
    '''

    def set_real_time(self):
        self.info["realtime"] = datetime.strftime(self.cur_time, "%d %b %Y, %a %H:%M")
