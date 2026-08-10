from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe
from util.simple_model import Simple_Model
from attuatore_generico.umid.model.lista_umid import Lista_Umid
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2
from attuatore_generico.temp_reg.model.lista_temp_reg import Lista_Temp_Reg
from random import random

'''
    Implementazione della classe Model_Centralina
    Implementa un model per la rappresentazione di una centralina
'''

class Model_Centralina(Simple_Model):

    '''
        Costruttore
        Percorso delle funzioni chiamate:
            util.lista.get_by_id(self,id)
            util.simple_model.retrieve_data(self, table, values = "*", cond_field = None, cond_value = None)
    '''

    def __init__(self, id):
        super().__init__("Centralina",id)
        self.lrate = 0.2
        id_settore = self.retrieve_data("Lotto", "id_settore","id_centralina", id)["id_settore"]
        id_temp_reg = self.retrieve_data("Settore","id_temp_reg","id",id_settore)["id_temp_reg"]
        id_serbco2 = self.retrieve_data("Settore","id_serbco2","id",id_settore)["id_serbco2"]
        id_umid = self.retrieve_data("Settore","id_umid","id",id_settore)["id_umid"]
        id_pompa = self.retrieve_data("Settore","id_pompa","id",id_settore)["id_pompa"]
        self.temp_reg = Lista_Temp_Reg().get_by_id(id_temp_reg)
        self.serbco2 = Lista_SerbCO2().get_by_id(id_serbco2)
        self.umid = Lista_Umid().get_by_id(id_umid)
        self.pompa = Lista_Pompe().get_by_id(id_pompa)
    
    '''
        Restituisce la temperatura rilevata dalla centralina
        Return:
            (float) temperatura
    '''

    def get_temp(self):
        return float(self.info["temp"])

    '''
        Setta la temperatura rilevata dalla centralina
        Parametri:
            (float) valore
    '''

    def set_temp(self,val):
        self.info["temp"] = val
    
    '''
        Restituisce la concentrazione di CO2 rilevata dalla centralina
        Return:
            (float) concentrazione di CO2
    '''

    def get_liv_co2(self):
        return float(self.info["liv_co2"])

    '''
        Setta la concentrazione di CO2 rilevata dalla centralina
        Parametri:
            (float) valore
    '''

    def set_liv_co2(self,val):
        self.info["liv_co2"] = val

    '''
        Restituisce l'umidità rilevata dalla centralina
        Return:
            (float) umidità
    '''

    def get_umid(self):
        return float(self.info["umid"])

    '''
        Setta l'umidità rilevata dalla centralina
        Parametri:
            (float) valore
    '''

    def set_umid(self,val):
        self.info["umid"] = val
    
    '''
        Restituisce un valore booleano che indica se la pompa presente 
        nel settore della centralina è accesa e impostata sui valori
        consigliati
    '''

    def get_flag_pompa(self):
        return not self.pompa.is_oor() and self.pompa.get_switch()

    '''
        Ricalcola un parametro della centralina in modo che si avvicini
        al valore obiettivo impostato
        Parametri:
            (float) x, valore attuale del parametro;
            (float) target, valore obiettivo del parametro
        Return:
            (float) nuovo valore del parametro
    '''

    def appr(self, x, target):
        return self.casual(x + (target - x) * self.lrate)
    
    '''
        Ricalcola un parametro della centralina in modo randomico quando
        non esiste un valore obiettivo impostao (l'attuatore è spento)
        Parametri:
            (float) x, valore attuale del parametro;
        Return:
            (float) nuovo valore del parametro
    '''

    def casual(self, x):
        return x + x * (random() - 0.5)/100
    
    '''
        Procedura di ricalcolo che aggiorna il valore dei parametri rilevati
        dalla centralina per n volte, dove n (limitato a 100) è una misura del tempo
        trascorso dallo spegnimento del programma
        Parametri:
            (int) n, numero di iterazioni
    '''

    def recalc(self, n):
        target_temp = float(self.temp_reg.get_temp_ob())
        start_temp = float(self.get_temp())
        
        for i in range(n):
            start_temp = self.appr(start_temp, target_temp)
        self.set_temp(start_temp)

        target_umid = float(self.umid.get_umid_ob())
        start_umid = float(self.get_umid())

        for i in range(n):
            start_umid = self.appr(start_umid, target_umid)
        self.set_umid(start_umid)

        target_co2 = float(self.serbco2.get_co2_ob())
        start_co2 = float(self.get_liv_co2())

        for i in range(n):
            start_co2 = self.appr(start_co2, target_co2)
        self.set_liv_co2(start_co2)

    '''
        Procedura di update che aggiorna periodicamente il valore dei
        parametri della centralina, generando un valore parzialmente o
        completamente random
    '''

    def update(self):

        if self.temp_reg.get_switch():
            self.set_temp( self.appr( float(self.get_temp()) , float(self.temp_reg.get_temp_ob()) ) )
        else:
            self.set_temp( self.casual(float(self.get_temp())))
        
        if self.umid.get_switch():
            self.set_umid( self.appr( float(self.get_umid()) , float(self.umid.get_umid_ob()) ) )
        else:
            self.set_umid( self.casual(float(self.get_umid())))

        if self.serbco2.get_switch():
            self.set_liv_co2( self.appr( float(self.get_liv_co2()) , float(self.serbco2.get_co2_ob()) ) )
        else:
            self.set_liv_co2( self.casual(float(self.get_liv_co2())))