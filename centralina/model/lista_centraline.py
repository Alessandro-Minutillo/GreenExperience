from centralina.model.model_centralina import Model_Centralina
from util.lista import Lista
from util.singleton import Singleton

'''
    Implementazione della classe Lista_Centraline
    Implementa una lista di centraline
'''

@Singleton
class Lista_Centraline(Lista): 

    '''
        Costruttore
    '''
    
    def __init__(self):
        super().__init__(Model_Centralina, "Centralina")