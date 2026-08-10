from util.gui_refresher import Gui_Refresher
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from serra.view.ui_serra import Ui_Serra
from PyQt5.QtWidgets import QWidget, QLabel
from settore.view.vista_settore import Vista_Settore
from serra.controller.contr_serra import Contr_Serra
from functools import partial

'''
    Implementazione della classe Vista Serra
    Implementa la vista della serra
'''

class Vista_Serra(QWidget):
    
    '''
        Istanzia le immagini da visualizzare nella view
    '''

    def load_imgs(self):
        self.mywidth = 200
        self.myheight = 200
        self.ok_img = QPixmap("img/ok.png").scaled(self.mywidth, 
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.alert_img = QPixmap("img/alert.png").scaled(self.mywidth, 
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.empty_img = QPixmap("img/empty.png").scaled(self.mywidth, 
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
    '''
        Istanzia la vista serra
        Parametri:
            (int) id, id del settore
    '''                             

    def inspect_settore(self,id,event):
        vista = Vista_Settore(self,self.main_window, id)
        self.main_window.addWidget(vista)
        self.main_window.setCurrentWidget(vista)
    
    '''
        Istanzia il thread che esegue il refresh della gui
    '''

    def start_gui_refresher(self):
        self.thread = Gui_Refresher()
        self.thread.refresh_signal.connect(self.refresh_gui)
        self.thread.start()

    '''
        Esegue il refresh della gui
        E' connessa al segnale emesso dal QThread Gui_Refresher
        istanziato da util.simple_window.start_gui_refresher(self)

        Percorso delle funzioni chiamate:
            util.time_refresher.get_time(self)
            serra.controller.contr_serra.get_id_settori(self)
            serra.controller.contr_serra.get_empty_flags(self)
            serra.controller.contr_serra.get_ok_flags(self,time)
    '''

    def refresh_gui(self):
        time = self.parent_ui.time_thread.get_time()
        for id_settore, empty_flag, ok_flag in zip( self.controller.get_id_settori(),
                                                    self.controller.get_empty_flags(),
                                                    self.controller.get_ok_flags(time)):
            name = "Settore {}".format(id_settore)
            self.ui.alert_label_serra[name].setScaledContents(True)
            
            if not ok_flag:
                self.ui.alert_label_serra[name].setStyleSheet("background-color: yellow")
                self.ui.alert_label_serra[name].setPixmap(self.alert_img)
            elif empty_flag:
                self.ui.alert_label_serra[name].setStyleSheet("background-color: white")
                self.ui.alert_label_serra[name].setPixmap(self.empty_img)
            else:
                self.ui.alert_label_serra[name].setStyleSheet("background-color: white")
                self.ui.alert_label_serra[name].setPixmap(self.ok_img)

    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso della funzione chiamata:
            serra.view.ui_serra.setup_ui(self,ui)
            util.simple_window.start_gui_refresher(self)
    '''

    def __init__(self,parent_ui,main_window):
        super(Vista_Serra,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Serra()
        self.ui = Ui_Serra()
        self.ui.setup_ui(self)
        
        self.load_imgs()
        self.start_gui_refresher()
        
        self.id_settori = self.controller.get_id_settori()
        numero_settori = len(self.id_settori)

        for i in range(numero_settori):
            self.ui.settori[i].mousePressEvent = partial(self.inspect_settore,self.id_settori[i])
            label = self.ui.settori[i].findChildren(QLabel, "nome_settore")[0]
            name = "Settore {}".format(self.id_settori[i])
            alert_label = self.ui.settori[i].findChildren(QLabel,"alert_label")[0]
            alert_label.setObjectName(name)
            self.ui.alert_label_serra[name] = alert_label
            label.setText(name)