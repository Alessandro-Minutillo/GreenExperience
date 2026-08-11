from account.model.lista_account import Lista_Account


# Controller dell'account: tramite tra Vista_Account e Model_Account.
class Contr_Account():

    def __init__(self,id):
        self.model = Lista_Account().get_by_id(id)

    # Valida il cambio password e restituisce il messaggio di esito.
    def controllo_password(self, vecchia_password, nuova_password, conferma_nuova_password):
        return self.model.controllo_password(vecchia_password, nuova_password, conferma_nuova_password)

    # Valida il cambio username e restituisce il messaggio di esito.
    def controllo_username(self, nuovo_username):
        return self.model.controllo_username(nuovo_username)

    # Imposta un nuovo username.
    def cambia_username(self,nuovo_username):
        self.model.cambia_username(nuovo_username)

    # Imposta una nuova password.
    def cambia_password(self, nuova_password):
        self.model.cambia_password(nuova_password)

    # Restituisce lo username attuale.
    def get_username(self):
        return self.model.recupera_username_attuale()
