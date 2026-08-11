from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe
from util.simple_model import Simple_Model
from attuatore_generico.umid.model.lista_umid import Lista_Umid
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2
from attuatore_generico.temp_reg.model.lista_temp_reg import Lista_Temp_Reg
from random import random


# Model della centralina: simula la rilevazione di temperatura, CO2 e umidità del settore.
class Model_Centralina(Simple_Model):

    # Carica i dati e collega gli attuatori del settore (temp_reg, serbCO2, umid, pompa).
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

    # Restituisce la temperatura rilevata.
    def get_temp(self):
        return float(self.info["temp"])

    # Imposta la temperatura rilevata.
    def set_temp(self,val):
        self.info["temp"] = val

    # Restituisce la concentrazione di CO2 rilevata.
    def get_liv_co2(self):
        return float(self.info["liv_co2"])

    # Imposta la concentrazione di CO2 rilevata.
    def set_liv_co2(self,val):
        self.info["liv_co2"] = val

    # Restituisce l'umidità rilevata.
    def get_umid(self):
        return float(self.info["umid"])

    # Imposta l'umidità rilevata.
    def set_umid(self,val):
        self.info["umid"] = val

    # True se la pompa del settore è accesa e impostata sui valori consigliati.
    def get_flag_pompa(self):
        return not self.pompa.is_oor() and self.pompa.get_switch()

    # Avvicina un parametro al valore obiettivo con un passo pari a lrate.
    def appr(self, x, target):
        return self.casual(x + (target - x) * self.lrate)

    # Applica una piccola variazione casuale a un parametro (attuatore spento).
    def casual(self, x):
        return x + x * (random() - 0.5)/100

    # Ricalcola temperatura, umidità e CO2 iterando n volte (recupero dopo lo spegnimento).
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

    # Aggiorna i parametri rilevati: verso l'obiettivo se l'attuatore è acceso, casuale se spento.
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
