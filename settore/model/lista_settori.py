from settore.model.model_settore import Model_Settore
from util.lista import Lista
from util.singleton import Singleton


# Lista singleton dei settori (tabella "Settore").
@Singleton
class Lista_Settori(Lista):

    def __init__(self):
        super().__init__(Model_Settore, "Settore")
