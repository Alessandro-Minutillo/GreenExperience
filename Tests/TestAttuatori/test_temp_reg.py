import sqlite3
from unittest import TestCase
from util.db_connector import DB_Connector
from attuatore_generico.temp_reg.model.lista_temp_reg import Lista_Temp_Reg


# Test dei getter del regolatore di temperatura (temperatura obiettivo, stato) su dati di prova.
class Test_Temp_Reg(TestCase):

    # Inserisce regolatore e settore di prova e carica la lista regolatori.
    def setUp(self):
        sql = "INSERT OR REPLACE INTO Temp_Reg VALUES(5, 20, 300, 'True')"
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="INSERT OR REPLACE INTO Settore VALUES(5, 1, 1, 5, 5, 5, 5)"
        cursor.execute(sql)
        sqliteConnection.commit()
        self.temp = Lista_Temp_Reg()

    # Rimuove regolatore e settore di prova.
    def tearDown(self):
        sql = "DELETE FROM Temp_Reg WHERE id=5 "
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="DELETE FROM Settore WHERE id_temp_reg=5"
        cursor.execute(sql)
        sqliteConnection.commit()

    # get_temp_ob restituisce la temperatura obiettivo memorizzata.
    def test_liv_cons(self):
        self.assertEqual(self.temp.get_by_id(5).get_temp_ob(), 20, "Error")

    # Il regolatore di prova risulta acceso.
    def test_onoff(self):
        self.assertTrue(self.temp.get_by_id(5).get_switch())
