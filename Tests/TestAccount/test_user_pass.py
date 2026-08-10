import sqlite3
from unittest import TestCase
from util.db_connector import DB_Connector
from account.model.lista_account import Lista_Account

class Test_User_Pass(TestCase):

    def setUp(self):
        sql = "INSERT INTO Account VALUES(2, 'vecchio_username', 'vecchia_password', 1)" 
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()
        self.account = Lista_Account()

    def tearDown(self):
        sql = "DELETE FROM Account WHERE id=2"
        cursor = DB_Connector().get_cursor()
        sqliteConnection = DB_Connector().get_connection()
        cursor.execute(sql)
        sqliteConnection.commit()

    def test_password(self):
        self.assertEqual(self.account.get_by_id(2).controllo_password(self.account.get_by_id(2).recupera_password_attuale(), "nuova_password", "nuova_password"), "Password cambiata con successo!", "Error")

    def test_username(self):
        self.assertEqual(self.account.get_by_id(2).controllo_username(self.account.get_by_id(2).recupera_username_attuale()), "Username cambiato con successo!", "Error")

    def test_autenticate(self):
        self.assertTrue(self.account.autenticate("vecchio_username", "vecchia_password"))
        
    def test_errore_password_1(self):
        self.assertEqual(self.account.get_by_id(2).controllo_password("", "nuova_password", "nuova_password"), "Inserire la vecchia password")

    def test_errore_password_2(self):
        self.assertEqual(self.account.get_by_id(2).controllo_password("vecchia_password", "", "nuova_password"), "Inserire la nuova password")

    def test_errore_password_3(self):
        self.assertEqual(self.account.get_by_id(2).controllo_password("vecchia_password", "nuova_password", ""), "Confermare la nuova password")
    
    def test_errore_password_4(self):
        self.assertEqual(self.account.get_by_id(2).controllo_password("vecchia_password_non_corretta", "nuova_password", "nuova_password"), "Vecchia password non corretta")
    
    def test_errore_password_5(self):
        self.assertEqual(self.account.get_by_id(2).controllo_password("vecchia_password", "vecchia_password", "vecchia_password"), "Inserire una password diversa dalla precedente")
        
    def test_errore_password_6(self):
        self.assertEqual(self.account.get_by_id(2).controllo_password("vecchia_password", "nuova_password", "nuova_password_non_corretta"), "Errore nella conferma della password")
    
    def test_errore_username_1(self):
        self.assertEqual(self.account.get_by_id(2).controllo_username(""), "Inserire il nuovo username")
    