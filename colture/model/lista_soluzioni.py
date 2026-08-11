from colture.model.model_soluzione import Model_Soluzione
from util.lista import Lista
from util.singleton import Singleton


# Lista singleton delle soluzioni circolanti (tabella "Soluzione_Circolante").
@Singleton
class Lista_Soluzioni(Lista):

    def __init__(self):
        super().__init__(Model_Soluzione,"Soluzione_Circolante")
