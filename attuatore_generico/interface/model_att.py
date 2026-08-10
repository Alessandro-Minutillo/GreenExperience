from util.simple_model import Simple_Model

'''
    Implementazione della classe Model_Att
    Definisce un'interfaccia per il model di un generico attuatore
'''

class Model_Att(Simple_Model):

    '''
        Costruttore
        Parametri:
            (string) table, tabella del database;
            (int) id, id dell'attuatore
    '''

    def __init__(self, table, id):
        super().__init__(table, id)
        self.info["switch"] = self.info["switch"] == 'True'

    '''
        Restituisce un flag booleano che indica lo stato acceso/spento dell'attuatore
        Return:
            (bool) stato acceso/spento
    '''

    def get_switch(self):
        return self.info["switch"]
    
    '''
        Inverte lo stato acceso/spento dell'attuatore
    '''

    def on_off(self):
        self.info["switch"] = not self.info["switch"]

    '''
        Restituisce il nome comune della coltura coltivata nel settore
        in cui è presente l'attuatore
        Return:
            (string) nome coltura
    '''

    def get_coltura(self):
        return self.coltura.get_name()
    
    '''
        Setta la coltura su cui è impostato l'attuatore
        Parametri:
            (coltura.model.model_coltura) coltura
    '''

    def set_coltura(self, coltura):
        self.coltura = coltura

    '''
        Restituisce il consumo energetico attuale dell'attuatore
        Return:
            (float) consumo
    '''

    def get_consumo(self):
        valore_finale=0
        if self.get_switch():
            valore_finale=self.info["consumo_elettrico"]
        return valore_finale
    
    '''
        Restituisce il consumo energetico medio dell'attuatore
        Parametri:
            (float) spinbox_value
        Return:
            (float) consumo
    '''

    def get_consumo_medio(self, spinbox_value):
        valore_finale=0
        if self.get_switch():
            valore_finale=(self.get_consumo()+self.get_consumo_real(spinbox_value))/2
        return valore_finale