from produttività.model.model_prod import Model_Prod
from datetime import datetime,timedelta
from util.lista import Lista
from util.singleton import Singleton
"""
    Implementazione della classe Lista_Prod

    Contiene le funzioni fondamentali necessarie alla visualizzazione della produttività

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""
@Singleton
class Lista_Prod(Lista):
    '''
        Costruttore
        Parametri:
            Nessuno
        Return:
            Nessuno
    ''' 
    def __init__(self):
        super().__init__(Model_Prod,"Prodotto")  
    """
        Restituisce le coppie quantità/data tramite i dati nel database opportunamente filtrati
        Parametri:
            (int) id: id relativo alla coltura selezionata
            (int) indextime: indice del periodo di tempo specificato (settimanale/mensile/annuale/dall' inizio)
            (timedelta) timenow: l' orario corrente
        Return:
            (list) lista contenente i valori della produttività con i relativi orari di raccolta
    """
    def get_prod(self,id,indextime,timenow):
        if indextime==0:
            timegap=timedelta(days=7)
        if indextime==1:
            timegap=timedelta(days=30)
        if indextime==2:
            timegap=timedelta(days=365)
        if indextime==3:
            a=[]
            intervals=[]
            for d in self.lista.values():
                if(d.get_id_coltura()==id ):
                    intervals.append(d.get_time().timestamp())
                    a.append(d.get_quant())
            return [a,intervals]
        a=[]
        intervals=[]
        for d in self.lista.values():
            if(d.get_id_coltura()==id and d.get_time()>timenow-timegap):
                intervals.append(d.get_time().timestamp())
                a.append(d.get_quant())
        return [a,intervals]