from serra.model.model_serra import Model_Serra

'''
    Implementazione della classe Contr_Serra
    Implementa un controller per la gestione della serra
'''

class Contr_Serra():

    '''
        Costruttore
    '''

    def __init__(self):
        self.model = Model_Serra()

    '''
        Restituisce una lista degli id dei settori presenti nella serra
        Percorso della funzione chiamata:
            serra.model.model_serra.get_ids(self)
        Return:
            (list) lista id
    '''

    def get_id_settori(self):
        return self.model.get_ids()
    
    '''
        Restituisce una lista di flag posti a True se l'iesimo settore
        è ok
        Percorso della funzione chiamata:
            serra.model.model_serra.get_ok_flags(self,time)
        Return:
            (list) lista flag
    '''

    def get_ok_flags(self, time):
        return self.model.get_ok_flags(time)
    
    '''
        Restituisce una lista di flag posti a True se l'iesimo settore
        è completamente vuoto
        Percorso della funzione chiamata:
            serra.model.model_serra.get_empty_flags(self)
        Return:
            (list) lista flag
    '''

    def get_empty_flags(self):
        return self.model.get_empty_flags()

    '''
        Ritorna il model
        Return:
            (Model_Serra) model
    '''

    def get_model(self):
        return self.model