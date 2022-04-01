'''
NAME
    nucleotide-count

VERSION
    1.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/nucleotide-count.py

DESCRIPTION
    Calcula la frecuencia de A, T, C y G en una secuencia de DNA

CATEGORY
    DNA sequence

USAGE
    py nucleotide-count.py

ARGUMENTS
    None

INPUT
    Secuencia de DNA desde teclado

OUTPUT
    Frecuencia de A, T, C y G en la secuencia

SEE ALSO
    None

'''

## 1. Inicio

## 2. Leer secuencia de DNA desde teclado
dna_sequence = input("Introduce la secuencia de DNA: ")

## 3. Contar el total de A, T, C y G en la secuencia
a_count = dna_sequence.count('A')
t_count = dna_sequence.count('T')
c_count = dna_sequence.count('C')
g_count = dna_sequence.count('G')

## 4. Imprimir resultados
print(f"El total por base es:    A: {a_count}  T: {t_count}  C: {c_count}  G: {g_count}")

## 5. Fin
