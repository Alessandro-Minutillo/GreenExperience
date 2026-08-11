from account.view.ui_account import Ui_Account
from account.controller.contr_account import Contr_Account
from PyQt5.QtWidgets import QWidget, QApplication
from util.simple_window import Simple_Window


# Vista dell'account: modifica di username e password con relativi controlli.
class Vista_Account(Simple_Window):

    # Legge i campi password, applica il cambio se valido e pulisce i campi.
    def set_password(self):
        vecchia_password = self.ui.vecchia_password_field.text()
        nuova_password = self.ui.nuova_password_field.text()
        conferma_nuova_password = self.ui.conferma_password_field.text()
        self.ui.label_errore_2.setText(self.controller.controllo_password(vecchia_password, nuova_password, conferma_nuova_password))
        if (self.ui.label_errore_2.text()=="Password cambiata con successo!"):
            self.controller.cambia_password(nuova_password)
            self.ui.vecchia_password_field.setText("")
            self.ui.nuova_password_field.setText("")
            self.ui.conferma_password_field.setText("")

    # Legge il campo username, applica il cambio se valido e pulisce il campo.
    def set_username(self):
        nuovo_username = self.ui.username_field.text()
        self.ui.label_errore_1.setText(self.controller.controllo_username(nuovo_username))
        if(self.ui.label_errore_1.text()=="Username cambiato con successo!"):
            self.controller.cambia_username(nuovo_username)
            self.ui.username_field.setText("")

    # Costruisce la UI e collega i pulsanti di applicazione delle modifiche.
    def __init__(self,parent_ui,main_window,id):
        super(Vista_Account,self).__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.ui = Ui_Account()
        self.controller = Contr_Account(id)
        self.ui.setup_ui(self)
        self.start_time_refresher(self.ui.data_ora)
        self.ui.indietro.clicked.connect(self.go_back)

        self.ui.applica_modifiche.clicked.connect(self.set_username)
        self.ui.applica_modifiche_2.clicked.connect(self.set_password)
