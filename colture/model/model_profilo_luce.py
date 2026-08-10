from util.simple_model import Simple_Model

'''
    Implentazione della classe Model_Profilo_Luce
    Implementa un model per il profilo luce
'''

class Model_Profilo_Luce(Simple_Model):

    '''
        Costruttore
        Parametri:
            (int) id, id della soluzione        
    '''

    def __init__(self, id):
        super().__init__("Profilo_Luce",id)
    
    '''
        Restituisce la luce consigliata per la fase fenologica specificata
        Parametri:
            (string) fase fenologica
        Return:
            (string) luce consigliata
    '''


    def get_luce_per_fase(self,fase):
        return self.info[fase]
    
    '''
        Ridefinisce il magic method __str__
        Return:
            (string) formattazione html di un profilo luce
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
                row1 += "<td>" + str(prop) + "</td>" 
                row2 += "<td>" + str(self.info[prop]) + "</td>"
        row1 += "</tr>"
        row2 += "</tr>"
        string += row1 + row2 + "</table>"
        return string