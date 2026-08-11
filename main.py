from PyQt5.QtWidgets import QApplication
from util.main_window import Main_Window
import locale
import sys
import faulthandler; faulthandler.enable()
import os

# Punto di ingresso: imposta locale e working dir, applica lo stile e avvia la GUI.
if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    # working dir = cartella di main.py
    app = QApplication(sys.argv)
    style="./coolstyles/darkmode.qss"
    with open(style,"r") as file:
        app.setStyleSheet(file.read())
    window = Main_Window()
    window.show()
    app.exec_()
