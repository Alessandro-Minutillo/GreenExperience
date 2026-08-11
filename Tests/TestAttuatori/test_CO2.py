import sqlite3
from unittest import TestCase
from util.db_connector import DB_Connector
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2


# Test dei getter del serbatoio di CO2 (livello obiettivo, stato) su dati di prova.
class Test_CO2(TestCase):

    # Inserisce serbatoio e settore di prova e carica la lista serbatoi.
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

    # Rimuove serbatoio e settore di prova.
    def tearDown(self):
        sql = "DELETE FROM SerbCO2 WHERE id=5 "
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="DELETE FROM Settore WHERE id_serbco2=5"
        cursor.execute(sql)
        sqliteConnection.commit()

    # get_co2_ob restituisce il livello obiettivo memorizzato.
    def test_liv_cons(self):
        self.assertEqual(self.co2.get_by_id(5).get_co2_ob(), 700, "Error")

    # Il serbatoio di prova risulta acceso.
    def test_onoff(self):
        self.assertTrue(self.co2.get_by_id(5).get_switch())
