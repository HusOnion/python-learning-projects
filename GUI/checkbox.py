
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.checkBox = QCheckBox("Do you love me? ", self)
        self.initUI()
        
        
    def initUI(self):
        self.checkBox.setGeometry(20,0,300,100)
        self.checkBox.setStyleSheet("font-size: 30px;"
                                    "font-family: Times new Roman;")
        
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.checking)

    def checking(self,state):
        if state == Qt.Checked:
            print("You love me!")
        else:
            print("Y..Yo...You Dont love me !")
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":  
    main()
