from colture.model.lista_colture import Lista_Colture


# Controller della lista colture: tramite tra le viste e Lista_Colture.
class Contr_Lista_Colture():

    def __init__(self):
        self.model = Lista_Colture()

    # Restituisce tutte le colture {id: Model_Coltura}.
    def get_all(self):
        return self.model.get_all()

    # Restituisce l'id della coltura dal nome indicato.
    def get_id_by_name(self,name):
       return self.model.get_id_by_name(name)

    # Restituisce i nomi delle colture che contengono la stringa cercata.
    def search(self,string):
        return self.model.search(string)

    # Restituisce i nomi comuni di tutte le colture.
    def carica_colture(self):
        return self.model.get_lista_nomi_colture()

    # Restituisce come stringa una proprietà della coltura indicata.
    def get_property(self, id, prop):
        return str(self.model.get_by_id(id).get_property(prop))

    # Restituisce la soluzione circolante formattata della coltura indicata.
    def get_soluzione(self,id):
        return self.model.get_by_id(id).get_soluzione()

    # Restituisce il profilo luce formattato della coltura indicata.
    def get_profilo_luce(self,id):
        return self.model.get_by_id(id).get_profilo_luce()
