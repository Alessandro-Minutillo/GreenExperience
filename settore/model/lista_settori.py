from settore.model.model_settore import Model_Settore
from util.lista import Lista
from util.singleton import Singleton

'''
    Implementazione della classe Lista_Settori
    Implementa una lista di settori
'''

@Singleton
class Lista_Settori(Lista):
    
    '''
        Costruttore
    '''
    
    def __init__(self):
        super().__init__(Model_Settore, "Settore")