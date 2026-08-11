from consumi.model.model_consumo import Model_Consumo
from util.lista import Lista
from util.singleton import Singleton
from datetime import datetime, timedelta
import locale


# Lista singleton dei consumi campionati (tabella "Consumo").
@Singleton
class Lista_Consumi(Lista):
    def __init__(self):
        super().__init__(Model_Consumo,"Consumo")
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")

    # Restituisce i consumi registrati entro l'intervallo di tempo indicato.
    def selectdata(self,timegap,tipoconsumo,time):
        returnlist=[]
        for i in self.lista.values():
            if datetime.strptime(i.info["data"],"%d %b %Y, %a %H:%M")>time-timegap :
                returnlist.append(i)
        return returnlist

    # Restituisce [timestamp, valori] del tipo di consumo, per il periodo scelto (settimana/mese/anno/tutto).
    def getdata(self,index,tipoconsumo,time):
        if index == 0:
            timegap=timedelta(days=7)
            gap = 7
            listaconsumi=self.selectdata(timegap,tipoconsumo,time)
            valoriconsumi=[a.info[tipoconsumo] for a in listaconsumi]
            intervals=[datetime.strptime(i.info["data"],"%d %b %Y, %a %H:%M").timestamp() for i in listaconsumi]
        if index == 1:
            timegap=timedelta(days=30)
            gap = 30
            listaconsumi=self.selectdata(timegap,tipoconsumo,time)
            valoriconsumi=[a.info[tipoconsumo] for a in listaconsumi]
            intervals=[datetime.strptime(i.info["data"],"%d %b %Y, %a %H:%M").timestamp() for i in listaconsumi]
        if index == 2:
            timegap=timedelta(days=365)
            gap = 365
            listaconsumi=self.selectdata(timegap,tipoconsumo,time)
            valoriconsumi=[a.info[tipoconsumo] for a in listaconsumi]
            intervals=[datetime.strptime(i.info["data"],"%d %b %Y, %a %H:%M").timestamp() for i in listaconsumi]
        if index == 3:
            listaconsumi=[]
            for i in self.lista.values():
                listaconsumi.append(i)
            valoriconsumi=[a.info[tipoconsumo] for a in listaconsumi]
            intervals=[datetime.strptime(i.info["data"],"%d %b %Y, %a %H:%M").timestamp() for i in listaconsumi]
        return [intervals,valoriconsumi]
