from colture.model.model_coltura import Model_Coltura
from util.lista import Lista
from util.singleton import Singleton


# Lista singleton delle colture disponibili (tabella "Coltura").
@Singleton
class Lista_Colture(Lista):

    def __init__(self):
        super().__init__(Model_Coltura,"Coltura")

    # Restituisce l'id della coltura con il nome comune indicato.
    def get_id_by_name(self,name):
        ret_id = None
        for item in self.lista.values():
            if item.get_name() == name:
                ret_id = item.get_id()
        return ret_id

    # Restituisce i nomi comuni di tutte le colture.
    def get_lista_nomi_colture(self):
        colture = [i.get_name() for i in self.lista.values()]
        return colture

    # Restituisce i nomi delle colture che contengono la stringa cercata (case-insensitive).
    def search(self,string):
        colture = []
        for i in self.lista.values():
            if string.lower() in i.get_name().lower():
                colture.append(i.get_name())
        return colture
