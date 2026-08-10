from util.simple_model import Simple_Model
from colture.model.lista_profili_luce import Lista_Profili_Luce
from colture.model.lista_soluzioni import Lista_Soluzioni

'''
    Implementazione della classe Model_Coltura
    Implementa un model per la rappresentazione di una coltura
'''

class Model_Coltura(Simple_Model):

    '''
        Costruttore
        Parametri:
            (int) id, id della coltura
        Percorso delle funzioni chiamate:
            util.lista.get_by_id(self,id)
    ''' 

    def __init__(self, id):
        super().__init__("Coltura",id)
        id_soluzione = self.info["id_soluzione_circolante"]
        id_profilo_luce = self.info["id_profilo_luce"]
        self.soluzione = Lista_Soluzioni().get_by_id(id_soluzione)
        self.profilo_luce = Lista_Profili_Luce().get_by_id(id_profilo_luce)
    
    '''
        Ritorna il nome comune di una coltura
        Return:
            (string) nome
    '''

    def get_name(self):
        return self.info["nome_comune"]

    '''
        Ritorna il pH consigliato di una coltura
        Return:
            (float) pH
    '''

    def get_ph_cons(self):
        return self.info["pH_cons"]
    
    '''
        Ritorna l'EC consigliato di una coltura
        Return:
            (float) EC
    '''

    def get_ec_cons(self):
        return self.info["ec_cons"]

    '''
        Ritorna la durata media di una coltura
        Return:
            (int) durata
    '''

    def get_durata(self):
        return int(self.info["durata"])
    
    '''
        Ritorna la temperatura consigliata di una coltura
        Return:
            (float) temperatura
    '''

    def get_temp_cons(self):
        return self.info["temp_cons"]
    
    '''
        Ritorna l'umidità consigliata di una coltura
        Return:
            (float) umidità
    '''

    def get_umid_cons(self):
        return self.info["umid_cons"]

    '''
        Ritorna la concentrazione di CO2 consigliata di una coltura
        Return:
            (float) concentrazione di CO2
    '''

    def get_co2_cons(self):
        return self.info["liv_co2_cons"]

    '''
        Ritorna la resa per lotto di una coltura
        Return:
            (float) resa per lotto
    '''

    def get_prod_per_lotto(self):
        return int(self.info["prod_lotto"])

    '''
        Ritorna il soluzione circolante formattata di una coltura
        Return:
            (string) soluzione
    '''

    def get_soluzione(self):
        return str(self.soluzione)

    '''
        Ritorna l'oggetto soluzione
        Return:
            (Model_Soluzione) soluzione
    '''

    def get_raw_sol(self):
        return self.soluzione
    
    '''
        Ritorna il profilo luce formattato di una coltura
        Return:
            (string) profilo luce
    '''

    def get_profilo_luce(self):
        return str(self.profilo_luce)