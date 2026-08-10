from datetime import datetime
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStyle
from PyQt5.QtWidgets import QStyleOption
from PyQt5.QtGui import QPainter
from util.time_refresher import Time_Refresher
from util.gui_refresher import Gui_Refresher
import locale

'''
    Implementazione della classe Simple_Window
    Definisce un'intefaccia per le view
'''

class Simple_Window(QWidget):

    '''
        Reimplementazione di paintEvent
    '''

    def paintEvent(self, pe):
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, o, p, self)
    
    '''
        Costruttore
    '''

    def __init__(self):
        super().__init__()
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
        self.thread_list = []
    
    '''
        Aggiunge un thread alla lista dei thread presenti sulla view
        Parametri:
            (QThread) thread
    '''

    def add_thread(self,thread):
        self.thread_list.append(thread)

    '''
        Riattiva tutti i thread presenti sulla view
    '''

    def activate_threads(self):
        for th in self.thread_list:
            th.start()

    '''
        Termina tutti i thread presenti sulla view
        Percorso della funzione chiamata:
            util.simple_refresher.abort(self)
    '''

    def abort_threads(self):    
        for th in self.thread_list:
            th.abort()
    '''
        Elimina la view attualmente mostrata dal QStackedWidget e
        visualizza la view precedente
    '''

    def go_back(self):
        self.abort_threads()
        self.main_window.removeWidget(self.main_window.currentWidget())

    '''
        Attiva i thread della view quando questa viene mostrata
    '''

    def showEvent(self,event):
        self.activate_threads()

    '''
        Termina i thread della view quando questa viene nascosta
    '''

    def hideEvent(self,event):
        self.abort_threads()

    '''
        Stampa data e ora corrente in una label della view
    '''

    def print_data(self):
        self.data_label.setText(datetime.strftime(self.time_thread.get_time(), "%d %b %Y, %a %H:%M"))
    
    '''
        Istanzia il thread che aggiorna data e ora nella view
    '''

    def start_time_refresher(self, data_label):
        self.time_thread = Time_Refresher()
        self.data_label = data_label
        self.time_thread.refresh_signal.connect(self.print_data)
        self.time_thread.start()
        self.add_thread(self.time_thread)
    
    '''
        Istanzia il thread che esegue il refresh della view
    '''

    def start_gui_refresher(self):
        thread = Gui_Refresher()
        thread.refresh_signal.connect(self.refresh_gui)
        thread.start()
        self.add_thread(thread)