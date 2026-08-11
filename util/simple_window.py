from datetime import datetime
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStyle
from PyQt5.QtWidgets import QStyleOption
from PyQt5.QtGui import QPainter
from util.time_refresher import Time_Refresher
from util.gui_refresher import Gui_Refresher
import locale


# Widget base delle view: gestisce i thread di refresh e la navigazione.
class Simple_Window(QWidget):

    # Ridisegna lo sfondo del widget applicando lo stile QSS.
    def paintEvent(self, pe):
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, o, p, self)

    # Inizializza il locale e la lista dei thread della view.
    def __init__(self):
        super().__init__()
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
        self.thread_list = []

    # Registra un thread tra quelli gestiti dalla view.
    def add_thread(self,thread):
        self.thread_list.append(thread)

    # Avvia tutti i thread della view.
    def activate_threads(self):
        for th in self.thread_list:
            th.start()

    # Ferma tutti i thread della view.
    def abort_threads(self):
        for th in self.thread_list:
            th.abort()

    # Torna alla view precedente rimuovendo quella corrente dallo stack.
    def go_back(self):
        self.abort_threads()
        self.main_window.removeWidget(self.main_window.currentWidget())

    # Avvia i thread della view quando questa viene mostrata.
    def showEvent(self,event):
        self.activate_threads()

    # Ferma i thread della view quando questa viene nascosta.
    def hideEvent(self,event):
        self.abort_threads()

    # Aggiorna la label con data e ora correnti.
    def print_data(self):
        self.data_label.setText(datetime.strftime(self.time_thread.get_time(), "%d %b %Y, %a %H:%M"))

    # Avvia il thread che aggiorna data e ora nella label indicata.
    def start_time_refresher(self, data_label):
        self.time_thread = Time_Refresher()
        self.data_label = data_label
        self.time_thread.refresh_signal.connect(self.print_data)
        self.time_thread.start()
        self.add_thread(self.time_thread)

    # Avvia il thread che esegue il refresh periodico della view.
    def start_gui_refresher(self):
        thread = Gui_Refresher()
        thread.refresh_signal.connect(self.refresh_gui)
        thread.start()
        self.add_thread(thread)
