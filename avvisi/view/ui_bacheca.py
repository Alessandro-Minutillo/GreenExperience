from PyQt5.QtWidgets import QAbstractItemView, QListWidget, QVBoxLayout, QGroupBox

# GUI di una bacheca: titolo e lista scorrevole di notifiche.
class Ui_Bacheca():

    # Costruisce i widget e il layout sulla vista passata.
    def setup_ui(self,ui):
     self.main_container = QVBoxLayout()
     gbox = QGroupBox(ui.title)
     gbox.setObjectName("gbox")
     layout = QVBoxLayout()
     self.list_notify = QListWidget()
     self.list_notify.setSelectionMode(QAbstractItemView.NoSelection)
     layout.addWidget(self.list_notify)
     gbox.setLayout(layout)
     self.main_container.addWidget(gbox)
     ui.setLayout(self.main_container)