from util.clock import Clock
from util.simple_refresher import Simple_Refresher

'''
    Implementazione della classe Time_Refresher
    Implementa un thread che si occupa di aggiornare
    data e ora mostrate nelle view
'''

class Time_Refresher(Simple_Refresher):
    
    multiplier = 5

    '''
        Costruttore
    '''

    def __init__(self):
        super().__init__(self.multiplier)

    '''
        Restituisce il tempo attuale:
        Return:
            (datetime) tempo attuale
    '''

    def get_time(self):
        return Clock().get_cur_time()