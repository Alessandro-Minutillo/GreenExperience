from consumi.model.model_consumo import Model_Consumo
from util.lista import Lista
from util.singleton import Singleton
from datetime import datetime, timedelta
import locale

"""
    Implementazione della classe Lista_Consumi

    Contiene le funzioni fondamentali necessarie alla visualizzazione dei consumi

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""
@Singleton
class Lista_Consumi(Lista): 
    def __init__(self):
        super().__init__(Model_Consumo,"Consumo")
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
    """
        filtra i consumi presenti nella lista in base al tipo di consumo e al tempo specificato
        Parametri:
            timegap: periodo di tempo in cui deve cercare i consumi(datetime)
            tipoconsumo: stringa contenente il tipo di consumo cercato(idrico/elettrico)
            time: l' orario corrente(datetime)
        Return: lista contenente i consumi  cercati
    """
    def selectdata(self,timegap,tipoconsumo,time):
        returnlist=[]
        for i in self.lista.values():
            if datetime.strptime(i.info["data"],"%d %b %Y, %a %H:%M")>time-timegap :
                returnlist.append(i)
        return returnlist
    """
        Restituisce i consumi cercati dall' utente
        Percorso delle funzioni richiamate:
            self.selectdata(timegap,tipoconsumo,time)
        Parametri:
            index: indice del periodo di tempo specificato (settimanale/mensile/annuale/dall' inizio)
            tipoconsumo: stringa contenente il tipo di consumo desiderato
            time: l' orario corrente
        Return:
            lista contenente gli orari dei consumi e i rispettivi valori
    """
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
            #to continue
            listaconsumi=[]
            for i in self.lista.values():
                listaconsumi.append(i)
            valoriconsumi=[a.info[tipoconsumo] for a in listaconsumi]
            intervals=[datetime.strptime(i.info["data"],"%d %b %Y, %a %H:%M").timestamp() for i in listaconsumi]
        return [intervals,valoriconsumi]
