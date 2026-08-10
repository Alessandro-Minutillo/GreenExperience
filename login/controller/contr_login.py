from account.model.lista_account import Lista_Account

'''
    Implementazione della classe Contr_Login
    Implementa un controller per la gestione del login
'''

class Contr_Login():

    '''
        Costruttore
    '''
    def __init__(self):
        self.model = Lista_Account()

    '''
        Tenta l'autenticazione con username e password inseriti
        Parametri:
            (string) username;
            (string) password
        Percorso della funzione chiamata:
            account.model.lista_account.autenticate(self,username,password)
    '''

    def autenticate(self,username,password):
        return self.model.autenticate(username,password)
    
    '''
        Restituisce l'id relativo all'account al quale si è autenticati
        Parametri:
            (string) username;
            (string) password
        Percorso della funzione chiamata:
            account.model.lista_account.get_id(self,username,password)
    '''

    def get_id(self, username, password):
        return self.model.get_id(username,password)