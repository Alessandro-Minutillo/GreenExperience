'''
    Implementazione della classe Contr_Att

    Implementa un'interfaccia per il controller di un generico attuatore
'''

class Contr_Att():

    '''
        Restituisce lo stato acceso/spento dell'attuatore
        Return: 
            (bool) stato acceso/spento
    '''    
    def get_switch(self):
        return self.model.get_switch()

    '''
        Restituisce il consumo energetico attuale dell'attuatore
        Return:
            (float) consumo
    '''

    def get_consumo(self):
        return "{:.2f}".format(self.model.get_consumo())

    '''
        Restituisce il consumo energetico mediio dell'attuatore
        Parametri:
            (float) spinbox_value
        Return:
            (float) consumo medio
    '''

    def get_consumo_medio(self, spinbox_value):
        return "{:.2f}".format(self.model.get_consumo_medio(spinbox_value))

    '''
        Restituisce il consumo energetico attuale dell'attuatore
        Parametri:
            (float) spinbox_value
        Return:
            (float) consumo
    '''

    def get_consumo_real(self, spinbox_value):
        return "{:.2f}".format(self.model.get_consumo_real(spinbox_value))

    '''
        Restituisce il nome comune della coltura coltivata nel settore
        in cui è presente l'attuatore
        Return:
            (string) nome coltura
    '''

    def get_coltura(self):
        return self.model.get_coltura()
    
    '''
        Cambia lo stato acceso/spento dell'attuatore
    '''

    def on_off(self):
        self.model.on_off()