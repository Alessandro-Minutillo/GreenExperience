from lotto.model.lista_lotti import Lista_Lotti
from datetime import datetime
import locale

'''
    Implementazione della classe Contr_Lotto
    Implementa un controller per la gestione di un lotto
'''

class Contr_Lotto():

    '''
        Costruttore
        Percorso della funzione chiamata:
            util.lista.get_by_id(self,id)
    '''

    def __init__(self,id):
        self.model = Lista_Lotti().get_by_id(id)
        locale.setlocale(locale.LC_ALL,"it_IT.UTF-8")
    
    '''
        Restituisce l'id dell'impianto di illuminazione presente nel lotto
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_luce_id(self)
        Return:
            (int) id
    '''

    def get_luce_id(self):
        return self.model.get_luce_id()

    '''
        Restituisce l'id della centralina presente nel lotto
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_centralina_id(self)
        Return:
            (int) id
    '''

    def get_centralina_id(self):
        return self.model.get_centralina_id()

    '''
        Restituisce l'indicatore di salute del lotto
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_salute(self)
        Return:
            (float) indicatore di salute
    '''

    def get_salute(self):
        return self.model.get_salute()

    '''
        Restituisce lo stato attuale del lotto
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_status(self)
        Return:
            (string) status
    '''

    def get_status(self):
        return self.model.get_status()

    '''
        Restituisce la fase fenologica attuale del lotto
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_fasef(self)
        Return:
            (string) fase fenologica
    '''

    def get_fasef(self):
        return self.model.get_fasef()
    
    '''
        Restituisce la luce attualmente consigliata per il lotto
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_luce_cons(self)
        Return:
            (string) tipo di luce
    '''

    def get_luce_cons(self):
        return self.model.get_luce_cons()
    
    '''
        Restituisce, se esiste, la data in cui è iniziata la coltivazione
        del lotto
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_inizio(self)
        Return:
            (string) data
    '''

    def get_inizio(self):
        return "mancante" if self.model.get_inizio() == "mancante" else datetime.strftime( datetime.strptime(self.model.get_inizio(), "%d %b %Y, %a %H:%M") , "%d/%m/%Y")
    
    '''
        Restituisce, se esiste, la data in cui dovrebbe essere
        raccolto il lotto
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_fine(self)
        Return:
            (string) data
    '''

    def get_fine(self):
        return "mancante" if self.model.get_fine() == "mancante" else datetime.strftime( datetime.strptime(self.model.get_fine(), "%d %b %Y, %a %H:%M") , "%d/%m/%Y")
    
    '''
        Restituisce le eventuali note riguardanti il lotto
        Percorso della funzione chiamata:
            lotto.model.model_lotto.get_note(self)
        Return:
            (string) note
    '''

    def get_note(self):
        return self.model.get_note()

    '''
        Setta le note del lotto
        Parametri:
            (string) note, nuove note
        Percorso della funzione chiamata:
            lotto.model.model_lotto.change_note(self,note)
    '''

    def change_note(self,note):
        self.model.change_note(note)

    '''
        Ritorna il model
        Return:
            (Model_Lotto) model
    '''

    def get_model(self):
        return self.model
    
    '''
        Pianta il lotto
        Parametri:
            (datetime) time, istante in cui si inizia a piantare
        Percorso della funzione chiamata:
            lotto.model.model_lotto.pianta(self,time)
        Return:
            (bool) flag, esito dell'operazione
    '''

    def pianta(self, time):
        return self.model.pianta(time)
    
    '''
        Raccoglie il lotto
        Parametri:
            (datetime) time, istante in cui si inizia la raccolta
        Percorso della funzione chiamata:
            lotto.model.model_lotto.raccogli(self,time)
        Return:
            (bool) flag, esito dell'operazione
    '''

    def raccogli(self, time):
        return self.model.raccogli(time)
    
    '''
        Restituisce True se il lotto è pieno o è in stato di raccolta,
        False altrimenti
        Percorso delle funzioni chiamate:
            lotto.model.model_lotto.is_full(self)
            lotto.model.model_lotto.is_raccogliendo(self)
        Return:
            (bool) flag
    '''

    def is_full_or_raccogliendo(self):
        return self.model.is_full() or self.model.is_raccogliendo()