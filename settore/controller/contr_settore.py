from settore.model.lista_settori import Lista_Settori


# Controller di un settore: tramite tra la vista e Model_Settore.
class Contr_Settore():

    def __init__(self,id):
        self.model = Lista_Settori().get_by_id(id)

    # Restituisce gli id di tutti i lotti del settore.
    def get_id_lotti(self):
        return self.model.get_ids()

    # Restituisce il nome della coltura del settore.
    def get_name_coltura(self):
        return self.model.get_name_coltura()

    # Raccoglie tutti i lotti raccoglibili; restituisce il numero di lotti raccolti.
    def raccogli_tutto(self, time):
        return self.model.raccogli_tutto(time)

    # Pianta la coltura nei lotti disponibili; restituisce il numero di lotti piantati.
    def pianta_tutto(self, id_coltura, time):
        return self.model.pianta_tutto(id_coltura, time)

    # Cambia la coltura del settore.
    def change_coltura(self, id_coltura):
        self.model.change_coltura(id_coltura)

    # Restituisce lo stato di tutti i lotti del settore.
    def get_status_lotti(self):
        return self.model.get_status_lotti()

    # Restituisce la salute di tutti i lotti del settore.
    def get_salute_lotti(self):
        return self.model.get_salute_lotti()

    # Restituisce le soglie di salute minima di tutti i lotti del settore.
    def get_soglia_salute_lotti(self):
        return self.model.get_soglia_salute_lotti()

    # Restituisce l'id dell'umidificatore del settore.
    def get_id_umid(self):
        return self.model.get_id_umid()

    # Restituisce l'id del regolatore di temperatura del settore.
    def get_id_temp_reg(self):
        return self.model.get_id_temp_reg()

    # Restituisce l'id del serbatoio di CO2 del settore.
    def get_id_serbCO2(self):
        return self.model.get_id_serbCO2()

    # Restituisce le date di raccolta previste di tutti i lotti del settore.
    def get_date_fine(self):
        return self.model.get_date_fine()

    # True se la pompa è accesa.
    def is_pompa_on(self):
        return self.model.is_pompa_on()

    # True se il serbatoio di CO2 è acceso.
    def is_serb_on(self):
        return self.model.is_serb_on()

    # True se il regolatore di temperatura è acceso.
    def is_temp_reg_on(self):
        return self.model.is_temp_reg_on()

    # True se l'umidificatore è acceso.
    def is_umid_on(self):
        return self.model.is_umid_on()

    # True se la pompa non è impostata sui valori consigliati.
    def is_pompa_oor(self):
        return self.model.is_pompa_oor()

    # True se il serbatoio di CO2 non è impostato sui valori consigliati.
    def is_serb_oor(self):
        return self.model.is_serb_oor()

    # True se il regolatore di temperatura non è impostato sui valori consigliati.
    def is_temp_reg_oor(self):
        return self.model.is_temp_reg_oor()

    # True se l'umidificatore non è impostato sui valori consigliati.
    def is_umid_oor(self):
        return self.model.is_umid_oor()

    # Restituisce il model della coltura del settore.
    def get_coltura(self):
        return self.model.get_coltura()
