'''
NAME
    AT_GC_percentage

VERSION
    1.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/AT_GC_percentage.py

DESCRIPTION
    Calcula el porcentaje de AT y GC de una secuencia de DNA

CATEGORY
    DNA sequence

USAGE
    py AT_GC_percentage.py

ARGUMENTS
    None

INPUT
    Ruta y nombre de un archivo que contiene una secuencia de DNA

OUTPUT
    Porcentaje de AT y GC en la secuencia de DNA

SEE ALSO
    None

'''

## 1. Inicio

## 2. Leer desde teclado la ruta y nombre del archivo con la secuencia
dna_file_name = input("Archivo de secuencia: ")

## 3. Abrir el archivo, leer el contenido y cerrar el archivo
dna_file = open(dna_file_name, 'r')
dna_sequence = dna_file.read()
dna_file.close()

## 4. Eliminar caracteres ajenos a la secuencia de DNA
dna_sequence.rstrip('\n')

## 5. Contar A, T, G, C y la longitud de la secuencia
a_count = dna_sequence.count('A')
t_count = dna_sequence.count('T')
g_count = dna_sequence.count('G')
c_count = dna_sequence.count('C')
dna_length = len(dna_sequence)

## 6. Calcular porcentaje de AT y GC en la secuencia de DNA
AT_percentage = ((a_count + t_count) / dna_length) * 100
GC_percentage = ((g_count + c_count) / dna_length) * 100

## 7. Imprimir resultados
print(f"La secuencia de DNA es {dna_sequence}\n Porcentaje de AT y GC\n AT: {AT_percentage} %\n GC: {GC_percentage} %")

## 8. Fin
