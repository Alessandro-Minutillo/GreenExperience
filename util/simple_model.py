from util.db_connector import DB_Connector


# Model base: incapsula i dati di una riga di tabella e l'accesso al database.
class Simple_Model():

    # Se id è dato carica la riga dal database; altrimenti prepara un nuovo record.
    def __init__(self, table, id = None):
        self.id = id
        self.table = table
        self.info = {}

        self.updatable_flag = self.table != "Consumo" and self.table != "Prodotto"
        self.insert_flag = id is None

        if id is not None:
            self.info = self.retrieve_data(table, "*", "id", id)

    # Restituisce l'id dell'oggetto.
    def get_id(self):
        return self.id

    # Aggiorna una proprietà in self.info se la chiave esiste.
    def set_property(self, key, val):
        if key in self.info.keys():
            self.info[key] = val

    # Restituisce il valore di una proprietà di self.info, o None se assente.
    def get_property(self, key):

        if key in self.info.keys():
            return self.info[key]

        return None

    # Restituisce il dizionario completo dei dati (self.info).
    def get_info(self):
        return self.info

    # Esegue una SELECT; con mode_flag=True torna una riga (dict), altrimenti tutte le righe.
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

    # SELECT che restituisce la prima riga come dizionario.
    def retrieve_data(self, table, values = "*", cond_field = None, cond_value = None):
        return self.retrieve(True, table, values, cond_field, cond_value)

    # SELECT che restituisce tutte le righe.
    def retrieve_all_data(self, table, values = "*", cond_field = None, cond_value = None):
        return self.retrieve(False, table, values, cond_field, cond_value)

    # Salva i dati su database: INSERT per un nuovo record, UPDATE se aggiornabile.
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
            cursor.execute(insert_query)
            sqliteConnection.commit()

        elif self.updatable_flag:
            update_query = " UPDATE {} SET ".format(self.table)

            for k, key in enumerate(self.info.keys()):
                update_query += key + " = '" + str(self.info[key]) + "'" + (" " if k == size else " , ")

            update_query += "WHERE id = {}".format(self.get_id())
            cursor.execute(update_query)
            sqliteConnection.commit()
