'''
NAME
    AT-content

VERSION
    1.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    

DESCRIPTION
    Calcula el contenido de AT en una secuencia de DNA

CATEGORY
    DNA sequence

USAGE
    py src/AT_GC_percentage --input [PATH] [OPTIONS]

ARGUMENTS
    -i, --input     argumento necesario, lee la ruta del archivo con 
                    secuencia de DNA
                

OUTPUT
    Porcentaje de AT en la secuencia de DNA

SEE ALSO
    AT_GC_percentage

'''

import re

# Definir errores para bases no validas introducidas por el usuario
class InvalidBaseError(Exception):
    pass
class AmbiguousBaseError(Exception):
    pass

# Leer desde teclado la ruta y nombre del archivo con la secuencia
dna_file_name = input("\nArchivo de secuencia: ")

# Intentar leer el archivo de secuencia
try:
    # Abrir el archivo, leer el contenido y cerrar el archivo
    with open(dna_file_name, 'r') as dna_file:
        dna_sequence = dna_file.read()
        
    # Si hay un caracter distinto a las cuatro bases aceptadas, 
    # generar un error
    if re.search("[^ATCGN]", dna_sequence):
        raise InvalidBaseError(f"{dna_file_name} no contiene secuencia valida")
        
    if dna_sequence.count("N") > 0:
        raise AmbiguousBaseError(f"La secuencia contiene {dna_sequence.count('N')} N's")
        
# Si no se encuentra el archivo de secuencia, notificarlo
except IOError as io_error:
    print(f"\nEl archivo {io_error.filename} no se encuentra.\n")

# Si hay una base no valida, notificarlo al usuario
except InvalidBaseError as invalid_base_error:
    print(invalid_base_error.args[0] 
          + ". Las bases aceptadas son A, T, C y G.\n")

# Si se encuentra archivo de secuencia y las bases son validas
else:
    # Eliminar caracteres ajenos a la secuencia de DNA
    dna_sequence.rstrip('\n')

    # Contar A, T y la longitud de la secuencia
    a_count = dna_sequence.count('A')
    t_count = dna_sequence.count('T')
    dna_length = len(dna_sequence)

    # Calcular porcentaje de AT en la secuencia de DNA
    at_percentage = ((a_count + t_count) / dna_length) * 100

    # Imprimir resultados
    print(f"\nLa secuencia de DNA es {dna_sequence}\
    \n Porcentaje de AT y GC")