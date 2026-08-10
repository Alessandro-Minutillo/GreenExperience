from util.lista import Lista

'''
    Implementazione della classe Lista_Att

    Definisce un'interfaccia per una lista di generici attuatori
    Eredita dall'interfaccia util.lista
'''

class Lista_Att(Lista):

    '''
        Costruttore
        Parametri: 
            (class) class_, classe dell'attuatore;
            (string) table, tabella del database
    '''

    def __init__(self, class_, table):
        super().__init__(class_, table)
    
    '''
        Restituisce un dizionario avente per chiave l'id dell'attuatore
        e per valore un flag booleano posto a True se l'attuatore è spento
        o a False se l'attuatore è acceso
        Percorso delle funzioni chiamata:
            util.simple_model.get_id(self)
            attuatore_generico.interface.model_att.get_switch(self)
        Return: (dict) dizionario
    '''

    def get_diz_off(self):
        return { d.get_id() : not d.get_switch() for d in self.lista.values()}
    
    '''
        Restituisce un dizionario avente per chiave l'id dell'attuatore
        e per valore un flag booleano posto a True se l'attuatore è
        'out of range', ovvero non è impostato sui valori consigliati
        Percorso delle funzioni chiamata:
            util.simple_model.get_id(self)
        Return: (dict) dizionario
    '''

    def get_diz_oor(self):
        return { d.get_id() : d.is_oor() for d in self.lista.values()}