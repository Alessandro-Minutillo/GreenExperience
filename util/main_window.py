from datetime import datetime
from PyQt5.QtCore import Qt
from util.db_connector import DB_Connector
from PyQt5.QtWidgets import QMessageBox, QStackedWidget, QDesktopWidget, QStackedWidget
from login.view.vista_login import Vista_Login
from util.updater import Updater


# Finestra principale: stack di view dell'applicazione, parte dalla schermata di login.
class Main_Window(QStackedWidget):

    # Centra la finestra sullo schermo.
    def centerOnScreen(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    # Avvia il thread Updater e mostra la view di login.
    def __init__(self):
        super().__init__()
        self.resize(1080,720)
        self.update_thread = Updater()
        self.update_thread.start()
        self.centerOnScreen()
        self.addWidget(Vista_Login(None,self))
        self.setWindowTitle("Green Experience")
        self.show()

    # Ferma i thread e salva lo stato del programma sul database.
    def save(self):
        window = self.currentWidget()
        window.abort_threads()
        self.update_thread.abort()
        self.update_thread.save()
        DB_Connector().close_connection()

    # Chiede conferma alla chiusura: se confermata salva ed esce, altrimenti annulla.
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
