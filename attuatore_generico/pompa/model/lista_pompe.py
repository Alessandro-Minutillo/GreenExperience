from attuatore_generico.pompa.model.model_pompa import Model_Pompa
from util.lista import Lista
from util.singleton import Singleton
from attuatore_generico.interface.lista_att import Lista_Att
@Singleton
class Lista_Pompe(Lista_Att): 
    def __init__(self):
        super().__init__(Model_Pompa,"Pompa")