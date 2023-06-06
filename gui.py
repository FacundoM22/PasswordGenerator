import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog


class ejemplo_GUI(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui_menu.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())