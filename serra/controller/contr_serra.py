from serra.model.model_serra import Model_Serra


# Controller della serra: tramite tra le viste e Model_Serra.
class Contr_Serra():

    def __init__(self):
        self.model = Model_Serra()

    # Restituisce gli id dei settori della serra.
    def get_id_settori(self):
        return self.model.get_ids()

    # Restituisce, per ogni settore, True se è privo di problemi al tempo dato.
    def get_ok_flags(self, time):
        return self.model.get_ok_flags(time)

    # Restituisce, per ogni settore, True se è completamente vuoto.
    def get_empty_flags(self):
        return self.model.get_empty_flags()

    # Restituisce il model della serra.
    def get_model(self):
        return self.model
