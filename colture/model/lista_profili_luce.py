from colture.model.model_profilo_luce import Model_Profilo_Luce
from util.lista import Lista
from util.singleton import Singleton

'''
    Implementazione della classe Lista_Profili_Luce
    Implementa una lista di profili luce
'''

@Singleton
class Lista_Profili_Luce(Lista):

    '''
        Costruttore
    '''

    def __init__(self):
        super().__init__(Model_Profilo_Luce,"Profilo_Luce")