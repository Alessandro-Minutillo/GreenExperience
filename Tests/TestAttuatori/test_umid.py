import sqlite3
from unittest import TestCase
from util.db_connector import DB_Connector
from attuatore_generico.umid.model.lista_umid import Lista_Umid

class Test_Umid(TestCase):

    def setUp(self):
        sql = "INSERT OR REPLACE INTO Umid VALUES(5, 70, 300, 'True')" 
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="INSERT OR REPLACE INTO Settore VALUES(5, 1, 1, 5, 5, 5, 5)"
        cursor.execute(sql)
        sqliteConnection.commit()
        self.umid=Lista_Umid()
    
    def tearDown(self):
        sql = "DELETE FROM Umid WHERE id=5 "
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="DELETE FROM Settore WHERE id_umid=5"
        cursor.execute(sql)
        sqliteConnection.commit()

    def test_liv_cons(self):
        self.assertEqual(self.umid.get_by_id(5).get_umid_ob(), 70, "Error")
        
    def test_onoff(self):
        self.assertTrue(self.umid.get_by_id(5).get_switch())

    
