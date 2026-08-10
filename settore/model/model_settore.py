from datetime import datetime
from util.simple_model import Simple_Model
from lotto.model.lista_lotti import Lista_Lotti
from attuatore_generico.temp_reg.model.lista_temp_reg import Lista_Temp_Reg
from attuatore_generico.serbCO2.model.lista_serbCO2 import Lista_SerbCO2
from attuatore_generico.umid.model.lista_umid import Lista_Umid
from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe
from colture.model.lista_colture import Lista_Colture
import locale

'''
    Implementazionde della classe Model_Settore
    Implementa un model che rappresenta il settore
'''

class Model_Settore(Simple_Model):

    '''
        Costruttore
        Percorso delle funzioni chiamate:
            util.lista.get_by_id(self,id)
            util.simple_model.retrieve_all_data(self, table, values = "*", cond_field = None, cond_value = None)
    '''

    def __init__(self, id):
        super().__init__("Settore", id)
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
        id_lotti = self.retrieve_all_data("Lotto","id",'id_settore',id)
        self.lotti = [ Lista_Lotti().get_by_id(d["id"]) for d in id_lotti]
        self.coltura = Lista_Colture().get_by_id(self.info["id_coltura"])
        self.temp_reg = Lista_Temp_Reg().get_by_id(self.info["id_temp_reg"])
        self.umid = Lista_Umid().get_by_id(self.info["id_umid"])
        self.serbCO2 = Lista_SerbCO2().get_by_id(self.info["id_serbco2"])
        self.pompa = Lista_Pompe().get_by_id(self.info["id_pompa"])

    '''
        Restituisce la lista di tutti i lotti presenti nel settore
        Return
            (list) lista model lotti
    '''

    def get_lotti(self):
        return self.lotti

    '''
        Ritorna l'id del de/umidificatore presente nel settore
        Percorso della funzione chiamata:
            util.simple_model.get_id(self)
        Return:
            (int) id
    '''

    def get_id_umid(self):
        return self.umid.get_id()
    
    '''
        Ritorna l'id del climatizzatore presente nel settore
        Percorso della funzione chiamata:
            util.simple_model.get_id(self)
        Return:
            (int) id
    '''

    def get_id_temp_reg(self):
        return self.temp_reg.get_id()

    '''
        Ritorna l'id del serbatoio di CO2 presente nel settore
        Percorso della funzione chiamata:
            util.simple_model.get_id(self)
        Return:
            (int) id
    '''

    def get_id_serbCO2(self):
        return self.serbCO2.get_id()

    '''
        Ritorna la lista di id di tutti i lotti presenti nel settore
        Percorso della funzione chiamata:
            util.simple_model.get_id(self)
        Return:
            (list) lista id lotti
    '''

    def get_ids(self):
        return [d.get_id() for d in self.lotti]

    '''
        Ritorna la lista degli status di tutti i lotti presenti nel settore
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_status(self)
        Return:
            (list) lista status lotti
    '''

    def get_status_lotti(self):
        return [d.get_status() for d in self.lotti]

    '''
        Ritorna la lista degli indicatori di salute di tutti i lotti
        presenti nel settore
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_salute(self)
        Return:
            (list) lista salute lotti
    '''

    def get_salute_lotti(self):
        return [d.get_salute() for d in self.lotti]
    
    '''
        Ritorna la lista delle soglie di salute minima di tutti i lotti
        presenti nel settore
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_salute_threshold(self)
        Return:
            (list) lista soglia salute lotti
    '''

    def get_soglia_salute_lotti(self):
        return [d.get_salute_threshold() for d in self.lotti]
    
    '''
        Ritorna la lista delle date fissate per la raccolta di tutti i lotti
        presenti nel settore
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_fine(self)
        Return:
            (list) lista date fine
    '''

    def get_date_fine(self):
        return [d.get_fine() for d in self.lotti]

    '''
        Restituisce il nome della coltura impostata nel settore
        Return:
            (string) nome
    '''

    def get_name_coltura(self):
        return self.coltura.get_name()

    '''
        Raccoglie il maggior numero di lotti nel settore
        Parametri:
            (datetime) time, istante attuale
        Percorso della funzione chiamata:
            lotto.model.model_lotto.raccogli(self,time)
        Return:
            (int) numero di lotti raccolti
    '''

    def raccogli_tutto(self, time):
        num = 0
        for l in self.lotti:
            if l.raccogli(time):
                num += 1
        return num
    
    '''
        Pianta il maggior numero di lotti nel settore
        Parametri:
            (datetime) time, istante attuale
        Percorso della funzione chiamata:
            lotto.model.model_lotto.pianta(self,time)
        Return:
            (int) numero di lotti piantati
    '''

    def pianta_tutto(self, id_coltura, time):
        num = 0
        old_id_coltura = self.lotti[0].get_id_coltura()
        cond1 = not any([not l.is_empty() for l in self.lotti])
        for l in self.lotti:
            cond2 = cond1 or old_id_coltura == id_coltura 
            if cond1:
                l.change_coltura(id_coltura)
            if cond2:
                if l.pianta(time):
                    num += 1
        return num
    '''
        Cambia la coltura impostata nel settore e nei rispettivi attuatori
        Parametri:
            (int) id_coltura, id della nuova coltura
        Percorso della funzione chiamata:
            util.lista.get_by_id(self,id)
            attuatore_generico.interface.model_att.set_coltura(self,coltura)
    '''

    def change_coltura(self,id_coltura):
        self.info["id_coltura"] = id_coltura
        self.coltura = Lista_Colture().get_by_id(id_coltura)
        self.serbCO2.set_coltura(self.coltura)
        self.umid.set_coltura(self.coltura)
        self.temp_reg.set_coltura(self.coltura)
        self.pompa.set_coltura(self.coltura)
    
    '''
        Restituisce True se il settore è ok, ovvero non ci sono problemi riguardanti i
        lotti o gli attuatori, False altrimenti
        Parametri:
            (datetime) time, istante attuale
        Percorso delle funzioni chamate:
            lotto.model.model_lotto.get_salute(self)
            lotto.model.model_lotto.get_salute_threshold(self)
            lotto.model.model_lotto.get_status(self)
            lotto.model.model_lotto.get_fine(self)
            lotto.model.model_lotto.is_oor(self)
            attuatore_generico.pompa.model_pompa.is_oor(self)
            attuatore_generico.temp_reg.model_temp_regs.is_oor(self)
            attuatore_generico.umid.model_umid.is_oor(self)
            attuatore_generico.serbCO2.model_serbCO2.is_oor(self)
        Return:
            (bool) flag
    '''

    def is_ok(self, time):

        return (not any(
                            [ 
                                lotto.get_status() == 'coltivato' and 
                                ( 
                                    lotto.get_salute() < lotto.get_salute_threshold() or
                                    ( lotto.get_fine() != "mancante" and datetime.strptime(lotto.get_fine(), "%d %b %Y, %a %H:%M") < time )
                                )
                            for lotto in self.lotti
                            ]
                        )) and (not self.serbCO2.is_oor()) and (not self.umid.is_oor()) and (not self.temp_reg.is_oor()) and (not self.pompa.is_oor())
    
    '''
        Restituisce True se tutti i lotti nel settore sono vuoti
        Percorso delle funzioni chiamate:
            lotto.model.model_lotto.get_status(self)
        Return:
            (bool) flag
    '''

    def is_empty(self):
        return not any([lotto.get_status() != 'vuoto'
                            for lotto in self.lotti])
    '''
        Ritorna True se la pompa è accesa, False altrimenti
        Percorso della funzione chiamata:
            attuatore_generico.interface.model.get_switch(self)
        Return:
            (bool) flag
    '''

    def is_pompa_on(self):
        return self.pompa.get_switch()
    
    '''
        Ritorna True se il serbatoio di CO2 è acceso, False altrimenti
        Percorso della funzione chiamata:
            attuatore_generico.interface.model.get_switch(self)
        Return:
            (bool) flag
    '''

    def is_serb_on(self):
        return self.serbCO2.get_switch()
    
    '''
        Ritorna True se il climatizzatore è acceso, False altrimenti
        Percorso della funzione chiamata:
            attuatore_generico.interface.model.get_switch(self)
        Return:
            (bool) flag
    '''

    def is_temp_reg_on(self):
        return self.temp_reg.get_switch()
    
    '''
        Ritorna True se il de/umificatore è acceso, False altrimenti
        Percorso della funzione chiamata:
            attuatore_generico.interface.model.get_switch(self)
        Return:
            (bool) flag
    '''

    def is_umid_on(self):
        return self.umid.get_switch()

    '''
        Ritorna True se Ritorna True se la pompa non è impostata sui valori consigliati, False altrimenti
        Percorso della funzione chiamata:
            attuatore_generico.pompa.model.model_pompa.is_oor(self)
        Return:
            (bool) flag
    '''

    def is_pompa_oor(self):
        return self.pompa.is_oor()
    
    '''
        Ritorna True se Ritorna True se il serbatoio di CO2 non è impostato sui valori consigliati, False altrimenti
        Percorso della funzione chiamata:
            attuatore_generico.serbCO2.model.model_serbCO2.is_oor(self)
        Return:
            (bool) flag
    '''

    def is_serb_oor(self):
        return self.serbCO2.is_oor()
    
    '''
        Ritorna True se Ritorna True se il climatizzatore non è impostato sui valori consigliati, False altrimenti
        Percorso della funzione chiamata:
            attuatore_generico.temp_reg.model.model_temp_reg.is_oor(self)
        Return:
            (bool) flag
    '''

    def is_temp_reg_oor(self):
        return self.temp_reg.is_oor()
    
    '''
        Ritorna True se Ritorna True se il de/umificatore non è impostato sui valori consigliati, False altrimenti
        Percorso della funzione chiamata:
            attuatore_generico.umid.model.model_umid.is_oor(self)
        Return:
            (bool) flag
    '''

    def is_umid_oor(self):
        return self.umid.is_oor()

    '''
        Restituisce la coltura impostata nel settore
        Return:
            (Model_Coltura) coltura
    '''

    def get_coltura(self):
        return self.coltura
    '''
        Restituisce il consumo elettrico totale del settore
        Percorso della funzione chiamata:
            attuatore_generico.interface.model_att.get_consumo(self)
            attuatore_generico.pompa.model.model_pompa.get_consumo_el(self)
        Return:
            (float) consumo elettrico
    '''

    def get_cons_el(self):
        electric=self.pompa.get_consumo_el()+self.umid.get_consumo()+self.temp_reg.get_consumo()+self.serbCO2.get_consumo()
        consumoluce=0
        for i in  self.lotti:
            consumoluce+=i.luce_reg.get_consumo()
        electric+=consumoluce
        return electric
    '''
        Restituisce il consumo idrico totale del settore
        Percorso della funzione chiamata:
            attuatore_generico.pompa.model.model_pompa.get_consumo_idro(self)
        Return:
            (float) consumo idrico
    '''
    def get_cons_idro(self):
        return self.pompa.get_consumo_idro()