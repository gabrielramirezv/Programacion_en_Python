'''
NAME
    FastaTools

VERSION
    1.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    

DESCRIPTION
    Herramientas para el manejo de archivos FASTA

CATEGORY
    FASTA files (Module)

USAGE
    import FastaTools

SEE ALSO
    ProteinTools

'''

# Standard library imports
import re


def get_sequence_from_fasta_file(fasta_file_name):
    '''
    Obtiene la secuencia de nucleotidos o aminoacidos desde un archivo 
    con formato FASTA.
        Parameters:
            fasta_file_name (str): Ruta y nombre del archivo FASTA
        Returns:
            sequence (str): Secuencia de nucleotidos o aminoacidos
    '''
    # Intentar leer el archivo FASTA
    try:
        with open(fasta_file_name, 'r') as fasta_file:
            sequence = ""
            # Si la linea no es el encabezado, agregarla a la secuencia
            for line in fasta_file:
                if not re.search("^>.+", line):
                    sequence_fragment = line.strip('\n')
                    sequence += sequence_fragment
                    
    # Si no se encuentra el archivo de secuencia, notificarlo
    except IOError as io_error:
        print(f"\nEl archivo {io_error.filename} no se encuentra.\n")
        
    # Devolver la secuencia obtenida
    return sequence
        
