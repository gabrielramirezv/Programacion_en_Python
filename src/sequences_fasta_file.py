'''
NAME
    sequences_fasta_file

VERSION
    3.0

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

# Intentar leer archivo con secuencias
try:
    # Abrir archivo, guardar las lineas en una lista y cerrar archivo
    with open("data/dna_sequences.txt", 'r') as sequences_file:
        file_lines = sequences_file.readlines()

# Si no se encuentra el archivo con secuencias, notificarlo
except IOError as io_error:
    print(f"\nEl archivo {io_error.filename} no se encuentra.\n")

# Si se encuentra el archivo con secuencias, formatear a FASTA
else:
    # Abrir nuevo archivo FASTA, escribir secuencias y cerrar archivo
    with open("results/dna_sequences.fasta", 'w') as fasta_file:
        # Para cada linea en la lista, crear una lista con el ID y la 
        # secuencia, estandarizar la secuencia y formatarla a FASTA
        for line in file_lines:
            line_elements = line.split("   ")
            seq_id = line_elements[0]
            sequence = line_elements[1]
            standard_sequence = sequence.upper().replace('-', '')
            fasta_file.write(f"> {seq_id}\n{standard_sequence}")

    # Informar al usuario que el archivo FASTA se ha creado
    print("\nSe ha generado el archivo dna_sequences.fasta \
        \nEl archivo se encuentra disponible en la carpeta results/ \n")
