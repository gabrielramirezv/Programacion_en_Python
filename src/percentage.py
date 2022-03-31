'''
NAME
    nucleotide_percentage

VERSION
    1.0

AUTHOR
    Gabriel Ramírez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/61d4b35d7c6ac6975fb6d9e7c631beecb402124c/src/nucleotide_percentage.py

DESCRIPTION
    Este script sirve para calcular el porcentaje de AT y GC en una secuencia de DNA.

CATEGORY
    DNA sequence

USAGE


ARGUMENTS


SEE ALSO

'''

######## Obtener de la secuencia de DNA a partir de un archivo
# Solicitar la ruta y nombre del archivo al usuario y remover saltos de linea de la ruta para evitar posibles errores
dna_file_name = input("Ingresa la ruta y nombre del archivo que contiene la secuencia de DNA:\n")
dna_file_name = dna_file_name.rstrip("\n")
# Abrir archivo
dna_file = open(dna_file_name, "r")
# Guardar la secuencia en una variable
dna = dna_file.read()
# Cerrar archivo
dna_file.close()

######## Imprimir la secuencia, calcular el porcentaje de AT y GC e imprimirlo a pantalla
print(f"La secuencia es {dna} \n Porcentaje de AT y GC \n AT: {((dna.count('A') + dna.count('T')) / len(dna)) * 100} % \n GC: {((dna.count('G') + dna.count('C')) / len(dna)) * 100} %")