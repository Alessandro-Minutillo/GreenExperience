from colture.model.lista_colture import Lista_Colture

'''
    Implementazione della classe Contr_Lista_Colture
    Implementa un controller per la gestione della lista di tutte le colture
'''

class Contr_Lista_Colture():

    '''
        Costruttore
    '''

    def __init__(self): 
        self.model = Lista_Colture()

    '''
        Restituisce la lista di tutte le colture
        Percorso della funzione chiamata:
            util.lista.get_all(self)
    '''

    def get_all(self):
        return self.model.get_all()

    '''
        Restituisce l'id della coltura dal nome specificato
        Parametri:
            (string) name, nome della coltura
        Return:
            (int) id, id della coltura
    '''

    def get_id_by_name(self,name):
       return self.model.get_id_by_name(name)

    '''
        Ritorna una lista dei nomi comuni di tutte le colture che contengono
        la stringa cercata (no case sensitive)
        Parametri:
            (string) string, stringa cercata
        Percorso della funzione chiamata:
            colture.model.lista_colture.search(self,string)
        Return:
            (list) lista dei nomi
    '''

    def search(self,string):
        return self.model.search(string)

    '''
        Ritorna una lista dei nomi comuni di tutte le colture
        Percorso della funzione chiamata:
            colture.model.lista_colture.get_lista_nomi_colture(self)
        Return:
            (list) lista dei nomi
    '''

    def carica_colture(self):
        return self.model.get_lista_nomi_colture()

    '''
        Ritorna una proprietà della coltura identificata dall'id
        Parametri:
            (int) id, id della coltura
            (string) prop, nome della proprietà
        Percorso della funzione chiamata:
            util.simple_model.get_property(self,prop)
        Return:
            proprietà
    '''

    def get_property(self, id, prop):
        return str(self.model.get_by_id(id).get_property(prop))
    '''
        Ritorna la soluzione circolante della coltura identificata dall'id
        Parametri:
            (int) id, id della coltura
        Percorso della funzione chiamata:
            colture.model.model_coltura.get_soluzione(self)
        Return:
            (string) soluzione formattata
    '''

    def get_soluzione(self,id):
        return self.model.get_by_id(id).get_soluzione()

    '''
        Ritorna il profilo luce della coltura identificata dall'id
        Parametri:
            (int) id, id della coltura
        Percorso della funzione chiamata:
            colture.model.model_coltura.get_profilo_luce(self)
        Return:
            (string) profilo luce formattato
    '''

    def get_profilo_luce(self,id):
        return self.model.get_by_id(id).get_profilo_luce()