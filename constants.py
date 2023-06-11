import re


EXPRESIONREGULAR = re.compile(r'[^\w\s]') # busca caracteres que no sean letras ni espacios en blanco.
MAYUSCULAS = re.compile(r'[A-Z]') # busca mayusculas
NUMEROS = re.compile(r'[\d+]')
CARACTERES = {0: 'Ñ', 1: '!', 2: '#'}
LENCARACTERES = len(CARACTERES)


MSG_DICT = { "corta": "Su contraseña debe poseer al menos un caracter especial", 
            "letraMayus" : "Su contraseña debee poseer al menos una letra en mayuscula.",
            "numeros" : "Su contraseña debe poseer al menos cuatro numeros."}

OPCIONES = { "validar" : "Validar contraseña", "encriptar": "Encriptar contraseña", "desencriptar" : "Desencriptar contraseña"}