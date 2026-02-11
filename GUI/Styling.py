
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.initUI()


    def initUI(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        centralWidget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
            font-size: 30px;
            font-family: Times new Roman;
            padding: 10px 40px;
            margin: 20px;
            border: 2px solid;
            border-radius: 15px;       
            }
                           
            QPushButton#button1{
                background-color: hsl(288, 84%, 51%);
                           }
            QPushButton#button2{
                background-color: hsl(223, 63%, 47%);
                           }
            QPushButton#button3{
                background-color: hsl(67, 49%, 48%);
                           }
            
                           
            QPushButton#button1:hover{
                background-color: hsl(288, 84%, 80%);
                           }
            QPushButton#button2:hover{
                background-color: hsl(223, 63%, 80%);
                           }
            QPushButton#button3:hover{
                background-color: hsl(67, 49%, 80%);
                           }

        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


