from lotto.model.lista_lotti import Lista_Lotti

'''
    Implementazione della classe Contr_Notifiche_Lotto
    Implementa un controller per la gestione delle notifiche
    riguardanti i lotti
'''

class Contr_Notifiche_Lotto():

    '''
        Costruttore
    '''

    def __init__(self):
        self.model = Lista_Lotti()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative ai lotti non raccolti in tempo
        Parametri:
            (datetime) time, tempo attuale
        Percorso della funzione chiamata:
            lotto.model.lista_lotti.get_diz_time_out_lotti(self,time)
        Return:
            (dict) dizionario
    '''

    def get_diz_time_out_lotti(self, time):
        return self.model.get_diz_time_out_lotti(time)
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative ai lotti con salute bassa
        Percorso della funzione chiamata:
            lotto.model.lista_lotti.get_diz_low_salute_lotti(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_low_salute_lotti(self):
        return self.model.get_diz_low_salute_lotti()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative ai lotti vuoti
        Percorso della funzione chiamata:
            lotto.model.lista_lotti.get_diz_lotti_vuoti(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_lotti_vuoti(self):
        return self.model.get_diz_lotti_vuoti()
    
    '''
        Restituisce l'indicatore numerico di salute del lotto
        contraddistinto dal parametro id
        Parametri:
            (int) id, id del lotto
        Percorso della funzione chiamata:
            lotto.model.lista_lotti.get_salute_lotto(self,id)
        Return:
            (float) salute
    '''

    def get_salute_lotto(self, id):
        return self.model.get_salute_lotto(id)
    
    '''
        Restituisce l'id del settore cui appartiene il lotto
        contrassegnato dal parametro id
        Parametri:
            (int) id, id del lotto
        Percorso della funzione chiamata:
            lotto.model.lista_lotti.get_id_settore(self,id)
        Return:
            (int) id del settore
    '''

    def get_id_settore(self,id):
        return self.model.get_id_settore(id)