from util.simple_model import Simple_Model

"""
    Implementazione della classe Model_Account

    Contiene l'implementazioni fondamentali necessarie alla gestione dell'account

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""

class Model_Account(Simple_Model):

    def __init__(self, id):
        super().__init__("Account",id)

    """
        Restituisce l'attributo info di model_account relativo al campo "password"
        Return:
            Stringa rappresentante l'attributo info di model_account relativo al campo "password"
    """
    def recupera_password_attuale(self):
        return self.info["password"]

    """
        Restituisce l'attributo info di model_account relativo al campo "username"
        Return:
            Stringa rappresentante l'attributo info di model_account relativo al campo "username"
    """
    def recupera_username_attuale(self):
        return self.info["username"]
       
    """
        Cambia il valore dell'attributo info di model_account relativo al campo "username" con il valore passato
        Parametri:
            nuovo_username: Stringa che rappresenta il nuovo username che si vuole inserire
        Return:
            Nessuno
    """
    def cambia_username(self, nuovo_username):
        self.info["username"]=nuovo_username

    """
        Cambia il valore dell'attributo info di model_account relativo al campo "password" con il valore passato
        Parametri:
            nuova_password: Stringa che rappresenta la password che si vuole inserire
        Return:
            Nessuno
    """
    def cambia_password(self, nuova_password):
        self.info["password"]=nuova_password
    
    """
        Verifica che il cambio della password sia lecito, soddisfacendo tutti i vincoli sotto elencati
        Percorso della funzione richiamata:
            account.model.model_account.recupera_password_attuale()
        Parametri:
            vecchia_password: Stringa che rappresenta la password attuale
            nuova_password: Stringa che rappresenta la password che si vuole inserire
            conferma_nuova_password: Stringa per confermare la password che si vuole inserire
        Return:
            Stringa rappresentante il tipo di errore che si è riscontrato nel voler cambiare la password
            o l'eventuale successo dell'operazione
    """
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

    """
        Verifica che il cambio dello username sia lecito, soddisfacendo tutti i vincoli sotto elencati
        Parametri:
            nuovo_username: Stringa che rappresenta il nuovo username che si vuole inserire
        Return:
            Stringa rappresentante il tipo di errore che si è riscontrato nel voler cambiare lo username
            o l'eventuale successo dell'operazione
    """
    def controllo_username(self, nuovo_username):
        if (nuovo_username==""):
            messaggio_errore="Inserire il nuovo username"
        else:
            messaggio_errore="Username cambiato con successo!"
        return messaggio_errore
        