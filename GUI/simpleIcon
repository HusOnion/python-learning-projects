import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #name
        self.setWindowTitle("First GUI !")
        #place
        self.setGeometry(700,300,500,500)
        #Icon
        self.setWindowIcon(QIcon("onion.png"))

class main():
    app = QApplication(sys.argv)
    window = MainWindow()
    #to show the window
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
