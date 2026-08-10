from avvisi.model.model_notifiche_att import Model_Notifiche_Att

'''
    Implementazione della classe Contr_Notifiche_Att
    Implementa un controllore per la gestione delle notifiche
    riguardanti gli attuatori
'''

class Contr_Notifiche_Att():

    '''
        Costruttore
    '''

    def __init__(self):
        self.model = Model_Notifiche_Att()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di accensione delle pompe
        Percorso della funzione chiamata:
            avvisi.model.model_notifiche_att.get_diz_pompa_off(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_pompa_off(self):
        return self.model.get_diz_pompa_off()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di accensione degli
        impianti di illuminazione
        Percorso della funzione chiamata:
            avvisi.model.model_notifiche_att.get_diz_luce_reg_off(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_luce_reg_off(self):
        return self.model.get_diz_luce_reg_off()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di accensione degli
        impianti di climatizzazione
        Percorso della funzione chiamata:
            avvisi.model.model_notifiche_att.get_diz_temp_reg_off(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_temp_reg_off(self):
        return self.model.get_diz_temp_reg_off()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di accensione dei
        de/umidificatori
        Percorso della funzione chiamata:
            avvisi.model.model_notifiche_att.get_diz_umid_off(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_umid_off(self):
        return self.model.get_diz_umid_off()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato dei
        serbatoi di CO2
        Percorso della funzione chiamata:
            avvisi.model.model_notifiche_att.get_diz_serbco2_off(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_serbco2_off(self):
        return self.model.get_diz_serbco2_off()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di funzionamento delle pompe
        Percorso della funzione chiamata:
            avvisi.model.model_notifiche_att.get_diz_pompa_oor(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_pompa_oor(self):
        return self.model.get_diz_pompa_oor()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di funzionamento degli
        impianti di illuminazione
        Percorso della funzione chiamata:
            avvisi.model.model_notifiche_att.get_diz_luce_reg_oor(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_luce_reg_oor(self):
        return self.model.get_diz_luce_reg_oor()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di funzionamento degli
        impianti di illuminazione
        Percorso della funzione chiamata:
            avvisi.model.model_notifiche_att.get_diz_temp_reg_oor(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_temp_reg_oor(self):
        return self.model.get_diz_temp_reg_oor()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di funzionamento dei
        de/umidificatori
        Percorso della funzione chiamata:
            avvisi.model.model_notifiche_att.get_diz_umid_oor(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_umid_oor(self):
        return self.model.get_diz_umid_oor()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di funzionamento dei
        serbatoi di CO2
        Percorso della funzione chiamata:
            avvisi.model.model_notifiche_att.get_diz_serbco2_oor(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_serbco2_oor(self):
        return self.model.get_diz_serbco2_oor()