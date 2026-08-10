from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from avvisi.view.vista_avvisi import Vista_Avvisi
from home.view.ui_home import Ui_Home
from consumi.view.vista_consumi import Vista_Consumi
from produttività.view.vista_prod import Vista_Prod
from account.view.vista_account import Vista_Account
from colture.view.vista_colture import Vista_Colture
from util.simple_window import Simple_Window
from account.controller.contr_account import Contr_Account

'''
    Implementazione della classe Vista_Home
    Implementa la vista home
'''

class Vista_Home(Simple_Window):
    
    '''
        Istanzia le immagini da visualizzare nella view
    '''

    def load_imgs(self):
        self.mywidth = 200
        self.myheight = 200
        self.guest_img = QPixmap("img/guest.png").scaled(self.mywidth, 
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)

        self.admin_img = QPixmap("img/admin.png").scaled(self.mywidth, 
                                                            self.myheight,
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
    '''
        Istanzia la vista notifiche
    '''

    def vedi_notifiche(self):
        Vista=Vista_Avvisi(self,self.main_window)
        self.main_window.addWidget(Vista)
        self.main_window.setCurrentWidget(Vista)

    '''
        Istanzia la vista colture
    '''

    def vedi_colture(self):
        Vista=Vista_Colture(self,self.main_window)
        self.main_window.addWidget(Vista)
        self.main_window.setCurrentWidget(Vista)
    
    '''
        Istanzia la vista produttività
    '''

    def vedi_prod(self):
        Vista=Vista_Prod(self,self.main_window)
        self.main_window.addWidget(Vista)
        self.main_window.setCurrentWidget(Vista)
    
    '''
        Istanzia la vista consumi
    '''

    def vedi_cons(self):
        Vista=Vista_Consumi(self,self.main_window)
        self.main_window.addWidget(Vista)
        self.main_window.setCurrentWidget(Vista)

    '''
        Istanzia la vista account
    '''

    def vedi_account(self):
        Vista=Vista_Account(self,self.main_window, self.id)
        self.main_window.addWidget(Vista)
        self.main_window.setCurrentWidget(Vista)
    
    '''
        Torna alla vista login
    '''

    def cambia_utente(self):
        self.main_window.removeWidget(self.main_window.currentWidget())

    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso delle funzioni chiamate:
            home.view.ui_home.setup_ui(self,ui)
            util.simple_window.add_thread(self,thread)
    '''

    def __init__(self,parent_ui,main_window, id):
        super().__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.ui = Ui_Home()
        self.id = id
        if id is not None:
            self.controller = Contr_Account(id)
        self.load_imgs()
        self.ui.setup_ui(self)
        self.start_time_refresher(self.ui.data_label)
        self.add_thread(self.ui.serra_frame.thread)
        
        if self.main_window.mode == "guest":
            self.ui.button[0].hide()
            self.ui.button[1].hide()
            self.ui.profile_pic.setPixmap(self.guest_img)
            self.ui.profile_label.setText("[guest]")
        else:
            self.ui.profile_pic.setPixmap(self.admin_img)
            self.ui.profile_label.setText("[admin] {}".format(self.controller.get_username()))

        self.ui.cambia_button.clicked.connect(self.cambia_utente)
        self.ui.button[0].clicked.connect(self.vedi_account)
        self.ui.button[1].clicked.connect(self.vedi_notifiche)
        self.ui.button[2].clicked.connect(self.vedi_colture)
        self.ui.button[3].clicked.connect(self.vedi_prod)
        self.ui.button[4].clicked.connect(self.vedi_cons)