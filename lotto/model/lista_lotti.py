from lotto.model.model_lotto import Model_Lotto
from util.lista import Lista
from util.singleton import Singleton
from datetime import datetime
import locale

'''
    Implementazione della classe Lista_Lotti
    Implementa una lista di lotti
'''

@Singleton
class Lista_Lotti(Lista):

    '''
        Costruttore
    '''

    def __init__(self):
        super().__init__(Model_Lotto, "Lotto")
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
    
    '''
        Restituisce un dizionario avente per chiave l'id del lotto
        e per valore un flag booleano posto a True se il lotto è coltivato
        ma non raccolto nei tempi previsti
        Percorso delle funzioni chiamata:
            util.simple_model.get_id(self)
            lotto.model.model_lotto.get_inizio(self)
            lotto.model.model_lotto.get_status(self)
            lotto.model.model_lotto.get_fine(self)
        Return: (dict) dizionario
    '''


    def get_diz_time_out_lotti(self, time):
        return { d.get_id() : d.get_inizio() != "mancante" and d.get_status() != "raccogliendo" and datetime.strptime(d.get_fine(),"%d %b %Y, %a %H:%M") < time for d in self.lista.values()}
    
    '''
        Restituisce un dizionario avente per chiave l'id del lotto
        e per valore un flag booleano posto a True se il lotto è
        coltivato e il suo indicatore di salute è al di sotto
        della soglia minima
        Percorso delle funzioni chiamata:
            util.simple_model.get_id(self)
            lotto.model.model_lotto.get_salute(self)
            lotto.model.model_lotto.get_status(self)
            lotto.model.model_lotto.get_thresold(self)
        Return: (dict) dizionario
    '''


    def get_diz_low_salute_lotti(self):
        return { d.get_id() : (d.get_status() == "coltivato" and d.get_salute() < d.get_salute_threshold(), d.get_salute()) for d in self.lista.values()}
    
    '''
        Restituisce un dizionario avente per chiave l'id del lotto
        e per valore un flag booleano posto a True se il lotto è vuoto
        Percorso delle funzioni chiamata:
            util.simple_model.get_id(self)
            lotto.model.model_lotto.get_status(self)
        Return: (dict) dizionario
    '''


    def get_diz_lotti_vuoti(self):
        return { d.get_id() : d.get_status() == "vuoto" for d in self.lista.values() }
    

    '''
        Restituisce l'indicatore di salute del lotto identificato dall'id
        Parametri:
            (int) id, id del lotto
        Percorso delle funzioni chiamata:
            lotto.model.model_lotto.get_salute(self)
        Return:
            (float) indicatore di salute
    '''

    def get_salute_lotto(self, id):
        return self.lista[id].get_salute()
    
    '''
        Restituisce l'id del settore in cui è presente il lotto
        identificato dal parametro id
        Parametri:
            (int) id, id del lotto
        Percorso delle funzioni chiamata:
            lotto.model.model_lotto.get_id_salute(self)
        Return:
            (int) id del settore
    '''

    def get_id_settore(self, id):
        return self.lista[id].get_id_settore()
    
    '''
        Restituisce un dizionario avente per chiave l'id del lotto
        e per valore un flag booleano posto a True se l'impianto di illuminazione
        presente nel lotto è acceso, a False altrimenti
        Percorso delle funzioni chiamata:
            util.simple_model.get_id(self)
            attuatore_generico.interface.model_att.get_switch(self)
        Return: (dict) dizionario
    '''

    def get_diz_off(self):
        return { d.get_id() : not d.luce_reg.get_switch() for d in self.lista.values()}
    
    '''
        Restituisce un dizionario avente per chiave l'id del lotto
        e per valore un flag booleano posto a True se l'impianto di illuminazione
        presente nel lotto non è impostato sui valori consigliati, a False altrimenti
        Percorso delle funzioni chiamata:
            util.simple_model.get_id(self)
            lotto.model.model_lotto.is_oor(self)
        Return: (dict) dizionario
    '''

    def get_diz_oor(self):
        return { d.get_id() : d.is_oor() for d in self.lista.values()}