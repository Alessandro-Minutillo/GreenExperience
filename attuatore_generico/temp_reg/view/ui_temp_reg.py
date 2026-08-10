from PyQt5 import QtCore
from attuatore_generico.interface.ui_att import Ui_Att

class Ui_Temp_Reg(Ui_Att):
    
    def retranslateUi(self, att):
        _translate = QtCore.QCoreApplication.translate
        att.setWindowTitle(_translate("att", "GreenExperience"))
        self.data_ora.setText(_translate("att", "DATA/ORA"))
        self.elettricita.setText(_translate("att", "Consumo elettrico (KWh)"))

        self.consumo_corrente.setText(_translate("att", "Consumo elettrico con le impostazioni correnti: "))
        self.valore_corrente.setText(_translate("att", "valore_corrente"))

        self.suggerimento.setText(_translate("att", "Suggerimento: il livello di temperatura consigliato per la coltura "))
        self.nome_coltura.setText(_translate("att", "nome_coltura "))
        self.e_label.setText(_translate("att", "è "))
        self.valore_consigliato.setText(_translate("att", "valore_consigliato"))

        self.consumo_medio.setText(_translate("att", "Consumo elettrico medio: "))
        self.valore_medio.setText(_translate("att", "valore_medio"))

        self.titolo.setText(_translate("att", "Impianto di riscaldamento/raffrescamento"))
        self.obiettivo.setText(_translate("att", "Livello di temperatura obiettivo (°C)"))
        self.indietro.setText(_translate("att", "indietro"))

        for label in [self.elettricita, self.consumo_corrente, self.valore_corrente, 
                        self.suggerimento, self.nome_coltura, self.e_label, self.valore_consigliato,
                        self.consumo_medio, self.valore_medio, self.obiettivo]:
            label.setObjectName("info_att")
        
        self.titolo.setObjectName("titolo_att")