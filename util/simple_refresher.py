from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep

'''
    Implementazione della classe Simple_Refresher
    Implementa un thread che emette un segnale periodicamente in loop
    Definisce un'interfaccia per i qthread
'''

class Simple_Refresher(QThread):

    refresh_signal = pyqtSignal()

    '''
        Costruttore
        Parametri:
            (int) x, istanti di clock che il thread deve aspettare
                    per emettere nuovamente il segnale
    '''

    def __init__(self, x):
        super().__init__()
        self.clock = 0.1
        self.multiplier = x
        self.sleep_time = self.clock * self.multiplier
        self.run_flag = True
        self.started.connect(self.on_started)
        self.finished.connect(self.on_finished)

    '''
        Funzione eseguita quando il thread inizia
    '''

    def on_started(self):
        pass
        #print("Thread " + str(self) + " iniziato")
    
    '''
        Funzione eseguita quando il thread finisce
    '''

    def on_finished(self):
        self.run_flag = True
        #print("Thread " + str(self) + " finito")

    '''
        Setta a True il parametro abort
    '''

    def abort(self):
        self.run_flag = False
    
    '''
        Ritorna il tempo di attesa del thread
    '''

    def get_sleep_time(self):
        return self.sleep_time

    '''
        Implementa il loop principale del thread
    '''

    def run(self):
        self.eta = 0
        while self.run_flag:
            if self.eta == 0:
                try:
                    self.refresh_signal.emit()
                except Exception as e: print("Errore in simple_refresher\n" + str(e))
            self.eta = (self.eta + 1) % self.multiplier
            sleep(self.clock)