from attuatore_generico.interface.model_att import Model_Att
from colture.model.lista_colture import Lista_Colture
from colture.model.lista_soluzioni import Lista_Soluzioni


# Model della pompa: gestisce pH, EC, soluzione circolante e consumi idrico/elettrico.
class Model_Pompa(Model_Att):

    # Carica i dati della pompa e la coltura del settore associato.
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

    # Imposta la salinità (EC) corrente della soluzione.
    def on_change_ec(self,value):
        self.info["EC"]=float(value)

    # Imposta il pH corrente della soluzione.
    def on_change_ph(self,value):
        self.info["pH"]=float(value)

    # Imposta il profilo (id) della soluzione circolante.
    def on_change_sol(self,newid):
        self.info["id_soluzione_circolante"]=newid

    # Restituisce il pH corrente della soluzione.
    def get_ph(self):
        return self.info["pH"]

    # Restituisce la salinità (EC) corrente della soluzione.
    def get_ec(self):
        return self.info["EC"]

    # Consumo elettrico orario: il valore nominale se la pompa è accesa, altrimenti 0.
    def get_consumo_el(self):
        if self.info["switch"]:
            return self.info["consumo_elettrico"]
        else:
            return 0

    # Consumo idrico orario: il valore nominale se la pompa è accesa, altrimenti 0.
    def get_consumo_idro(self):
        if self.info["switch"]:
            return self.info["consumo_idrico"]
        else:
            return 0

    # Restituisce il profilo soluzione attualmente circolante.
    def get_sol(self):
        id_sol=self.info["id_soluzione_circolante"]
        data = Lista_Soluzioni().get_by_id(id_sol)
        return data

    # Restituisce il profilo soluzione consigliato per la coltura piantata.
    def get_sol_cons(self):
        return self.coltura.get_raw_sol()

    # Restituisce la salinità (EC) consigliata per la coltura piantata.
    def get_ec_cons(self):
        return self.coltura.get_ec_cons()

    # Restituisce il pH consigliato per la coltura piantata.
    def get_ph_cons(self):
        return self.coltura.get_ph_cons()

    # Restituisce l'elenco descrittivo dei profili soluzione disponibili.
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

    # True se le impostazioni (profilo, EC o pH) differiscono da quelle consigliate.
    def is_oor(self):
        return  self.get_sol_cons().get_id() != self.get_sol().get_id() or self.get_ec() != self.get_ec_cons() or self.get_ph() != self.get_ph_cons()
