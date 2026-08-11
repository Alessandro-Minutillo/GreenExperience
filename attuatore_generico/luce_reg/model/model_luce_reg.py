from attuatore_generico.interface.model_att import Model_Att


# Model dell'impianto di illuminazione: gestisce il tipo di luce impostato.
class Model_Luce_Reg(Model_Att):

    def __init__(self, id):
        super().__init__("Luce_Reg",id)

    # Restituisce il tipo di luce attualmente impostato.
    def get_luce(self):
        return self.info["luce"]

    # Imposta il tipo di luce dell'impianto.
    def change_luce(self,tipo):
        self.info["luce"] = tipo
