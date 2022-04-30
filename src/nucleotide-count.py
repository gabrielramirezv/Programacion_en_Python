'''
NAME
    nucleotide-count

VERSION
    2.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/nucleotide-count.py

DESCRIPTION
    Calcula la frecuencia de A, T, C y G en una secuencia de DNA

CATEGORY
    DNA sequence

USAGE
    py src/nucleotide-count.py

ARGUMENTS
    None

INPUT
    Secuencia de DNA desde teclado

OUTPUT
    Frecuencia de A, T, C y G en la secuencia

SEE ALSO
    None

'''

import re

# Definir error para bases no validas introducidas por el usuario
class InvalidBaseError(Exception):
    pass

# Leer secuencia de DNA desde teclado
dna_sequence = input("\nIntroduce la secuencia de DNA: ").upper()

# Intentar llevar a cabo el conteo de nucleotidos
try:
    # Si hay un caracter distinto a las cuatro bases aceptadas, 
    # generar un error InvalidBaseError()
    if re.search("[^ATCG]", dna_sequence):
        raise InvalidBaseError("Secuencia de DNA no valida.")

    # Contar el total de A, T, C y G en la secuencia
    a_count = dna_sequence.count('A')
    t_count = dna_sequence.count('T')
    c_count = dna_sequence.count('C')
    g_count = dna_sequence.count('G')

    # Imprimir resultados
    print(f"El total por base es: \
        A: {a_count} \
        T: {t_count} \
        C: {c_count} \
        G: {g_count}\n")

# Si hay una base no valida, notificarlo al usuario
except InvalidBaseError as invalid_base_error:
    print(invalid_base_error.args[0] 
          + " Las unicas bases aceptadas son A, T, C y G.\n")
