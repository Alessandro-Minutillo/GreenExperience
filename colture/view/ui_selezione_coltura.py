from PyQt5.QtWidgets import QComboBox, QVBoxLayout

# GUI della vista di selezione coltura: una combo box.
class Ui_Selezione_Coltura():

    # Costruisce la combo box di selezione coltura sulla vista passata.
    def setup_ui(self,ui):
       ui.setObjectName("widget_selezione_coltura")
       layout = QVBoxLayout()
       self.combo_coltura = QComboBox()
       layout.addWidget(self.combo_coltura)
       ui.setLayout(layout)