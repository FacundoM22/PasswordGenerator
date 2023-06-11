import sys
from constants import OPCIONES
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from metods_gui import btnEjecutar,  comprobarEstado

class ejemplo_GUI(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui_menu.ui", self)
        self.cbOpciones = self.cb_Opciones
        self.btnEjecutar = self.btn_Ejecutar
        self.lblContrasenia = self.lbl_Contrasenia
        self.lblContrasenia2 = self.lbl_Contrasenia2
        self.txtContrasenia = self.txt_Contrasenia
        self.txtContrasenia2 = self.txt_Contrasenia2
        self.lblMensaje = self.lbl_Mensaje
        self.lblSemilla = self.lbl_Semilla
        self.txtSemilla = self.txt_Semilla
        self.lblMensaje.setWordWrap(True)
        self.txtContrasenia2.hide()
        self.lblContrasenia2.hide()
        self.lblSemilla.hide()
        self.txtSemilla.hide()
        self.lblMensaje.hide()

        self.cbOpciones.addItem(OPCIONES["validar"])
        self.cbOpciones.addItem(OPCIONES["encriptar"])
        self.cbOpciones.addItem(OPCIONES["desencriptar"])
        

        self.btnEjecutar.clicked.connect(lambda: btnEjecutar(self))
        self.cbOpciones.currentIndexChanged.connect(lambda: comprobarEstado(self))




