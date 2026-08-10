from produttività.model.lista_prod import Lista_Prod
"""
    Implementazione della classe Contr_Prod

    Contiene i richiami delle funzioni definite nella classe Lista_Prod
    Costituisce il tramite tra la classe Lista_Prod e la classe Vista_Prod

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
    """
class Contr_Prod():
    '''
        Costruttore
        Parametri:
            Nessuno
        Return:
            Nessuno
    '''
    def __init__(self):
        self.model = Lista_Prod()
    """
       Restituisce i dati ottenuti dalla funzione get_prod presente nella Lista_Prod 
        Percorso della funzione richiamata: 
            self.model.get_prod(coltura+1,indextime,timenow)
        Parametri:
            (int) coltura: l'id della coltura desiderata 
            (int)indextime: indice dell' impostazione del periodo d'interesse selezionato
            (timedelta)timenow: orario corrente
        Return:
            (list) lista contenente le coppie tempo/valore
    """
    def on_change_tipo_coltura(self,coltura,indextime,timenow):
        return self.model.get_prod(coltura+1,indextime,timenow)
