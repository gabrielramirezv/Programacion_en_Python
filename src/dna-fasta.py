'''
NAME
    dna-fasta

VERSION
    2.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/dna-fasta.py

DESCRIPTION
    Dado un archivo dna.txt que contiene una secuencia de DNA, genera
    un nuevo archivo con la misma secuencia en formato FASTA.

CATEGORY
    DNA sequence

USAGE
    py src/dna-fasta.py

ARGUMENTS
    None

INPUT
    Archivo data/dna.txt que contiene una secuencia de DNA sin formato

OUTPUT
    Archivo nuevo results/dna.fasta con la secuencia en formato FASTA
    Nota: El nuevo archivo dna.fasta se guarda en la carpeta results/

SEE ALSO
    None

'''

# Abrir el archivo, leer el contenido y cerrar el archivo
with open("data/dna.txt", 'r') as dna_file:
    dna_sequence = dna_file.read()

# Abrir nuevo archivo, escribir secuencia en FASTA y cerrar archivo
with open("results/dna.fasta", 'w') as fasta_file:
    fasta_file.write(f">sequence_name\n{dna_sequence}")

# Informar al usuario que el archivo FASTA se ha creado
print("\nSe ha generado el archivo dna.fasta \
      \nEl archivo se encuentra disponible en la carpeta results/ \n")
