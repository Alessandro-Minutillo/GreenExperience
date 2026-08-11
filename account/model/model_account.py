from util.simple_model import Simple_Model


# Model dell'account: gestisce username, password e la loro validazione.
class Model_Account(Simple_Model):

    def __init__(self, id):
        super().__init__("Account",id)

    # Restituisce la password attuale.
    def recupera_password_attuale(self):
        return self.info["password"]

    # Restituisce lo username attuale.
    def recupera_username_attuale(self):
        return self.info["username"]

    # Imposta un nuovo username.
    def cambia_username(self, nuovo_username):
        self.info["username"]=nuovo_username

    # Imposta una nuova password.
    def cambia_password(self, nuova_password):
        self.info["password"]=nuova_password

    # Valida il cambio password e restituisce il messaggio di errore o di successo.
    def controllo_password(self, vecchia_password, nuova_password, conferma_nuova_password):
        if(vecchia_password==""):
            messaggio_errore="Inserire la vecchia password"
        elif(nuova_password==""):
            messaggio_errore="Inserire la nuova password"
        elif(conferma_nuova_password==""):
            messaggio_errore="Confermare la nuova password"
        elif(vecchia_password!=self.recupera_password_attuale()):
            messaggio_errore="Vecchia password non corretta"
        elif (nuova_password==vecchia_password):
            messaggio_errore="Inserire una password diversa dalla precedente"
        elif (nuova_password!=conferma_nuova_password):
            messaggio_errore="Errore nella conferma della password"
        else:
            messaggio_errore="Password cambiata con successo!"
        return messaggio_errore

    # Valida il cambio username e restituisce il messaggio di errore o di successo.
    def controllo_username(self, nuovo_username):
        if (nuovo_username==""):
            messaggio_errore="Inserire il nuovo username"
        else:
            messaggio_errore="Username cambiato con successo!"
        return messaggio_errore
