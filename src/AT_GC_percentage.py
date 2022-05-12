'''
NAME
    AT_GC_percentage

VERSION
    5.0

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
import argparse

# Definir errores para bases no validas introducidas por el usuario
class InvalidBaseError(Exception):
    pass
class AmbiguousBaseError(Exception):
    pass

# Crear el parser
parser = argparse.ArgumentParser(description="Script que calcula el "
        + "contenido de AT y GC a partir de la ruta del archivo que "
        + "contiene una secuencia de DNA.")

# Agregar y almacenar los argumentos
parser.add_argument("-i", "--input",
                    metavar="path/to/input/file",
                    help="File with gene sequences",
                    required=True)

parser.add_argument("-o", "--output",
                    metavar="path/to/output/file",
                    help="Path for the output file",
                    required=False)
                    
parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    required=False)
  
args = parser.parse_args()

# Leer la ruta y nombre del archivo con la secuencia
dna_file_name = args.input

# Intentar leer el archivo de secuencia
try:
    # Abrir el archivo, leer el contenido y cerrar el archivo
    with open(dna_file_name, 'r') as dna_file:
        dna_sequence = str(dna_file.read().replace('\n', ''))
    
    # Si hay un caracter distinto a las cuatro bases aceptadas, 
    # generar un error
    if re.search("[^ATCGN]", dna_sequence):
        raise InvalidBaseError(f"{dna_file_name} no contiene secuencia valida")
        
    if dna_sequence.count("N") > 0:
        N_count = dna_sequence.count("N")
        raise AmbiguousBaseError(f"La secuencia contiene {N_count} N's")
        
# Si no se encuentra el archivo de secuencia, notificarlo
except IOError as io_error:
    print(f"\nEl archivo {io_error.filename} no se encuentra.\n")

# Si hay una base no valida, notificarlo al usuario
except InvalidBaseError as invalid_base_error:
    print(invalid_base_error.args[0] 
          + ". Las bases aceptadas son A, T, C y G.\n")
        
except AmbiguousBaseError as ambiguous_base_error:
    print("\nSecuencia ambigua. " + ambiguous_base_error.args[0] + '\n\n')

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

    # Si se especifica el numero de decimales, redondear
    if args.round:
        at_percentage = round(at_percentage, args.round)
        gc_percentage = round(gc_percentage, args.round)

    # Imprimir resultados
    if args.output:
        with open(args.output, 'w') as output_file:
            print(f"La secuencia de DNA es {dna_sequence}\
                  \nSecuencia obtenida del archivo {dna_file_name} \
                  \n\n Porcentaje de AT: {at_percentage} % \
                  \n Porcentaje de GC: {gc_percentage} %",
                  file=output_file)
                  
        print(f"\nSe ha generado el archivo {args.output}"
              + " con el contenido de AT\n\n")
        
    else:
        print(f"\nLa secuencia de DNA es {dna_sequence}\
              \nSecuencia obtenida del archivo {dna_file_name} \
              \n\n Porcentaje de AT: {at_percentage} %\n\n")
    