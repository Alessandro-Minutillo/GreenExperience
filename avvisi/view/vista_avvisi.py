from avvisi.view.ui_avvisi import Ui_Avvisi
from util.simple_window import Simple_Window


# Vista avvisi: contiene le tre bacheche di notifiche (attuatori, lotti, pianta/raccogli).
class Vista_Avvisi(Simple_Window):

    # Costruisce la UI, avvia i thread delle bacheche e collega il pulsante indietro.
    def __init__(self,parent_ui,main_window):
        super().__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.ui = Ui_Avvisi()
        self.ui.setup_ui(self)

        self.start_time_refresher(self.ui.data_label)
        self.add_thread(self.ui.bacheca1.thread)
        self.add_thread(self.ui.bacheca2.thread)
        self.add_thread(self.ui.bacheca3.thread)
        self.ui.indietro.clicked.connect(self.go_back)
