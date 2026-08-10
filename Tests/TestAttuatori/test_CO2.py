import sqlite3
from unittest import TestCase
from util.db_connector import DB_Connector
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2

class Test_CO2(TestCase):

    def setUp(self):
        sql = "INSERT OR REPLACE INTO SerbCO2 VALUES(5, 700, 123, 'True')" 
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="INSERT OR REPLACE INTO Settore VALUES(5, 1, 1, 5, 5, 5, 5)"
        cursor.execute(sql)
        sqliteConnection.commit()
        self.co2 = Lista_SerbCO2()
    
    def tearDown(self):
        sql = "DELETE FROM SerbCO2 WHERE id=5 "
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="DELETE FROM Settore WHERE id_serbco2=5"
        cursor.execute(sql)
        sqliteConnection.commit()

    def test_liv_cons(self):
        self.assertEqual(self.co2.get_by_id(5).get_co2_ob(), 700, "Error")
        
    def test_onoff(self):
        self.assertTrue(self.co2.get_by_id(5).get_switch())

    
