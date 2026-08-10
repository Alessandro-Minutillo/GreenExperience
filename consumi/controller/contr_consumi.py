from consumi.model.lista_consumi import Lista_Consumi
"""
    Implementazione della classe Contr_Consumi

    Contiene i richiami delle funzioni definite nella classe Lista_Consumi
    Costituisce il tramite tra la classe Lista_Consumi e la classe Vista_consumi

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""
class Contr_Consumi():
    def __init__(self):
       self.model = Lista_Consumi()
    """
       Restituisce i dati ottenuti dalla funzione on_change_elettro presente nella Lista_Consumi 
        Percorso della funzione richiamata: 
            self.model.getdata(index,"consumo_elettrico",time)
        Parametri: 
            index: indice dell' impostazione selezionata
            time: orario corrente
        Return:
            lista contenente le coppie valore/tempo
    """
    def on_change_elettro (self,index,time):
        returndata = self.model.getdata(index,"consumo_elettrico",time)
        return returndata

    """
       Restituisce i dati ottenuti dalla funzione on_change_idro presente nella Lista_Consumi 
        Percorso della funzione richiamata: 
            self.model.getdata(index,"consumo_idrico",time)
        Parametri: 
            index: indice dell' impostazione selezionata
            time: orario corrente
        Return:
            lista contenente le coppie valore/tempo
    """
    def on_change_idro(self,index,time):
        returndata = self.model.getdata(index,"consumo_idrico",time)
        return returndata
