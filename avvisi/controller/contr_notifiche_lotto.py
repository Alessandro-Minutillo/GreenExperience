from lotto.model.lista_lotti import Lista_Lotti


# Controller delle notifiche sui lotti: tramite verso Lista_Lotti.
class Contr_Notifiche_Lotto():

    def __init__(self):
        self.model = Lista_Lotti()

    # Dizionario dei lotti non raccolti entro la data prevista.
    def get_diz_time_out_lotti(self, time):
        return self.model.get_diz_time_out_lotti(time)

    # Dizionario dei lotti con salute sotto soglia.
    def get_diz_low_salute_lotti(self):
        return self.model.get_diz_low_salute_lotti()

    # Dizionario dei lotti vuoti.
    def get_diz_lotti_vuoti(self):
        return self.model.get_diz_lotti_vuoti()

    # Restituisce l'indicatore di salute del lotto indicato.
    def get_salute_lotto(self, id):
        return self.model.get_salute_lotto(id)

    # Restituisce l'id del settore del lotto indicato.
    def get_id_settore(self,id):
        return self.model.get_id_settore(id)
