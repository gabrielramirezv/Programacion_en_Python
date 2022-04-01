'''
NAME
    dna-fasta

VERSION
    0.3

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

## 1. Inicio

## 2. Abrir el archivo, leer el contenido y cerrar el archivo
dna_file = open("data/dna.txt", 'r')
dna_sequence = dna_file.read()
dna_file.close()

## 3. Abrir nuevo archivo, escribir secuencia en FASTA y cerrar archivo
fasta_file = open("results/dna.fasta", 'w')
fasta_file.write(f">sequence_name\n{dna_sequence}")
fasta_file.close()

## 4. Informar al usuario que el archivo FASTA se ha creado
print("\nSe ha generado el archivo dna.fasta \nEl archivo se encuentra disponible en la carpeta results/ \n")

## 5. Fin
