from colture.model.model_soluzione import Model_Soluzione
from util.lista import Lista
from util.singleton import Singleton

'''
    Implementazione della classe Lista_Soluzioni
    Implementa una lista di soluzioni
'''

@Singleton
class Lista_Soluzioni(Lista): 

    '''
        Costruttore
    '''

    def __init__(self):
        super().__init__(Model_Soluzione,"Soluzione_Circolante")