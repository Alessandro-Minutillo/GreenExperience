from produttività.model.model_prod import Model_Prod
from datetime import datetime,timedelta
from util.lista import Lista
from util.singleton import Singleton


# Lista singleton dei prodotti raccolti (tabella "Prodotto").
@Singleton
class Lista_Prod(Lista):

    def __init__(self):
        super().__init__(Model_Prod,"Prodotto")

    # Restituisce [quantità, timestamp] dei prodotti di una coltura per il periodo scelto.
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
