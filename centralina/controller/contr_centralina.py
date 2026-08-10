from centralina.model.lista_centraline import Lista_Centraline

'''
    Implementazionde della classe Contr_Centralina
    Implementa un controller per la gestione di una centralina
'''

class Contr_Centralina():

    '''
        Costruttore
        Parametri:
            (int) id, id della centralina
        Percorso della funzione chiamata:
            centralina.model.lista_centraline.get_by_id(self,id)
    '''

    def __init__(self,id):
        self.model = Lista_Centraline().get_by_id(id)

    '''
        Restituisce la temperatura rilevata dalla centralina
        Percorso della funzione chiamata:
            centralina.model.model_centralina.get_temp(self)
        Return:
            (string) temperatura
    '''

    def get_temp(self):
        return "{:.1f}".format(self.model.get_temp())

    '''
        Restituisce la concentrazione di CO2 rilevata dalla centralina
        Percorso della funzione chiamata:
            centralina.model.model_centralina.get_liv_co2(self)
        Return:
            (string) concentrazione di co2
    '''

    def get_liv_co2(self):
        return "{:.0f}".format(self.model.get_liv_co2())

    '''
        Restituisce il livello di umidità rilevata dalla centralina
        Percorso della funzione chiamata:
            centralina.model.model_centralina.get_umid(self)
        Return:
            (string) umidità
    '''

    def get_umid(self):
        return "{:.1f}".format(self.model.get_umid())
    
    '''
        Restituisce il model
        Return:
            (centralina.model.model_centralina) model
    '''

    def get_model(self):
        return self.model