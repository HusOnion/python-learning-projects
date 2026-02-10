import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.initUI()

    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("O", self)
        label2 = QLabel("N", self)
        label3 = QLabel("I", self)
        label4 = QLabel("O", self)
        label5 = QLabel("N", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: blue;")
        label3.setStyleSheet("background-color: orange;")
        label4.setStyleSheet("background-color: purple;")
        label5.setStyleSheet("background-color: yellow;")

        grid = QGridLayout()
        
        grid.addWidget(label1, 0 ,1 )
        grid.addWidget(label2, 0 ,0 )
        grid.addWidget(label3, 1 ,1 )
        grid.addWidget(label4, 1 ,2 )
        grid.addWidget(label5, 0 ,2 )

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

