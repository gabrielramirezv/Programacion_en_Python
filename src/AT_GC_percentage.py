'''
NAME
    AT_GC_percentage

VERSION
    4.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/AT_GC_percentage.py

DESCRIPTION
    Calcula el porcentaje de AT y GC de una secuencia de DNA

CATEGORY
    DNA sequence

USAGE
    py src/AT_GC_percentage.py

ARGUMENTS
    None

INPUT
    Ruta y nombre de un archivo que contiene una secuencia de DNA
    Al ejecutarse, se lee el archivo indicado por el usuario
    Nota: Los archivos con datos para programas se hallan en data/

OUTPUT
    Porcentaje de AT y GC en la secuencia de DNA

SEE ALSO
    None

'''

import re

# Definir error para bases no validas introducidas por el usuario
class InvalidBaseError(Exception):
    pass

# Leer desde teclado la ruta y nombre del archivo con la secuencia
dna_file_name = input("\nArchivo de secuencia: ")

# Intentar leer el archivo de secuencia
try:
    # Abrir el archivo, leer el contenido y cerrar el archivo
    with open(dna_file_name, 'r') as dna_file:
        dna_sequence = dna_file.read()
    
    # Si hay un caracter distinto a las cuatro bases aceptadas, 
    # generar un error InvalidBaseError()
    if re.search("[^ATCG]", dna_sequence):
        raise InvalidBaseError(f"{dna_file_name} no contiene secuencia valida")
        
# Si no se encuentra el archivo de secuencia, notificarlo
except IOError as io_error:
    print(f"\nEl archivo {io_error.filename} no se encuentra.\n")

# Si hay una base no valida, notificarlo al usuario
except InvalidBaseError as invalid_base_error:
    print(invalid_base_error.args[0] 
          + ". Las bases aceptadas son A, T, C y G.\n")

# Si se encuentra archivo de secuencia y las bases son validas, contar
else:
    # Eliminar caracteres ajenos a la secuencia de DNA
    dna_sequence.rstrip('\n')

    # Contar A, T, G, C y la longitud de la secuencia
    a_count = dna_sequence.count('A')
    t_count = dna_sequence.count('T')
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    dna_length = len(dna_sequence)

    # Calcular porcentaje de AT y GC en la secuencia de DNA
    at_percentage = ((a_count + t_count) / dna_length) * 100
    gc_percentage = ((g_count + c_count) / dna_length) * 100

    # Imprimir resultados
    print(f"\nLa secuencia de DNA es {dna_sequence}\
        \n Porcentaje de AT y GC\
        \n AT: {at_percentage} %\
        \n GC: {gc_percentage} %\n")
