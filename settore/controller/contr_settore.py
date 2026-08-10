from settore.model.lista_settori import Lista_Settori

'''
    Implementazione della classe Contr_Settore
    Implementa un controller per la gestione di un settore
'''

class Contr_Settore():

    '''
        Costruttore
        Percorso della funzione chiamata:
            util.lista.get_by_id(self,id)
    '''

    def __init__(self,id):
        self.model = Lista_Settori().get_by_id(id)
    '''
        Ritorna la lista di id di tutti i lotti presenti nel settore
        Percorso della funzione chiamata:
            settore.model.model_settore.get_ids(self)
        Return:
            (list) lista id lotti
    '''

    def get_id_lotti(self):
        return self.model.get_ids()

    '''
        Ritorna il nome della coltura impostata nel settore
        Percorso della funzione chiamata:
            settore.model.model_settore.get_name_coltura(self)
        Return:
            (string) nome coltura
    '''

    def get_name_coltura(self):
        return self.model.get_name_coltura()
    
    '''
        Raccoglie il maggior numero di lotti nel settore
        Parametri:
            (datetime) time, istante attuale
        Percorso della funzione chiamata:
            settore.model.model_settore.raccogli_tutto(self,time)
        Return:
            (int) numero di lotti raccolti
    '''

    def raccogli_tutto(self, time):
        return self.model.raccogli_tutto(time)
    
    '''
        Pianta il maggior numero di lotti nel settore
        Parametri:
            (datetime) time, istante attuale
        Percorso della funzione chiamata:
            settore.model.model_settore.pianta_tutto(self,time)
        Return:
            (int) numero di lotti piantati
    '''

    def pianta_tutto(self, id_coltura, time):
        return self.model.pianta_tutto(id_coltura, time)
    
    '''
        Cambia la coltura impostata nel settore
        Parametri:
            (int) id_coltura, id della nuova coltura
        Percorso della funzione chiamata:
            settore.model.model_settore.change_coltura(self,id)
    '''

    def change_coltura(self, id_coltura):
        self.model.change_coltura(id_coltura)
    
    '''
        Ritorna la lista degli status di tutti i lotti presenti nel settore
        Percorso della funzione chiamata:
            settore.model.model_settore.get_status_lotti(self)
        Return:
            (list) lista status lotti
    '''

    def get_status_lotti(self):
        return self.model.get_status_lotti()
    
    '''
        Ritorna la lista degli indicatori di salute di tutti i lotti
        presenti nel settore
        Percorso della funzione chiamata:
            settore.model.model_settore.get_salute_lotti(self)
        Return:
            (list) lista salute lotti
    '''

    def get_salute_lotti(self):
        return self.model.get_salute_lotti()
    
    '''
        Ritorna la lista delle soglie di salute minima di tutti i lotti
        presenti nel settore
        Percorso della funzione chiamata:
            settore.model.model_settore.get_soglia_salute_lotti(self)
        Return:
            (list) lista soglia salute lotti
    '''


    def get_soglia_salute_lotti(self):
        return self.model.get_soglia_salute_lotti()

    '''
        Ritorna l'id del de/umidificatore presente nel settore
        Percorso della funzione chiamata:
            settore.model.model_settore.get_id_umid(self)
        Return:
            (int) id
    '''

    def get_id_umid(self):
        return self.model.get_id_umid()
    
    '''
        Ritorna l'id del climatizzatore presente nel settore
        Percorso della funzione chiamata:
            settore.model.model_settore.get_id_temp_reg(self)
        Return:
            (int) id
    '''

    def get_id_temp_reg(self):
        return self.model.get_id_temp_reg()

    '''
        Ritorna l'id del serbatoio di CO2 presente nel settore
        Percorso della funzione chiamata:
            settore.model.model_settore.get_id_serbCO2(self)
        Return:
            (int) id
    '''

    def get_id_serbCO2(self):
        return self.model.get_id_serbCO2()
    
    '''
        Ritorna la lista delle date fissate per la raccolta di tutti i lotti
        presenti nel settore
        Percorso della funzione chiamata:
            settore.model.model_settore.get_date_fine(self)
        Return:
            (list) lista date fine
    '''

    def get_date_fine(self):
        return self.model.get_date_fine()
    
    '''
        Ritorna True se la pompa è accesa, False altrimenti
        Return:
            (bool) flag
    '''

    def is_pompa_on(self):
        return self.model.is_pompa_on()
    
    '''
        Ritorna True se il serbatoio di CO2 è acceso, False altrimenti
        Return:
            (bool) flag
    '''

    def is_serb_on(self):
        return self.model.is_serb_on()
    
    '''
        Ritorna True se il climatizzatore è acceso, False altrimenti
        Return:
            (bool) flag
    '''

    def is_temp_reg_on(self):
        return self.model.is_temp_reg_on()
    
    '''
        Ritorna True se il de/umidificatore è acceso, False altrimenti
        Return:
            (bool) flag
    '''

    def is_umid_on(self):
        return self.model.is_umid_on()
    
    '''
        Ritorna True se la pompa non è impostata sui valori consigliati, False altrimenti
        Return:
            (bool) flag
    '''
    
    def is_pompa_oor(self):
        return self.model.is_pompa_oor()
    
    '''
        Ritorna True se il serbaotoio di CO2 non è impostato sui valori consigliati, False altrimenti
        Return:
            (bool) flag
    '''

    def is_serb_oor(self):
        return self.model.is_serb_oor()
    
    '''
        Ritorna True se il climatizzatore non è impostato sui valori consigliati, False altrimenti
        Return:
            (bool) flag
    '''

    def is_temp_reg_oor(self):
        return self.model.is_temp_reg_oor()
    
    '''
        Ritorna True se il de/umidificatore non è impostato sui valori consigliati, False altrimenti
        Return:
            (bool) flag
    '''

    def is_umid_oor(self):
        return self.model.is_umid_oor()
    
    '''
        Restituisce la coltura impostata nel settore
        Return:
            (Model_Coltura) coltura
    '''

    def get_coltura(self):
        return self.model.get_coltura()