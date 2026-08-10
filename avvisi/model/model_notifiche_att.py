from lotto.model.lista_lotti import Lista_Lotti
from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe
from attuatore_generico.temp_reg.model.lista_temp_reg import Lista_Temp_Reg
from attuatore_generico.umid.model.lista_umid import Lista_Umid
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2

'''
    Implementazione della classe Model_Notifiche_Att
    Implementa un model per la gestione delle notifiche relative
    agli attuatori
'''

class Model_Notifiche_Att():
    
    '''
        Costruttore
    '''

    def __init__(self):
        self.pompe = Lista_Pompe()
        self.lotti = Lista_Lotti()
        self.temp_reg = Lista_Temp_Reg()
        self.umid = Lista_Umid()
        self.serbco2 = Lista_SerbCO2()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di accensione delle pompe
        Percorso della funzione chiamata:
            attuatore_generico.interface.lista_att.get_diz_off(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_pompa_off(self):
        return self.pompe.get_diz_off()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di accensione degli
        impianti di illuminazione
        Percorso della funzione chiamata:
            attuatore_generico.interface.lista_att.get_diz_off(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_luce_reg_off(self):
        return self.lotti.get_diz_off()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di accensione degli
        impianti di climatizzazione
        Percorso della funzione chiamata:
            attuatore_generico.interface.lista_att.get_diz_off(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_temp_reg_off(self):
        return self.temp_reg.get_diz_off()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di accensione dei
        de/umidificatori
        Percorso della funzione chiamata:
            attuatore_generico.interface.lista_att.get_diz_off(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_umid_off(self):
        return self.umid.get_diz_off()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di accensione dei
        serbatoi di CO2
        Percorso della funzione chiamata:
            attuatore_generico.interface.lista_att.get_diz_off(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_serbco2_off(self):
        return self.serbco2.get_diz_off()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di funzionamento delle pompe
        Percorso della funzione chiamata:
            attuatore_generico.interface.lista_att.get_diz_oor(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_pompa_oor(self):
        return self.pompe.get_diz_oor()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di funzionamento degli
        impianti di illuminazione
        Percorso della funzione chiamata:
            attuatore_generico.interface.lista_att.get_diz_oor(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_luce_reg_oor(self):
        return self.lotti.get_diz_oor()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di funzionamento degli
        impianti di climatizzazione
        Percorso della funzione chiamata:
            attuatore_generico.interface.lista_att.get_diz_oor(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_temp_reg_oor(self):
        return self.temp_reg.get_diz_oor()
    
    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di funzionamento dei
        de/umidificatori
        Percorso della funzione chiamata:
            attuatore_generico.interface.lista_att.get_diz_oor(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_umid_oor(self):
        return self.umid.get_diz_oor()

    '''
        Restituisce un dizionario in cui sono memorizzate
        informazioni relative allo stato di funzionamento dei
        serbatoi di CO2
        Percorso della funzione chiamata:
            attuatore_generico.interface.lista_att.get_diz_oor(self)
        Return:
            (dict) dizionario
    '''

    def get_diz_serbco2_oor(self):
        return self.serbco2.get_diz_oor()