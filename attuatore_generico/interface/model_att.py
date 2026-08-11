from util.simple_model import Simple_Model


# Model base di un attuatore generico: stato acceso/spento, coltura e consumi.
class Model_Att(Simple_Model):

    # Carica i dati e converte il campo "switch" da stringa a booleano.
    def __init__(self, table, id):
        super().__init__(table, id)
        self.info["switch"] = self.info["switch"] == 'True'

    # Restituisce lo stato acceso/spento dell'attuatore.
    def get_switch(self):
        return self.info["switch"]

    # Inverte lo stato acceso/spento dell'attuatore.
    def on_off(self):
        self.info["switch"] = not self.info["switch"]

    # Restituisce il nome della coltura del settore in cui opera l'attuatore.
    def get_coltura(self):
        return self.coltura.get_name()

    # Imposta la coltura associata all'attuatore.
    def set_coltura(self, coltura):
        self.coltura = coltura

    # Consumo elettrico attuale: il valore nominale se acceso, altrimenti 0.
    def get_consumo(self):
        valore_finale=0
        if self.get_switch():
            valore_finale=self.info["consumo_elettrico"]
        return valore_finale

    # Consumo medio tra quello attuale e quello a regime per il valore impostato.
    def get_consumo_medio(self, spinbox_value):
        valore_finale=0
        if self.get_switch():
            valore_finale=(self.get_consumo()+self.get_consumo_real(spinbox_value))/2
        return valore_finale
