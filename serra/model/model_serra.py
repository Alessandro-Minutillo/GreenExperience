from consumi.model.lista_consumi import Lista_Consumi
from consumi.model.model_consumo import Model_Consumo
from util.simple_model import Simple_Model
from util.singleton import Singleton
from settore.model.lista_settori import Lista_Settori
from datetime import datetime, timedelta
import locale

'''
    Implementazione della classe Model_Serra
    Implementa un model che rappresenta la serra
'''

@Singleton
class Model_Serra(Simple_Model):

    '''
        Costruttore
        Percorso delle funzioni chiamate:
            util.lista.get_by_id(self,id)
            util.simple_model.retrieve_all_data(self, table, values = "*", cond_field = None, cond_value = None)
    '''

    def __init__(self):
        super().__init__("Serra",1)
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
        id_settori = self.retrieve_all_data("Settore", 'id', "id_serra", 1)
        self.settori = [ Lista_Settori().get_by_id(int(id["id"])) for id in id_settori]
        self.info["cons_giorn_el"] = float(self.info["cons_giorn_el"])
        self.info["cons_giorn_idro"] = float(self.info["cons_giorn_idro"])
        self.data_lettura = None if self.info["data_lettura"] == "mancante" else datetime.strptime(self.info["data_lettura"], "%d %b %Y, %a %H:%M")
        self.old_cons_el = self.get_cons_el()
        self.old_cons_idro = self.get_cons_idro()

    '''
        Restituisce una lista degli id dei settori presenti nella serra
        Percorso della funzione chiamata:
            util.simple_model.get_id(self)
        Return:
            (list) lista id
    '''

    def get_ids(self):
        return [d.get_id() for d in self.settori]
    
    '''
        Restituisce una lista di flag posti a True se l'iesimo settore
        è ok
        Percorso della funzione chiamata:
            settore.model.model_settore.is_ok(self,time)
        Return:
            (list) lista flag
    '''

    def get_ok_flags(self, time):
        return [d.is_ok(time) for d in self.settori]
    
    '''
        Restituisce una lista di flag posti a True se l'iesimo settore
        è completamente vuoto
        Percorso della funzione chiamata:
            settore.model.model_settore.is_empty(self)
        Return:
            (list) lista flag
    '''

    def get_empty_flags(self):
        return [d.is_empty() for d in self.settori]

    '''
        Restituisce la lista di tutti i settori
        Return:
            (list) lista di model_settore
    '''

    def get_settori(self):
        return self.settori
    
    '''
        Restituisce il consumo elettrico totale della serra
        Percorso della funzione chiamata:
            settore.model.model_settore.get_cons_el(self)
        Return:
            (float) consumo elettrico
    '''

    def get_cons_el(self):
        ret = 0
        for set in self.settori:
            ret += set.get_cons_el()
        return ret
    
    '''
        Restituisce il consumo idrico totale della serra
        Percorso della funzione chiamata:
            settore.model.medel_settore.get_cons_el(self)
        Return:
            (float) consumo idrico
    '''

    def get_cons_idro(self):
        ret = 0
        for set in self.settori:
            ret += set.get_cons_idro()
        return ret

    '''
        Crea una nuova istanza di consumo periodicamente
        Parametri:
            (datetime) time, istante lettura
        Percorso delle funzioni chiamate:
            util.lista.get_last_id(self)
            util.simple_model.get_id(self)
            util.lista.add(self,item)
    '''

    def stock_cons(self, time):
        self.data_lettura = time
        self.info["data_lettura"] = datetime.strftime(time, "%d %b %Y, %a %H:%M")
        last_id=Lista_Consumi().get_last_id()
        new_cons = Model_Consumo()
        new_cons.set_new_model(last_id+1, self.get_id(),self.info["cons_giorn_idro"] ,self.info["cons_giorn_el"] , datetime.strftime(time,"%d %b %Y, %a %H:%M"))
        Lista_Consumi().add(new_cons)
        self.info["cons_giorn_el"]=0
        self.info["cons_giorn_idro"]=0
    
    '''
        Ricalcola i consumi letti nel periodo di spegnimento del programma
        Parametri:
            (datetime) time, tempo attuale
        
    '''

    def recalc(self, time):
        if self.data_lettura is not None:
            consumo_el = self.get_cons_el()
            consumo_idro = self.get_cons_idro()
            day = timedelta(days = 1)
            tot_sec = (time - self.data_lettura).total_seconds()
            resto_sec = tot_sec % (3600*24)
            n_giorni = int(tot_sec/(3600*24))

            if time < self.data_lettura + day:
                self.info["cons_giorn_el"] += consumo_el * (tot_sec/3600)
                self.info["cons_giorn_idro"] += consumo_idro * (tot_sec/3600)
            else:
                avg_el = (consumo_el * ((tot_sec-resto_sec)/3600) + self.info["cons_giorn_el"]) / ((tot_sec-resto_sec)/3600)
                avg_idro = (consumo_idro * ((tot_sec-resto_sec)/3600) + self.info["cons_giorn_idro"]) / ((tot_sec-resto_sec)/3600)
                
                for i in range(n_giorni):
                    self.info["cons_giorn_el"] = avg_el * 24
                    self.info["cons_giorn_idro"] = avg_idro * 24
                    self.stock_cons(self.data_lettura + day)
                
                self.info["cons_giorn_el"] = consumo_el * (resto_sec/3600)
                self.info["cons_giorn_idro"] = consumo_idro * (resto_sec/3600)

    '''
        Procedura di update che aggiorna i consumi elettrici e idrici della serra,
        e produce quotidianamente un nuovo oggetto consumo
        Parametri:
            (datetime) time, tempo attuale
            (int) time_interval, frequenza lettura in secondi
    '''

    def update(self,time, time_interval):
        
        new_cons_el = self.get_cons_el()
        new_cons_idro = self.get_cons_idro()

        plus_el = ((new_cons_el +self.old_cons_el)/2) * (time_interval/3600)
        plus_idro =((new_cons_idro+self.old_cons_idro)/2) * (time_interval/3600)

        self.info["cons_giorn_el"] += plus_el 
        self.info["cons_giorn_idro"] += plus_idro
        day = timedelta(days = 1)

        if self.data_lettura is None or time > self.data_lettura + day :
            self.stock_cons(time)
        
        self.old_cons_el= new_cons_el
        self.old_cons_idro= new_cons_idro