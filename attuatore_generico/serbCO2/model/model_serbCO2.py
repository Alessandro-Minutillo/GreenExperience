from colture.model.lista_colture import Lista_Colture
from attuatore_generico.interface.model_att import Model_Att

"""
    Implementazione della classe Model_SerbCO2
    Eredita dalla classe Model_Att
    Contiene le implementazioni fondamentali necessarie alla gestione del serbatoio di CO2

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""

class Model_SerbCO2(Model_Att):

    def __init__(self, id):
        super().__init__("SerbCO2",id)
        id_coltura = self.retrieve_data("Settore", "id_coltura", "id_serbco2", self.id)["id_coltura"]
        self.coltura = Lista_Colture().get_by_id(id_coltura)
    
    """
        Restituisce l'attributo info di Model_SerbCO2 relativo al campo "liv_co2_ob"
        Percorso della funzione richiamata:
            Nessuno
        Parametri:
            Nessuno
        Return:
            Decimale rappresentante il valore su cui è attualmente impostato l'attuatore
    """
    def get_co2_ob(self):
        return self.info["liv_co2_ob"]

    """
        Restituisce il valore su cui sarebbe corretto impostare l'attuatore a seconda della coltura coltivata
        Percorso della funzione richiamata:
            colture.model.model_coltura.get_co2_cons()
        Parametri:
            Nessuno
        Return:
            Decimale rappresentante il valore su cui sarebbe corretto impostare l'attuatore
            a seconda della coltura coltivata
    """
    def get_co2_cons(self):
        return self.coltura.get_co2_cons()

    """
        Cambia il valore dell'attributo info di Model_SerbCO2 relativo al campo "liv_co2_ob"
        con il valore passato
        Percorso della funzione richiamata:
            Nessuno
        Parametri:
            val: Decimale rappresentante il valore attualmente impostato sulla spinbox dall'utente
        Return:
            Nessuno
    """
    def change_co2(self, val):
        self.info["liv_co2_ob"] = val

    """
        Viene gestito il consumo energetico reale del serbatoio di CO2
        Percorso delle funzioni richiamate:
            attuatore_generico.serbCO2.model.get_switch()
            attuatore_generico.serbCO2.model.get_co2_cons()
            attuatore_generico.serbCO2.model.get_consumo()
        Parametri:
            spinbox_value: Decimale rappresentante il valore attualmente impostato sulla spinbox dall'utente
        Return:
            Decimale rappresentante l'effettivo consumo energetico del serbatoio di CO2
            calcolato a seconda delle scelte effettuate dall'utente
    """
    def get_consumo_real(self, spinbox_value):
        valore_finale=0
        if self.get_switch():
            cons_value = self.get_co2_cons()
            valore_finale= max(0,self.get_consumo()*(1 + (spinbox_value - cons_value)/cons_value))
        return valore_finale

    """
        Funzione che verifica se il valore della spinbox è lo stesso del valore consigliato per la coltura coltivata 
        Percorso della funzione richiamata:
            attuatore_generico.serbCO2.model.get_co2_cons()
            attuatore_generico.serbCO2.model.get_co2_ob()
        Parametri:
            Nessuno
        Return:
            Booleano con valore:
            True se il valore della spinbox è diverso da quello consigliato
            False se il valore della spinbox è lo stesso di quello consigliato
    """    
    def is_oor(self):
        return self.get_co2_ob() != self.get_co2_cons()