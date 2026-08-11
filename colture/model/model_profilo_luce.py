from util.simple_model import Simple_Model


# Model di un profilo luce: tipo di luce consigliato per ogni fase fenologica.
class Model_Profilo_Luce(Simple_Model):

    def __init__(self, id):
        super().__init__("Profilo_Luce",id)

    # Restituisce la luce consigliata per la fase fenologica indicata.
    def get_luce_per_fase(self,fase):
        return self.info[fase]

    # Rappresentazione HTML (tabella) del profilo luce.
    def __str__(self):
        string = '''
        <style>
        table, tr, td{
                border: 1px solid grey;
        }
        </style>
        <table>'''
        row1 = "<tr>"
        row2 = "<tr>"
        for prop in  self.info.keys():
            if prop != 'id':
                row1 += "<td>" + str(prop) + "</td>"
                row2 += "<td>" + str(self.info[prop]) + "</td>"
        row1 += "</tr>"
        row2 += "</tr>"
        string += row1 + row2 + "</table>"
        return string
