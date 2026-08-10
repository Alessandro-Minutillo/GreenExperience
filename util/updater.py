from util.clock import Clock
from colture.model.lista_soluzioni import Lista_Soluzioni
from colture.model.lista_profili_luce import Lista_Profili_Luce
from colture.model.lista_colture import Lista_Colture
from serra.model.model_serra import Model_Serra
from settore.model.lista_settori import Lista_Settori
from attuatore_generico.umid.model.lista_umid import Lista_Umid
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2
from attuatore_generico.temp_reg.model.lista_temp_reg import Lista_Temp_Reg
from account.model.lista_account import Lista_Account
from lotto.model.lista_lotti import Lista_Lotti
from centralina.model.lista_centraline import Lista_Centraline
from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe
from attuatore_generico.luce_reg.model.lista_luce_reg import Lista_Luce_Reg
from produttività.model.lista_prod import Lista_Prod
from util.singleton import Singleton
from util.time_refresher import Time_Refresher
from consumi.model.lista_consumi import Lista_Consumi

'''
    Implementazione della classe Updater
    Implementa un thread che si occupa di aggiornare lo stato del programma
    e dispone di una funzione di salvataggio
'''

@Singleton
class Updater(Time_Refresher):

    '''
        Costruttore
        Percorso delle funzioni chiamate:
            util.clock.get_time_diff(self)
            util.simple_refresher.get_sleep_time(self)
            util.time_refresher.get_cur_time(self)
            centralina.model.lista_centraline.recalc(self,number)
    '''

    def __init__(self):
        super().__init__()
        
        self.lim = 10
        self.eta2 = 0
        
        self.lista_prod = Lista_Prod()
        self.lista_profili_luce = Lista_Profili_Luce()
        self.lista_pompe = Lista_Pompe()
        self.lista_soluzioni = Lista_Soluzioni()
        self.lista_luce_reg = Lista_Luce_Reg()
        self.lista_temp_reg = Lista_Temp_Reg()
        self.lista_serbco2 = Lista_SerbCO2()
        self.lista_umid = Lista_Umid()
        self.lista_centraline = Lista_Centraline()
        self.lista_lotti = Lista_Lotti()
        self.lista_settori = Lista_Settori()
        self.lista_colture = Lista_Colture()
        self.lista_account = Lista_Account()
        self.serra = Model_Serra()
        self.timer = Clock()
        self.lista_consumi=Lista_Consumi()
        
        number = min(50, int( self.timer.get_time_diff_sec()/ (self.get_sleep_time() * self.lim)) )
        self.lista_centraline.recalc(number)
        self.serra.recalc(self.timer.get_cur_time())
        self.refresh_signal.connect(self.update)

    '''
        Funzione eseguita quando il thread emette il segnale
        Aggiorna l'orario di sistema e lo stato del programma,
        in particolare i model di centraline, lotti e serra
        Percorso delle funzioni chiamate:
            util.lista.update(self,...)
            util.clock.get_fact(self)
            util.simple_refresher.get_sleep_time(self)
    '''

    def update(self):
        self.timer.tick()
        
        if self.eta2 == 0:
            self.lista_centraline.update()
            self.lista_lotti.update(self.get_time())
            self.serra.update(self.get_time(), self.timer.get_fact() * (self.get_sleep_time() * self.lim) )
        
        self.eta2 = (self.eta2+1)% self.lim

    '''
        Salva lo stato del programma
        Percorso delle funzioni chiamate:
            util.lista.save_all(self)
            util.simple_model.save_data(self)
            util.clock.set_user_time(self)
            util.clock.set_real_time(self)
    '''

    def save(self):
        self.timer.set_user_time()
        self.timer.set_real_time()
        self.timer.save_data()
        self.lista_centraline.save_all()
        self.lista_pompe.save_all()
        self.lista_lotti.save_all()
        self.lista_luce_reg.save_all()
        self.lista_temp_reg.save_all()
        self.lista_umid.save_all()
        self.lista_serbco2.save_all()
        self.lista_settori.save_all()
        self.lista_account.save_all()
        self.lista_prod.save_all()
        self.lista_consumi.save_all()
        self.serra.save_data()