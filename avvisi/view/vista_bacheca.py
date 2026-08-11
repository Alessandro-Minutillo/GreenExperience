from avvisi.view.notifica_vuota import Notifica_Vuota
from util.gui_refresher import Gui_Refresher
from avvisi.view.ui_bacheca import Ui_Bacheca
from PyQt5.QtWidgets import QListWidgetItem, QWidget


# Vista base di una bacheca: lista di notifiche con refresh periodico.
class Vista_Bacheca(QWidget):

    # Costruisce la UI della bacheca con il titolo indicato.
    def __init__(self, parent_ui, main_window, title):
        super().__init__()
        self.parent_ui = parent_ui
        self.main_window = main_window
        self.title = title
        self.ui = Ui_Bacheca()
        self.ui.setup_ui(self)

    # Avvia il thread di refresh della GUI.
    def start_gui_refresher(self):
            self.thread = Gui_Refresher(100)
            self.thread.refresh_signal.connect(self.refresh_gui)
            self.thread.start()

    # Mostra una notifica vuota se la bacheca non contiene notifiche.
    def fill_empty_list(self):
        if not self.ui.list_notify.count():
            self.add_widget(Notifica_Vuota(self, self.main_window))

    # Inserisce un widget notifica nella QListWidget della bacheca.
    def add_widget(self, widget):
        item = QListWidgetItem()
        item.setSizeHint(widget.sizeHint())
        self.ui.list_notify.addItem(item)
        self.ui.list_notify.setItemWidget(item,widget)
