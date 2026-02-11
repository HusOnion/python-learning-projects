
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QRadioButton,QButtonGroup

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mada", self)
        self.radio3 = QRadioButton("Paypal", self)
        self.radio4 = QRadioButton("InStore", self)
        self.radio5 = QRadioButton("Online", self)
        self.buttonGroup1 = QButtonGroup(self)
        self.buttonGroup2 = QButtonGroup(self)
        self.initUI()


    def initUI(self):
        self.radio1.setGeometry(0,0,200,50)
        self.radio2.setGeometry(0,40,200,50)
        self.radio3.setGeometry(0,80,200,50)
        self.radio4.setGeometry(0,120,200,50)
        self.radio5.setGeometry(0,160,200,50)


        self.setStyleSheet("QRadioButton{"
                           "font-size: 30px;"
                           "font-family: Times new Roman;"
                           "Padding: 10px;"
                           "}")
        
        self.buttonGroup1.addButton(self.radio1)
        self.buttonGroup1.addButton(self.radio2)
        self.buttonGroup1.addButton(self.radio3)
        self.buttonGroup2.addButton(self.radio4)
        self.buttonGroup2.addButton(self.radio5)
        
        self.radio1.toggled.connect(self.radioButtonChanged)
        self.radio2.toggled.connect(self.radioButtonChanged)
        self.radio3.toggled.connect(self.radioButtonChanged)
        self.radio4.toggled.connect(self.radioButtonChanged)
        self.radio5.toggled.connect(self.radioButtonChanged)

    def radioButtonChanged(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print(f"{radioButton.text()} is selected")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


