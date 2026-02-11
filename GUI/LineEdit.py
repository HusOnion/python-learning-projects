
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit,QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.lineEdit = QLineEdit(self)
        self.Button = QPushButton("Submit", self)
        self.initUI()


    def initUI(self):
        self.lineEdit.setGeometry(20,20,200,50)
        self.Button.setGeometry(220,20,100,50)
        self.Button.setStyleSheet("font-size: 20px;"
                                    "font-family: Times new Roman;")
        self.lineEdit.setStyleSheet("font-size: 30px;"
                                    "font-family: Times new Roman;")
        
        self.lineEdit.setPlaceholderText("Enter your name")

        self.Button.clicked.connect(self.submit)
        
    
    def submit(self):
        text = self.lineEdit.text()
        print(text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
