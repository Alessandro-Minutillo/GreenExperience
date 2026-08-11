from produttività.model.lista_prod import Lista_Prod


# Controller della produttività: tramite tra Vista_Prod e Lista_Prod.
class Contr_Prod():

    def __init__(self):
        self.model = Lista_Prod()

    # Restituisce i dati di produttività della coltura per il periodo selezionato.
    def on_change_tipo_coltura(self,coltura,indextime,timenow):
        return self.model.get_prod(coltura+1,indextime,timenow)
