from account.model.lista_account import Lista_Account

"""
    Implementazione della classe Contr_Account

    Contiene i richiami delle funzioni definite nella classe Model_Account
    Costituisce il tramite tra la classe Model_Account e la classe Vista_Account

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""
class Contr_Account():
    
    def __init__(self,id):
        self.model = Lista_Account().get_by_id(id)

    """
        Restituisce il risultato della funzione controllo_password presente nel model
        Percorso della funzione richiamata: 
            account.model.model_account.controllo_password(vecchia_password, nuova_password, conferma_nuova_password)
        Parametri: 
            vecchia_password: Stringa che rappresenta la password attuale
            nuova_password: Stringa che rappresenta la password che si vuole inserire
            conferma_nuova_password: Stringa per confermare la password che si vuole inserire
        Return:
            Stringa contenente il messaggio di errore/successo
    """
    def controllo_password(self, vecchia_password, nuova_password, conferma_nuova_password):
        return self.model.controllo_password(vecchia_password, nuova_password, conferma_nuova_password)


    """
        Restituisce il risultato della funzione controllo_username presente nel model
        Percorso della funzione richiamata: 
            account.model.model_account.controllo_username(nuovo_username)
        Parametri: 
            nuovo_username: Stringa che rappresenta il nuovo username che si vuole inserire
        Return:
            Stringa contenente il messaggio di errore/successo
    """
    def controllo_username(self, nuovo_username):
        return self.model.controllo_username(nuovo_username)


    """
        Esegue la funzione cambia_username presente nel model
        Percorso della funzione richiamata: 
            account.model.model_account.cambia_username(nuovo_username)
        Parametri: 
            nuovo_username: Stringa che rappresenta il nuovo username che si vuole inserire
        Return:
            Nessun return 
    """
    def cambia_username(self,nuovo_username):
        self.model.cambia_username(nuovo_username)


    """
        Esegue la funzione cambia_password presente nel model
        Percorso della funzione richiamata: 
            account.model.model_account.cambia_password(nuova_password)
        Parametri: 
            nuova_password: Stringa che rappresenta la nuova password che si vuole inserire
        Return:
            Nessun return 
    """
    def cambia_password(self, nuova_password):
        self.model.cambia_password(nuova_password)
    

    """
        Restituisce il risultato della funzione get_username presente nel model
        Percorso della funzione richiamata:
            account.model.model_account.get_username()
        Parametri:
            Nessun parametro
        Return:
            Restituisce la stringa rappresentante lo username attuale
    """
    def get_username(self):
        return self.model.recupera_username_attuale()