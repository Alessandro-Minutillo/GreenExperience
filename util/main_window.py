from datetime import datetime
from PyQt5.QtCore import Qt
from util.db_connector import DB_Connector
from PyQt5.QtWidgets import QMessageBox, QStackedWidget, QDesktopWidget, QStackedWidget
from login.view.vista_login import Vista_Login
from util.updater import Updater

'''
    Implementazione della classe Main_Window
    Implementa la finestra principale
'''

class Main_Window(QStackedWidget):

    '''
        Centra la finestra nello schermo
    '''

    def centerOnScreen(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    '''
        Costruttore
    '''

    def __init__(self):
        super().__init__()
        t1 = datetime.now()
        self.resize(1080,720)
        self.update_thread = Updater()
        self.update_thread.start()
        self.centerOnScreen()
        self.addWidget(Vista_Login(None,self))
        self.setWindowTitle("Green Experience")
        self.show()
        t2 = datetime.now()
        #print("tempo impiegato per avviare il programma: " + str((t2-t1).total_seconds()) + " secondi")

    '''
        Salva i dati nel database, richiamando la classe Updater
    '''

    def save(self):
        window = self.currentWidget()
        t1 = datetime.now()
        window.abort_threads()
        self.update_thread.abort()
        self.update_thread.save()
        DB_Connector().close_connection()
        t2 = datetime.now()
        #print("tempo impiegato per salvare: " + str((t2-t1).total_seconds()) + " secondi")

    '''
        Istanzia un QMessageBox alla chiusura del programma
        Viene richiamata quando si clicca sulla x della finestra
    '''

    def closeEvent(self, event):

        box = QMessageBox(self)
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle('Chiusura del programma')
        box.setText('Sei sicuro di voler uscire?')
        box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        buttonY = box.button(QMessageBox.Yes)
        buttonN = box.button(QMessageBox.No)
        buttonY.setText(' Sì ')
        buttonN.setText(' No ')
        box.exec_()
        
        if box.clickedButton() == buttonY:
            event.accept()
            self.setWindowFlag(Qt.WindowCloseButtonHint, False)
            self.save()
        elif box.clickedButton() == buttonN:
            event.ignore()