from util.db_connector import DB_Connector


# Collezione generica di model, indicizzati per id e caricati dal database.
class Lista():

    # Carica dalla tabella gli id esistenti e istanzia un oggetto class_ per ciascuno.
    def __init__(self,class_,table):
        self.lista = {}
        self.class_ = class_

        cursor = DB_Connector().get_cursor()
        query = "SELECT id from {}".format(table)
        cursor.execute(query)
        d_items = cursor.fetchall()

        for d in d_items:
            self.lista[int(d["id"])] = class_(int(d["id"]))

        self.last_id = max(self.lista.keys()) if self.lista else 0

    # Aggiunge un elemento alla lista e aggiorna l'ultimo id usato.
    def add(self, item):
        self.last_id = int(item.get_id())
        self.lista[self.last_id] = item

    # Restituisce l'id più alto tra gli elementi della lista.
    def get_last_id(self):
       return self.last_id

    # Restituisce il dizionario {id: oggetto} di tutti gli elementi.
    def get_all(self):
        return self.lista

    # Restituisce l'elemento con l'id indicato.
    def get_by_id(self,id):
        return self.lista[int(id)]

    # Propaga update() a tutti gli elementi della lista.
    def update(self, *args, **kwargs):
        for val in self.lista.values():
            val.update(*args, **kwargs)

    # Propaga recalc() a tutti gli elementi (ricalcolo stato all'avvio).
    def recalc(self, *args, **kwargs):
        for val in self.lista.values():
            val.recalc(*args, **kwargs)

    # Salva su database tutti gli elementi della lista.
    def save_all(self):
        for val in self.lista.values():
            val.save_data()
