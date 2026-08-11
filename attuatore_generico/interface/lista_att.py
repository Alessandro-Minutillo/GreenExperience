from util.lista import Lista


# Lista base di attuatori generici; estende util.lista.
class Lista_Att(Lista):

    def __init__(self, class_, table):
        super().__init__(class_, table)

    # Dizionario {id: True se spento, False se acceso} per ogni attuatore.
    def get_diz_off(self):
        return { d.get_id() : not d.get_switch() for d in self.lista.values()}

    # Dizionario {id: True se fuori dai valori consigliati} per ogni attuatore.
    def get_diz_oor(self):
        return { d.get_id() : d.is_oor() for d in self.lista.values()}
