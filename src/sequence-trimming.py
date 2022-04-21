'''
NAME
    sequence-trimming

VERSION
    3.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/sequence-trimming.py

DESCRIPTION
    Corta los adaptadores de las secuencias que se encuentran en el 
    archivo data/4_input_adapters.txt, sabiendo que los adaptadores 
    se encuentran en las posiciones 1 a 14

CATEGORY
    DNA sequence

USAGE
    py src/sequence-trimming.py

ARGUMENTS
    None

INPUT
    Archivo con secuencias data/4_input_adapters.txt

OUTPUT
    Archivo con secuencias sin adaptadores
    results/4_output_no_adapters.txt

SEE ALSO
    None

'''

# Intentar ejecutar el programa
try:
    # Abrir archivo, guardar secuencias en una lista y cerrar archivo
    with open("data/4_input_adapters.txt", 'r') as sequences_file:
        sequences_list = sequences_file.readlines()

    # Abrir nuevo archivo, escribir cada secuencia sin adaptadores y 
    # cerrar archivo
    with open("results/4_output_no_adapters.txt", 'w') as no_adapters_file:
        for sequence in sequences_list:
            no_adapters_sequence = sequence[14:]
            no_adapters_file.write(no_adapters_sequence)

    # Informar al usuario que el archivo sin adaptadores se ha creado
    print("\nSe ha generado el archivo 4_output_no_adapters.txt \
          \nEl archivo se encuentra disponible en la carpeta results/ \n")

# Si no se encuentra el archivo data/4_input_adapters.txt, notificarlo
except IOError as io_error:
    print(f"\nEl archivo {io_error.filename} no se encuentra.\n")
