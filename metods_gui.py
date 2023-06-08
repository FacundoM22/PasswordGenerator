from PyQt5.QtWidgets import QMessageBox
from constants import *
from cryptography.fernet import Fernet
import random



def encriptarContrasenia(gui):   
            key = Fernet.generate_key()
            gui.txtSemilla.show()
            gui.lblSemilla.show()
            gui.txtSemilla.setText(key.decode())
            objeto_cifrado = Fernet(key)
            texto_encriptado = objeto_cifrado.encrypt(str.encode(gui.txtContrasenia.text()))
            texto_encriptado = texto_encriptado.decode()
            gui.txtContrasenia2.setText(texto_encriptado)
            gui.lblContrasenia2.show()
            gui.txtContrasenia2.show()

def desencriptarContrasenia(gui):
      key = Fernet.generate_key()
      objeto_cifrado = Fernet(key)
      password = str.encode(gui.txtContrasenia.text())
      password =  objeto_cifrado.decrypt(password)
      gui.txtContrasenia2.setText(password)
      gui.lblContrasenia.show()
      gui.txtContrasenia2.show()


def validarContrasenia(gui):
        password = gui.txtContrasenia.text()
        if len(password) < 8:
                gui.lblMensaje.show()
                gui.lblMensaje.setText("Su contraseña debe poseer al menos 8 caracteres.")
                
        else:
                if not EXPRESIONREGULAR.search(password):
                    gui.lblMensaje.show()   
                    gui.lblMensaje.setText("Su contraseña es demasido debil. No contiene caracteres especiales.")
                elif not MAYUSCULAS.search(password):
                    gui.lblMensaje.show()
                    gui.lblMensaje.setText("Su contraseña debee poseer al menos una letra en mayuscula.")
                elif not NUMEROS.search(password) or len(NUMEROS.findall(password)) < 4:
                    gui.lblMensaje.show()
                    gui.lblMensaje.setText("Su contraseña debe poseer al menos cuatro numeros.")
                else:
                    generarMsgBox(gui)
                    
    

def generarMsgBox(gui):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Password generator")
        msg_box.setText("La contraseña es optima igualmente desea generar una contraseña mas robusta?")
        msg_box.addButton(QMessageBox.No)
        msg_box.addButton(QMessageBox.Ok)
        result = msg_box.exec()
        if result == QMessageBox.Ok:
              mejorarContrasenia(gui,gui.txtContrasenia.text())


def btnEjecutar(gui):
     if gui.chkEncriptar.isChecked(): 
           encriptarContrasenia(gui)
     elif gui.chkValidar.isChecked():
           validarContrasenia(gui)
     elif gui.chkDesencriptar.isChecked():
           desencriptarContrasenia(gui)


def mejorarContrasenia(gui,password):
      for num in CARACTERES:
            print(len(CARACTERES))
            password += CARACTERES[random.randint(num, len(CARACTERES))-1]
            gui.txtContrasenia.setText(password)
      

def comprobarEstado(gui):
      if gui.chkDesencriptar.isChecked():
            gui.txtContrasenia2.setEnabled(True)
            gui.lblContrasenia2.setEnabled(True)
      else:
            gui.txtContrasenia2.setEnabled(False)     
            gui.lblContrasenia2.setEnabled(False)



