'''
NAME
    AT_GC_percentage

VERSION
    2.0

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

# Leer desde teclado la ruta y nombre del archivo con la secuencia
dna_file_name = input("\nArchivo de secuencia: ")

# Intentar leer el archivo de secuencia
try:
    # Abrir el archivo, leer el contenido y cerrar el archivo
    with open(dna_file_name, 'r') as dna_file:
        dna_sequence = dna_file.read()
# Si no se encuentra el archivo de secuencia, notificarlo
except IOError as io_error:
    print(f"\nEl archivo {io_error.filename} no se encuentra.\n")

# Si se encuentra el archivo de secuencia, ejecutar el conteo
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
