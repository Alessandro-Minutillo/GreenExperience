from util.db_connector import DB_Connector

'''
    Implementazione della classe Simple_Model
    Definisce un'interfaccia per tutti i model
'''

class Simple_Model():
    
    '''
        Costruttore
        Parametri:
            (string) table, tabella del database
            (int) id, id dell'oggetto
    '''

    def __init__(self, table, id = None):
        self.id = id
        self.table = table
        self.info = {}
        
        self.updatable_flag = self.table != "Consumo" and self.table != "Prodotto"
        self.insert_flag = id is None

        if id is not None:
            self.info = self.retrieve_data(table, "*", "id", id)
    
    '''
        Restituisce l'id dell'oggetto
        Return:
            (int) id
    '''

    def get_id(self):
        return self.id
    
    '''
        Setta una proprietà dell'oggetto presente nell'attributo self.info
        Parametri:
            (string) key, nome della proprietà;
            (object) val, valore della proprietà 
    '''

    def set_property(self, key, val):
        if key in self.info.keys():
            self.info[key] = val
    
    '''
        Restituisce una proprietà dell'oggetto presente nell'attributo self.info
        Parametri:
            (string) key, nome della proprietà;
        Return:
            (object) valore della proprietà
    '''

    def get_property(self, key):

        if key in self.info.keys():
            return self.info[key]

        return None

    '''
        Restituisce l'attributo self.info
        Return:
            (dict) info
    '''

    def get_info(self):
        return self.info        
    
    '''
        Acquisisce dati dal database eseguendo una query SELECT
        Parametri:
            (bool) mode_flag
            (string) table, tabella del database;
            (string) values, campi della tabella da acquisire;
            (string) cond_field, campo della tabella sul quale è presente una condizione;
            (string) cond_value, valore che il campo della tabella deve assumere
        Return:
            (dict) dizionario
    '''

    def retrieve(self, mode_flag, table, values = "*", cond_field = None, cond_value = None):
        ret = None
        cursor = DB_Connector().get_cursor()
        
        if cond_field is None:
            select_query = "SELECT {} FROM {}".format(values,table)
        else:
            select_query = "SELECT {} FROM {} WHERE {} = {}".format(values,table, cond_field, cond_value)
        
        cursor.execute(select_query) 
        if mode_flag:
            row = cursor.fetchone()
            if row is not None:
                ret = dict(zip([c[0] for c in cursor.description], row))
        else:
            ret = cursor.fetchall()
        
        return ret

    '''
        Acquisisce dati dal database eseguendo una query SELECT
        Ritorna solo la prima istanza
        Parametri:
            (bool) mode_flag
            (string) table, tabella del database;
            (string) values, campi della tabella da acquisire;
            (string) cond_field, campo della tabella sul quale è presente una condizione;
            (string) cond_value, valore che il campo della tabella deve assumere
        Return:
            (dict) dizionario
    '''

    def retrieve_data(self, table, values = "*", cond_field = None, cond_value = None):
        return self.retrieve(True, table, values, cond_field, cond_value)
    
    '''
        Acquisisce dati dal database eseguendo una query SELECT
        Ritorna tutte le istanze
        Parametri:
            (bool) mode_flag
            (string) table, tabella del database;
            (string) values, campi della tabella da acquisire;
            (string) cond_field, campo della tabella sul quale è presente una condizione;
            (string) cond_value, valore che il campo della tabella deve assumere
        Return:
            (dict) dizionario
    '''
    

    def retrieve_all_data(self, table, values = "*", cond_field = None, cond_value = None):
        return self.retrieve(False, table, values, cond_field, cond_value)
    
    '''
        Salva i dati del model nel databse eseguendo una query INSERT o una query UPDATE
    '''

    def save_data(self):
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        size = len(self.info.keys()) - 1

        if self.insert_flag:
            insert_query = "INSERT INTO {} ".format(self.table) 
            columns = "("
            values = "VALUES ("
            for k, key in enumerate(self.info.keys()):
                columns += str(key) + ("" if k == size else " , ")
                values += "'" + str(self.info[key]) + "'" + ("" if k == size else " , ")
            columns += ")"
            values += ")"
            insert_query += columns + " " + values
            #print(insert_query)
            cursor.execute(insert_query)
            sqliteConnection.commit()
            
        elif self.updatable_flag:
            update_query = " UPDATE {} SET ".format(self.table)
            
            for k, key in enumerate(self.info.keys()):
                update_query += key + " = '" + str(self.info[key]) + "'" + (" " if k == size else " , ")

            update_query += "WHERE id = {}".format(self.get_id())
            #print(update_query)
            cursor.execute(update_query)
            sqliteConnection.commit()