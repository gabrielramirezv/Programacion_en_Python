'''
NAME
    count_nucleotides

VERSION
    1.0

AUTHOR
    Gabriel Ramírez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/a0cd3abcacc973d648fec88f067914a840d776a5/src/count_nucleotides.py

DESCRIPTION
    Este script sirve para contar la frecuencia de nucleótidos en una secuencia de DNA.

CATEGORY
    DNA sequence

USAGE


ARGUMENTS


SEE ALSO

'''

# Solicitar la secuencia de DNA
dna = input("Ingresa una secuencia de DNA:\n")
# Contar las veces que aparece cada nucleotido e imprimir el conteo
print(f"Frecuencia de nucleotidos \n A: {dna.count('A')} \n T: {dna.count('T')} \n C: {dna.count('C')} \n G: {dna.count('G')}")