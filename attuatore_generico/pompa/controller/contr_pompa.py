from attuatore_generico.pompa.model.lista_pompe import Lista_Pompe
from attuatore_generico.interface.contr_att import Contr_Att
"""
    Implementazione della classe Contr_Pompa

    Contiene i richiami delle funzioni definite nella classe Model_Pompa
    Costituisce il tramite tra la classe Model_Pompa e la classe Vista_Pompa.

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""
class Contr_pompa(Contr_Att):
    def __init__(self,id):
        self.id=id
        self.model = Lista_Pompe().get_by_id(id)
    """
        Cambia la salinità della soluzione circolante
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.on_change_ec(value)
        Parametri:
            value: nuovo valore della salinità della soluzione circolante
        Return:
            Nessuno
    """

    def on_change_ec(self,value):
        self.model.on_change_ec(value)
    """
        Cambia il pH della soluzione circolante
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.on_change_ph(value)
        Parametri:
            value: nuovo valore del pH della soluzione circolante
        Return:
            Nessuno
    """
    def on_change_ph(self,value):
        self.model.on_change_ph(value)
    """
        Cambia il profilo della soluzione circolante
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.on_change_sol(value)
        Parametri:
            index: indice del profilo soluzione da settare
        Return:
            Nessuno
    """
    def on_change_sol(self,index):
        self.model.on_change_sol(index)
    """
        Restituisce la salinità della soluzione del settore considerato
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.get_ec()
        Parametri:
            Nessuno
        Return:
            (float) la salinità della soluzione
    """
    def get_ec(self):
        return self.model.get_ec()
    """
        Restituisce il pH della soluzione del settore considerato
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.get_ph()
        Parametri:
            Nessuno
        Return:
            (float) il pH della soluzione
    """
    def get_ph(self):
        return self.model.get_ph()
    """
        Restituisce il consumo elettrico orario della pompa
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.get_consumo_el()
        Parametri:
            Nessuno
        Return:
            (int) il consumo elettrico orario
    """
    def get_consumo_el(self):
        return self.model.get_consumo_el()
    """
        Restituisce il consumo idrico orario della pompa
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.get_consumo_idro()
        Parametri:
            Nessuno
        Return:
            (int) il consumo idrico orario
    """
    def get_consumo_idro(self):
        return self.model.get_consumo_idro()
    """
        Restituisce la soluzione cicolante attuale
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.get_sol()
        Parametri:
            Nessuno
        Return:
            soluzione circolante attuale
    """
    def get_sol(self):
        return self.model.get_sol()
    """
        Restituisce la soluzione cicolante consigliata
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.get_sol_cons()
        Parametri:
            Nessuno
        Return:
            soluzione circolante consigliata
    """
    def get_sol_cons(self):
        return self.model.get_sol_cons()
    """
        Restituisce il pH consigliato
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.get_ph_cons()
        Parametri:
            Nessuno
        Return:
            (float) ph consigliato
    """
    def get_ph_cons(self):
        return self.model.get_ph_cons()
    """
        Restituisce il livello di salinità consigliato
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.get_ec_cons()
        Parametri:
            Nessuno
        Return:
            (float) ec consigliata
    """
    def get_ec_cons(self):
        return self.model.get_ec_cons()
    """
        Restituisce la lista di profili soluzione disponibili
        Percorso della funzione richiamata:
            attuatore_generico.pompa.model.model_pompa.get_list_profiles()
        Parametri:
            Nessuno
        Return:
            lista di profili soluzione
    """
    def get_list_profiles(self):
        return self.model.get_list_profiles()