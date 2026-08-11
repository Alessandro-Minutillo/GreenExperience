# Controller base di un attuatore generico: fa da tramite tra vista e model.
class Contr_Att():

    # Restituisce lo stato acceso/spento dell'attuatore.
    def get_switch(self):
        return self.model.get_switch()

    # Consumo elettrico attuale, formattato a due decimali.
    def get_consumo(self):
        return "{:.2f}".format(self.model.get_consumo())

    # Consumo medio per il valore impostato, formattato a due decimali.
    def get_consumo_medio(self, spinbox_value):
        return "{:.2f}".format(self.model.get_consumo_medio(spinbox_value))

    # Consumo a regime per il valore impostato, formattato a due decimali.
    def get_consumo_real(self, spinbox_value):
        return "{:.2f}".format(self.model.get_consumo_real(spinbox_value))

    # Restituisce il nome della coltura del settore dell'attuatore.
    def get_coltura(self):
        return self.model.get_coltura()

    # Inverte lo stato acceso/spento dell'attuatore.
    def on_off(self):
        self.model.on_off()
