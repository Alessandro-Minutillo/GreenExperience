from attuatore_generico.interface.lista_att import Lista_Att
from attuatore_generico.temp_reg.model.model_temp_reg import Model_Temp_Reg
from util.singleton import Singleton


# Lista singleton dei regolatori di temperatura (tabella "Temp_Reg").
@Singleton
class Lista_Temp_Reg(Lista_Att):
    def __init__(self):
        super().__init__(Model_Temp_Reg, "Temp_Reg")
