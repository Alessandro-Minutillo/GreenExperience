from PyQt5.QtWidgets import QApplication
from util.main_window import Main_Window
import locale
import sys
import faulthandler; faulthandler.enable()
import os

'''
    Implementazione del main
'''

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    #setta la working dir a quella in cui si trova main.py
    app = QApplication(sys.argv)
    style="./coolstyles/darkmode.qss"
    with open(style,"r") as file:
        app.setStyleSheet(file.read())
    window = Main_Window()
    window.show()
    app.exec_()