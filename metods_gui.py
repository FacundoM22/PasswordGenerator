from PyQt5.QtWidgets import QMessageBox
from constants import *

def validarContrasenia(gui):
     
     if gui.chkValidar.isChecked():
        password = gui.txtContrasenia.text()
        if not EXPRESIONREGULAR.search(password):     
            gui.txtContrasenia2.setText("Su contraseña es demasido debil. No contiene caracteres especiales.")
        elif not MAYUSCULAS.search(password):
         gui.txtContrasenia2.setText("Su contraseña debee poseer al menos una letra en mayuscula.")
        elif not NUMEROS.search(password) or len(NUMEROS.findall(password)) < 4:
         gui.txtContrasenia2.setText("Su contraseña debe poseer al menos cuatro numeros.")
        else:
            generarMsgBox()
            
    
def generarMsgBox():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Password generator")
        msg_box.setText("La contraseña es optima igualmente desea generar una contraseña mas robusta?")
        msg_box.addButton(QMessageBox.No)
        msg_box.addButton(QMessageBox.Ok)
        result = msg_box.exec()


def mejorarContrasenia(gui):
    password = gui.txtContrasenia.text()



def encriptarContrasenia(gui):
    pass # Vamos a encriptarla.