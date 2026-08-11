from util.simple_model import Simple_Model


# Model di una soluzione circolante: quantità di macroelementi.
class Model_Soluzione(Simple_Model):

    def __init__(self, id):
        super().__init__("Soluzione_Circolante",id)

    # Rappresentazione HTML (tabella) dei macroelementi della soluzione.
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
                row1 += "<td>" + str(prop).replace("quant_","") + "</td>"
                row2 += "<td>" + "{:.0f}".format(self.info[prop]) + "</td>"
        row1 += "</tr>"
        row2 += "</tr>"
        string += row1 + row2 + "</table>"
        return string
