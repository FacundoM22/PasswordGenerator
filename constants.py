import re


EXPRESIONREGULAR = re.compile(r'[^\w\s]') # busca caracteres que no sean letras ni espacios en blanco.
MAYUSCULAS = re.compile(r'[A-Z]') # busca mayusculas
NUMEROS = re.compile(r'[\d+]')
CARACTERES = {0: 'Ñ', 1: '!', 2: '#'}



