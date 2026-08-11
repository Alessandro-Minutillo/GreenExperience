from util.simple_window import Simple_Window
from login.view.ui_login import Ui_Login
from home.view.vista_home import Vista_Home
from login.controller.contr_login import Contr_Login


# Vista di login: accesso come guest o come admin con credenziali.
class Vista_Login(Simple_Window):

    # Accede in modalità guest e apre la home.
    def on_guest_click(self):
        self.ui.error_label.clear()
        self.ui.edit_username.clear()
        self.ui.edit_password.clear()
        self.main_window.mode = "guest"
        vista = Vista_Home(self,self.main_window, None)
        self.main_window.addWidget(vista)
        self.main_window.setCurrentWidget(vista)

    # Autentica come admin e apre la home, o mostra un errore se le credenziali sono errate.
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

    # Costruisce la UI e collega i pulsanti admin e guest.
    def __init__(self, parent_ui, main_window):
        super(Vista_Login,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.controller = Contr_Login()
        self.ui = Ui_Login()
        self.ui.setup_ui(self)
        self.ui.adminbutton.clicked.connect(self.on_admin_click)
        self.ui.guestbutton.clicked.connect(self.on_guest_click)
