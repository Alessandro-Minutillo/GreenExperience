from util.db_connector import DB_Connector

'''
    Implementazione della classe Lista
    Definisce un'interfaccia per una lista di oggetti
'''

class Lista():

    '''
        Costruttore
        Parametri:
            (class) class_, classe degli oggetti;
            (string) table, tabella del database
    '''

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

    '''
        Aggiunge un elemento alla lista
        Parametri:
            (object) item
    '''

    def add(self, item):
        self.last_id = int(item.get_id())
        self.lista[self.last_id] = item 

    '''
        Restituisce l'id più grande tra gli oggetti della lista
        Return:
            (int) id
    '''

    def get_last_id(self):
       return self.last_id

    '''
        Restituisce la lista
        Return:
            (dict) lista
    '''

    def get_all(self):
        return self.lista
    
    '''
        Restituisce l'elemento della lista corrispondente all'id
        Parametri:
            (int) id
        Return:
            (object) item
    '''

    def get_by_id(self,id):
        return self.lista[int(id)]

    '''
        Aggiorna tutti gli elementi della lista
    '''

    def update(self, *args, **kwargs):
        for val in self.lista.values():
            val.update(*args, **kwargs)

    '''
        Ricalcola lo stato di tutti gli elementi della lista
        all'accensione del programma
    '''

    def recalc(self, *args, **kwargs):
        for val in self.lista.values():
            val.recalc(*args, **kwargs)
    '''
        Salva tutti gli elementi della lista nel database
    '''

    def save_all(self):
        for val in self.lista.values():
            val.save_data()