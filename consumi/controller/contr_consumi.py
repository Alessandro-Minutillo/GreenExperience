from consumi.model.lista_consumi import Lista_Consumi


# Controller dei consumi: tramite tra Vista_Consumi e Lista_Consumi.
class Contr_Consumi():
    def __init__(self):
       self.model = Lista_Consumi()

    # Restituisce i dati del consumo elettrico per il periodo selezionato.
    def on_change_elettro (self,index,time):
        returndata = self.model.getdata(index,"consumo_elettrico",time)
        return returndata

    # Restituisce i dati del consumo idrico per il periodo selezionato.
    def on_change_idro(self,index,time):
        returndata = self.model.getdata(index,"consumo_idrico",time)
        return returndata
