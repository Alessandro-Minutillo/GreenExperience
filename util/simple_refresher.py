from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep


# Thread base che emette periodicamente refresh_signal in loop.
class Simple_Refresher(QThread):

    refresh_signal = pyqtSignal()

    # Configura clock e moltiplicatore che determinano il periodo del segnale.
    def __init__(self, x):
        super().__init__()
        self.clock = 0.1
        self.multiplier = x
        self.sleep_time = self.clock * self.multiplier
        self.run_flag = True
        self.started.connect(self.on_started)
        self.finished.connect(self.on_finished)

    # Callback all'avvio del thread (nessuna azione).
    def on_started(self):
        pass

    # Callback alla fine del thread: riabilita il flag di esecuzione.
    def on_finished(self):
        self.run_flag = True

    # Ferma il loop del thread.
    def abort(self):
        self.run_flag = False

    # Restituisce il tempo di attesa tra due segnali.
    def get_sleep_time(self):
        return self.sleep_time

    # Loop principale: emette refresh_signal ogni multiplier tick di clock.
    def run(self):
        self.eta = 0
        while self.run_flag:
            if self.eta == 0:
                try:
                    self.refresh_signal.emit()
                except Exception as e: print("Errore in simple_refresher\n" + str(e))
            self.eta = (self.eta + 1) % self.multiplier
            sleep(self.clock)
