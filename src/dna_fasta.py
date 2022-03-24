'''
NAME
    dna_fasta

VERSION
    1.0

AUTHOR
    Gabriel Ramírez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/61d4b35d7c6ac6975fb6d9e7c631beecb402124c/src/dna_fasta.py

DESCRIPTION
    Este script sirve para crear un archivo FASTA de una secuencia de DNA a partir de un archivo que contiene dicha secuencia.

CATEGORY
    DNA sequence

USAGE


ARGUMENTS


SEE ALSO

'''

######## Obtener la secuencia de DNA a partir del archivo data/dna.txt
# Abrir archivo
dna_file = open("data/dna.txt", "r")
# Guardar la secuencia de DNA en una variable
dna = dna_file.read()
# Cerrar archivo
dna_file.close()

######## Crear archivo FASTA
# Abrir archivo
fasta_file = open("results/dna.fasta", "w")
# Escribir el archivo siguiendo el formato FASTA
fasta_file.write(f">sequence_name\n{dna}")
# Cerrar el archivo
fasta_file.close()