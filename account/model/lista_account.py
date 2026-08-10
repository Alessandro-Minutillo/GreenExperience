from account.model.model_account import Model_Account
from util.lista import Lista
from util.singleton import Singleton

'''
    Implementazione  della classe Lista_Account
    Implementa una lista di account
'''

@Singleton
class Lista_Account(Lista):

    '''
        Costruttore
    '''

    def __init__(self):
        super().__init__(Model_Account, "Account")
    
    '''
        Restituisce True se esiste un account con username e password inseriti, False altrimenti
        Return:
            (bool) flag
    '''

    def autenticate(self, username, password):
        return any(d.recupera_username_attuale() == username and d.recupera_password_attuale() == password for d in self.lista.values())
    
    '''
        Restituisce l'id dell'account corrispondente a username e password inseriti
        Return:
            (int) id
    '''

    def get_id(self, username, password):
        for d in self.lista.values():
            if(d.recupera_username_attuale() == username and d.recupera_password_attuale() == password):
                return d.get_id()