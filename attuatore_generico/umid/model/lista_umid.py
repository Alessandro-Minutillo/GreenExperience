from attuatore_generico.interface.lista_att import Lista_Att
from attuatore_generico.umid.model.model_umid import Model_Umid
from util.singleton import Singleton

@Singleton
class Lista_Umid(Lista_Att):
    def __init__(self):
        super().__init__(Model_Umid, "Umid")