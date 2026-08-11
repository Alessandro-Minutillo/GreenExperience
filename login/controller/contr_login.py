from account.model.lista_account import Lista_Account


# Controller del login: autenticazione degli account.
class Contr_Login():

    def __init__(self):
        self.model = Lista_Account()

    # Verifica le credenziali; True se corrette.
    def autenticate(self,username,password):
        return self.model.autenticate(username,password)

    # Restituisce l'id dell'account autenticato.
    def get_id(self, username, password):
        return self.model.get_id(username,password)
