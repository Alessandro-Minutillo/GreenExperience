from util.simple_refresher import Simple_Refresher

'''
    Implementazione della classe Gui_Refresher
    Implementa un thread che esegue il refresh della gui
'''

class Gui_Refresher(Simple_Refresher):

    '''
        Costruttore
    '''
    def __init__(self, multiplier = 20):
        super().__init__(multiplier)