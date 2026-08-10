from util.simple_window import Simple_Window
from login.view.ui_login import Ui_Login
from home.view.vista_home import Vista_Home
from login.controller.contr_login import Contr_Login

'''
    Implementazione della Vista Login
    Implementa la vista login
'''

class Vista_Login(Simple_Window):

    '''
        Istanzia la vista home quando si accede come guest
        Viene richiamata al click sul bottone guest
    '''

    def on_guest_click(self):
        self.ui.error_label.clear()
        self.ui.edit_username.clear()
        self.ui.edit_password.clear()
        self.main_window.mode = "guest"
        vista = Vista_Home(self,self.main_window, None)
        self.main_window.addWidget(vista)
        self.main_window.setCurrentWidget(vista)

    '''
        Istanzia la vista home quando si accede come admin
        Viene richiamata al click sul bottone admin
    '''

    def on_admin_click(self):
        user = self.ui.edit_username.text()
        pwd =  self.ui.edit_password.text()
        if self.controller.autenticate(user, pwd):
            self.ui.error_label.clear()
            self.ui.edit_username.clear()
            self.ui.edit_password.clear()
            self.main_window.mode = "admin"
            vista = Vista_Home(self,self.main_window,self.controller.get_id(user,pwd))
            self.main_window.addWidget(vista)
            self.main_window.setCurrentWidget(vista)
        else :
            self.ui.error_label.setText('username o password errati')
    
    '''
        Costruttore
        Parametri:
            (QWidget) parenti_ui, vista parent;
            (QStackedWidget) main_window, QStackedWidget
        Percorso della funzione chiamata:
            login.view.ui_login.setup_ui(self,ui)
    '''

    def __init__(self, parent_ui, main_window):
        super(Vista_Login,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Login()
        self.ui = Ui_Login()
        self.ui.setup_ui(self)
        self.ui.adminbutton.clicked.connect(self.on_admin_click)
        self.ui.guestbutton.clicked.connect(self.on_guest_click)