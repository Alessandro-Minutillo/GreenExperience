from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from lotto.view.ui_lotto import Ui_Lotto
from lotto.controller.contr_lotto import Contr_Lotto
from util.simple_window import Simple_Window

'''
    Implementazione della classe Vista_Lotto
    Implementa la vista del lotto
'''

class Vista_Lotto(Simple_Window):

    '''
        Istanzia le immagini da visualizzare nella view
    '''

    def load_imgs(self):

        self.full_lotto_img = QPixmap("img/area.png").scaled(400,400,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.empty_lotto_img = QPixmap("img/area2.png").scaled(400,400,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

    '''
        Raccoglie, se possibile, il lotto
        Viene richiamata quando si clicca sul bottone "raccogli"
        Percorso della funzione chiamata:
            util.time_refresher.get_time(self)
            lotto.controller.contr_lotto.raccogli(self,time)
            lotto.controller.contr_lotto.is_full_or_raccogliendo(self)
    '''

    def raccogli(self):
        flag = self.controller.raccogli(self.time_thread.get_time())
        if not flag:
            self.ui.error_label.setStyleSheet("color: red")
            if self.controller.is_full_or_raccogliendo():
                self.ui.error_label.setText("Il lotto è in fase vegetativa")
            else:
                self.ui.error_label.setText("Il lotto è vuoto")
        else:
            self.ui.error_label.setStyleSheet("color: #197d5a")
            self.ui.error_label.setText("raccogliendo il lotto")
            self.ui.button_raccogli.setEnabled(False)
            self.ui.button_pianta.setEnabled(False)
        
        self.clear_error_label = 1
    
    '''
        Pianta, se possibile, il lotto
        Viene richiamata quando si clicca sul bottone "pianta"
        Percorso della funzione chiamata:
            util.time_refresher.get_time(self)
            lotto.controller.contr_lotto.pianta(self,time)
    '''

    def pianta(self):
        flag = self.controller.pianta(self.time_thread.get_time())
        if not flag:
            self.ui.error_label.setStyleSheet("color: red")
            self.ui.error_label.setText("Il lotto è già coltivato")
        else:
            self.ui.error_label.setStyleSheet("color: #197d5a")
            self.ui.error_label.setText("piantando il lotto")
            self.ui.button_raccogli.setEnabled(False)
            self.ui.button_pianta.setEnabled(False)
        
        self.clear_error_label = 1

    '''
        Esegue il refresh della gui
        E' connessa al segnale emesso dal QThread Gui_Refresher
        istanziato da util.simple_window.start_gui_refresher(self)

        Percorso delle funzioni chiamate:
            lotto.controller.contr_lotto.get_salute(self)
            lotto.controller.contr_lotto.get_status(self)
            lotto.controller.contr_lotto.get_luce_cons(self)
            lotto.controller.contr_lotto.get_fasef(self)
            lotto.controller.contr_lotto.get_inizio(self)
            lotto.controller.contr_lotto.get_fine(self)
            lotto.controller.contr_lotto.is_full_or_raccogliendo(self)
    '''

    def refresh_gui(self):

        if self.clear_error_label == 2:
            self.ui.error_label.clear()

        if self.clear_error_label > 0:
            self.clear_error_label = (self.clear_error_label + 1)%3

        self.ui.status_bar.setValue(self.controller.get_salute())
        self.ui.stato_label.setText(self.controller.get_status())
        self.ui.luce_label.setText(self.controller.get_luce_cons())
        self.ui.fase_label.setText(self.controller.get_fasef())
        self.ui.inizio_label.setText(self.controller.get_inizio())
        self.ui.fine_label.setText(self.controller.get_fine())
        
        if self.controller.is_full_or_raccogliendo():
            self.ui.frame_lotto_sing.setPixmap(self.full_lotto_img)
        else:
            self.ui.frame_lotto_sing.setPixmap(self.empty_lotto_img)

    '''
        Setta le note del lotto
        Viene richiamata quando cambia il testo del campo note
        Percorso della funzione richiamata:
            lotto.controller.contr_lotto.change_note(self,text)
    '''

    def change_note(self):
    
        self.controller.change_note(self.ui.note_edit.toPlainText())
    
    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso della funzione chiamata:
            lotto.view.ui_lotto.setup_ui(self,ui)
            util.simple_window.start_time_refresher(self)
            util.simple_window.start_gui_refresher(self)
            util.simple_window.add_thread(self,thread)
    '''

    def __init__(self,parent_ui,main_window, id):
        super().__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Lotto(id)
        self.ui = Ui_Lotto()
        self.ui.setup_ui(self)
        
        self.load_imgs()
        self.clear_error_label = 0
        self.start_time_refresher(self.ui.data_label)
        self.start_gui_refresher()
        self.add_thread(self.ui.sensori_frame.thread)
        
        self.ui.lotto_text_label.setText("Lotto {}".format(id))
        self.ui.indietro.clicked.connect(self.go_back)
        self.ui.button_raccogli.clicked.connect(self.raccogli)
        self.ui.button_pianta.clicked.connect(self.pianta)

        if self.main_window.mode == "guest":
            self.ui.button_raccogli.hide()
            self.ui.button_pianta.hide()
            self.ui.note_edit.setEnabled(False)
        
        self.ui.note_edit.setText(self.controller.get_note())
        self.ui.note_edit.textChanged.connect(self.change_note)