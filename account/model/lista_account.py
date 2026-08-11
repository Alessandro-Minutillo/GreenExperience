from account.model.model_account import Model_Account
from util.lista import Lista
from util.singleton import Singleton


# Lista singleton degli account registrati (tabella "Account").
@Singleton
class Lista_Account(Lista):

    def __init__(self):
        super().__init__(Model_Account, "Account")

    # True se esiste un account con lo username e la password indicati.
    def autenticate(self, username, password):
        return any(d.recupera_username_attuale() == username and d.recupera_password_attuale() == password for d in self.lista.values())

    # Restituisce l'id dell'account corrispondente a username e password.
    def get_id(self, username, password):
        for d in self.lista.values():
            if(d.recupera_username_attuale() == username and d.recupera_password_attuale() == password):
                return d.get_id()
