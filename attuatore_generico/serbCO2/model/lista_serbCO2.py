from attuatore_generico.interface.lista_att import Lista_Att
from attuatore_generico.serbCO2.model.model_serbCO2 import Model_SerbCO2
from util.singleton import Singleton

@Singleton
class Lista_SerbCO2(Lista_Att):
    def __init__(self):
        super().__init__(Model_SerbCO2, "SerbCO2")