from colture.model.model_coltura import Model_Coltura
from util.lista import Lista
from util.singleton import Singleton

'''
    Implementazione della classe Lista_Colture
    Implementa una lista di colture
'''

@Singleton
class Lista_Colture(Lista):

    '''
        Costruttore
    '''

    def __init__(self):
        super().__init__(Model_Coltura,"Coltura")

    '''
        Ritorna l'id della coltura avente il nome comune specificato
        Parametri:
            (string) name, nome comune
        Percorso della funzione chiamata:
            colture.model.model_coltura.get_name(self)
        Return:
            (int) id, id della coltura
    '''

    def get_id_by_name(self,name):
        ret_id = None
        for item in self.lista.values():
            if item.get_name() == name:
                ret_id = item.get_id()
        return ret_id

    '''
        Ritorna una lista dei nomi comuni di tutte le colture
        Percorso della funzione chiamata:
            colture.model.model_coltura.get_name(self)
        Return:
            (list) lista dei nomi
    '''

    def get_lista_nomi_colture(self):
        colture = [i.get_name() for i in self.lista.values()]
        return colture

    '''
        Ritorna una lista dei nomi comuni di tutte le colture che contengono
        la stringa cercata (no case sensitive)
        Parametri:
            (string) string, stringa cercata
        Percorso della funzione chiamata:
            colture.model.model_coltura.get_name(self)
        Return:
            (list) lista dei nomi
    '''

    def search(self,string):
        colture = []
        for i in self.lista.values():
            if string.lower() in i.get_name().lower():
                colture.append(i.get_name())
        return colture