from attuatore_generico.interface.model_att import Model_Att
from colture.model.lista_colture import Lista_Colture
from colture.model.lista_soluzioni import Lista_Soluzioni

"""
    Implementazione della classe Model_Pompa

    Contiene l'implementazioni fondamentali necessarie alla gestione della pompa.

    Autori:
    Alessandro Minutillo
    Davide Nunin
    Marco Ciammaichella
    Vito Scaraggi
"""
class Model_Pompa(Model_Att):

    def __init__(self, id):
        super().__init__("Pompa",id)
        self.ph_corr = self.info["pH"]
        self.ec_corr = self.info["EC"]
        self.consumo_idrico_curr = self.info["consumo_idrico"]
        self.consumo_elettrico_curr = self.info["consumo_elettrico"]
        self.id_soluzione = self.info["id_soluzione_circolante"]
        self.switch = self.info["switch"]
        id_coltura = self.retrieve_data("Settore", "id_coltura", "id_pompa", self.id)["id_coltura"]
        self.coltura = Lista_Colture().get_by_id(id_coltura)
    """
        Cambia il valore della salinità attuale della soluzione circolante
        Percorso della funzione richiamata:
            Nessuna
        Parametri:
            value: il nuovo valore (float) della salinità della soluzione
        Return:
            Nessuno
    """
    def on_change_ec(self,value):
        self.info["EC"]=float(value)
    """
        Cambia il valore del pH attuale della soluzione circolante
        Percorso della funzione richiamata:
            Nessuna
        Parametri:
            value: il nuovo valore (float) del pH della soluzione
        Return:
            Nessuno
    """
    
    def on_change_ph(self,value):
        self.info["pH"]=float(value)
    """
        Cambia il livello di macroelementi attuale della soluzione circolante
        Percorso della funzione richiamata:
            Nessuna
        Parametri:
            newid: il nuovo profilo della soluzione
        Return:
            Nessuno
    """

    def on_change_sol(self,newid):
        self.info["id_soluzione_circolante"]=newid

    """
        Restituisce il pH attuale della soluzione circolante
        Percorso della funzione richiamata:
            Nessuna
        Parametri:
            Nessuno
        Return:
            Nessuno
    """
    def get_ph(self):
        return self.info["pH"]
    """
        Restituisce la salinità attuale della soluzione circolante
        Percorso della funzione richiamata:
            Nessuna
        Parametri:
            Nessuno
        Return:
            Nessuno
    """

    def get_ec(self):
        return self.info["EC"]
    """
        Restituisce il consumo elettrico orario della pompa
        Percorso della funzione richiamata:
            Nessuna
        Parametri:
            Nessuno
        Return:
            Nessuno
    """

    def get_consumo_el(self):
        if self.info["switch"]:
            return self.info["consumo_elettrico"]
        else:
            return 0
    """
        Restituisce il consumo idrico orario della pompa
        Percorso della funzione richiamata:
            Nessuna
        Parametri:
            Nessuno
        Return:
            Nessuno
    """

    def get_consumo_idro(self):
        if self.info["switch"]:
            return self.info["consumo_idrico"]
        else:
            return 0
    """
        Restituisce restituisce il profilo soluzione attualmente presente nella soluzione della pompa
        Percorso della funzione richiamata:
            colture.model.Lista_Soluzioni().get_by_id(id_sol)
        Parametri:
            Nessuno
        Return:
            Soluzione circolante attuale
    """

    def get_sol(self):
        id_sol=self.info["id_soluzione_circolante"]
        data = Lista_Soluzioni().get_by_id(id_sol)
        return data
    """
        Restituisce il profilo soluzione consigliato per la coltura attualmente piantata nel settore
        Percorso della funzione richiamata:
            colture.model.model_coltura.self.coltura.get_raw_sol()
        Parametri:
            Nessuno
        Return:
            Soluzione circolante consigliata
    """

    def get_sol_cons(self):
        return self.coltura.get_raw_sol()
    """
        Restituisce il livello di salinità consigliato per la coltura attualmente presente nel settore
        Percorso della funzione richiamata:
            colture.model.model_coltura.get_ec_cons()
        Parametri:
            Nessuno
        Return:
            (float) ec consigliata
    """

    def get_ec_cons(self):
        return self.coltura.get_ec_cons()
    """
        Restituisce il pH consigliato per la coltura attualmente presente nel settore
        Percorso della funzione richiamata:
            colture.model.model_coltura.get_pH_cons()
        Parametri:
            Nessuno
        Return:
            (float) pH consigliato
    """

    def get_ph_cons(self):
        return self.coltura.get_ph_cons()
    """
        Restituisce la lista dei profili soluzioni possibili
        Percorso della funzione richiamata:
            colture.model.Lista_Soluzioni().lista.values()
        Parametri:
            Nessuno
        Return:
            lista dei profili soluzioni
    """

    def get_list_profiles(self):
        listof_profiles=Lista_Soluzioni().lista.values()
        listof_solutions=[]
        for i in listof_profiles:
            sol="id: "
            sol=sol+str(i.info["id"])+" "
            for a in i.info.keys():
                if a != "id":
                    sol=sol+str(i.info[a])+"/"
            listof_solutions.append(sol)
        return listof_solutions
    """
        Funzione che valuta se le impostazioni della pompa sono in linea con quelle migliori per la coltura piantata
        Percorso della funzione richiamata:
            Nessuna
        Parametri:
            Nessuno
        Return:
            (bool) flag true se le impostazioni sono ottime, flag false se non lo sono
    """

    def is_oor(self):
        return  self.get_sol_cons().get_id() != self.get_sol().get_id() or self.get_ec() != self.get_ec_cons() or self.get_ph() != self.get_ph_cons()