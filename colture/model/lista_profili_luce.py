from colture.model.model_profilo_luce import Model_Profilo_Luce
from util.lista import Lista
from util.singleton import Singleton


# Lista singleton dei profili luce (tabella "Profilo_Luce").
@Singleton
class Lista_Profili_Luce(Lista):

    def __init__(self):
        super().__init__(Model_Profilo_Luce,"Profilo_Luce")
