from centralina.model.model_centralina import Model_Centralina
from util.lista import Lista
from util.singleton import Singleton


# Lista singleton delle centraline (tabella "Centralina").
@Singleton
class Lista_Centraline(Lista):

    def __init__(self):
        super().__init__(Model_Centralina, "Centralina")
