'''
NAME
    sequences_fasta_file

VERSION
    2.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/sequences_fasta_file.py

DESCRIPTION
    Dado un archivo de secuencias, las convierte en formato FASTA

CATEGORY
    FASTA format

USAGE
    py src/sequences_fasta_file.py

ARGUMENTS
    None

INPUT
    Archivo data/dna_sequences.txt con las secuencias de DNA
    Nota: Las columnas de seq_id y secuencia se hallan separadas por
    tres espacios (barra espaciadora)

OUTPUT
    Archivo results/dna_sequences.fasta con las secuencias de DNA en 
    formato FASTA

SEE ALSO
    None

'''

# Abrir archivo, guardar las lineas en una lista y cerrar archivo
sequences_file = open("data/dna_sequences.txt", 'r')
file_lines = sequences_file.readlines()
sequences_file.close()

# Abrir nuevo archivo FASTA
fasta_file = open("results/dna_sequences.fasta", 'w')

# Para cada linea en la lista, crear una lista con el ID y la 
# secuencia, estandarizar la secuencia y escribirla en formato FASTA
for line in file_lines:
    line_elements = line.split("   ")
    seq_id = line_elements[0]
    sequence = line_elements[1]
    standard_sequence = sequence.upper().replace('-', '')
    fasta_file.write(f"> {seq_id}\n{standard_sequence}")

# Cerrar el nuevo archivo FASTA
fasta_file.close()

# Informar al usuario que el archivo FASTA se ha creado
print("\nSe ha generado el archivo dna_sequences.fasta \
      \nEl archivo se encuentra disponible en la carpeta results/ \n")
