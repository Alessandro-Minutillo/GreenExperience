import sqlite3
from unittest import TestCase
from util.db_connector import DB_Connector
from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe


# Test dei getter della pompa (pH, EC, consumi, stato) su dati di prova.
class Test_Pompa(TestCase):

    # Inserisce pompe e settori di prova e carica la lista pompe.
    def setUp(self):
        sql = "INSERT OR REPLACE INTO Pompa VALUES(5 , 4, 1, 3, 400, 300, 'True')"
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="INSERT OR REPLACE INTO Pompa VALUES(6, 4, 1, 3, 400, 300, 'False')"
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="INSERT OR REPLACE INTO Settore VALUES(5, 1, 1, 3, 4, 3, 5)"
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="INSERT OR REPLACE INTO Settore VALUES(6, 1, 1, 3, 4, 3, 6)"
        cursor.execute(sql)
        sqliteConnection.commit()
        self.pompa = Lista_Pompe()

    # Rimuove le pompe e i settori di prova.
    def tearDown(self):
        sql = "DELETE FROM Pompa WHERE id=5 "
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="DELETE FROM Pompa WHERE id=6 "
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="DELETE FROM Settore WHERE id=5 "
        cursor.execute(sql)
        sqliteConnection.commit()
        sql="DELETE FROM Settore WHERE id=6 "
        cursor.execute(sql)
        sqliteConnection.commit()

    # get_ph restituisce il pH memorizzato.
    def test_ph(self):
        self.assertEqual(self.pompa.get_by_id(5).get_ph(), 1, "Error")
    # get_ec restituisce l'EC memorizzato.
    def test_ec(self):
        self.assertEqual(self.pompa.get_by_id(5).get_ec(), 3, "Error")
    # Pompa accesa: consumo elettrico pari al valore nominale.
    def test_consumo_el(self):
        self.assertEqual(self.pompa.get_by_id(5).get_consumo_el(), 400, "Error")
    # Pompa spenta: consumo elettrico nullo.
    def test_consumo_el_switch(self):
        self.assertEqual(self.pompa.get_by_id(6).get_consumo_el(), 0, "Error")
    # Pompa spenta: consumo idrico nullo.
    def test_consumo_idro_switch(self):
        self.assertEqual(self.pompa.get_by_id(6).get_consumo_el(), 0, "Error")
    # Pompa accesa: consumo idrico pari al valore nominale.
    def test_consumo_idro(self):
        self.assertEqual(self.pompa.get_by_id(5).get_consumo_idro(), 300, "Error")

    # La pompa di prova risulta accesa.
    def test_onoff(self):
        self.assertTrue(self.pompa.get_by_id(5).get_switch())
