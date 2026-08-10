from util.simple_model import Simple_Model

'''
    Implementazione della classe Model_Soluzione
    Implementa un model per la rappresentazione di una soluzione circolante
'''

class Model_Soluzione(Simple_Model):

    '''
        Costruttore
        Parametro:
            (int) id, id della soluzione
    '''

    def __init__(self, id):
        super().__init__("Soluzione_Circolante",id)
    
    '''
        Ridefinisce il magic method __str__
        Return:
            (string) formattazione html di una soluzione circolante
    '''

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