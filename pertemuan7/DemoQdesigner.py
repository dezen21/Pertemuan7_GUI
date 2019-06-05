import sys

from Desain_GUI_2 import *
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class MainForm(QDialog):
    def __init(self,parent = None):
        Qdialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.hallo.clicked.connect(self.halloClicked)

    def halloClicked(self):
        QMessageBox.information(self, 'Demo Qt Designer',
        'Hallo %s apa kabar ?' %self.ui.namaEdit.setText())

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
