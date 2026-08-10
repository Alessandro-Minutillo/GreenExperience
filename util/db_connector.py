from util.singleton import Singleton
import sqlite3

'''
    Implementazione della classe DB_Connector
    Definisce un'interfaccia per comunicare con il database
'''

@Singleton
class DB_Connector():
    
    '''
        Costruttore
    '''

    def __init__(self):
        
        try:
            self.sqliteConnection = sqlite3.connect('db/database.db')
            self.sqliteConnection.row_factory = sqlite3.Row
            self.sqliteConnection.execute("PRAGMA journal_mode = WAL")
        
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
    
    '''
        Restituisce il cursore alla connessione con il database
        Return:
            cursore
    '''

    def get_cursor(self):
        return self.sqliteConnection.cursor()
    
    '''
        Restituisce la connessione con il database
        Return:
            connessione
    '''

    def get_connection(self):
        return self.sqliteConnection

    '''
        Chiude la connessione con il database
    '''

    def close_connection(self):
        if self.sqliteConnection:
                self.sqliteConnection.cursor().close()
                self.sqliteConnection.close()