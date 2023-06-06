from constants import *

def detectarVulnerabilidades(password):
    
    if not EXPRESIONREGULAR.search(password):
        print("Su contraseña es demasido debil. No contiene caracteres especiales.")
    elif not MAYUSCULAS.search(password):
        print("Su contraseña debee poseer al menos una letra en mayuscula.")
    elif not NUMEROS.search(password) or len(NUMEROS.findall(password)) < 4:
        print("Su contraseña debe poseer al menos cuatro numeros.")
    
      


    
