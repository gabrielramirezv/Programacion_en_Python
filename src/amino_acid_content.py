'''
NAME
    amino_acid_content

VERSION
    3.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/amino_acid_content.py

DESCRIPTION
    Calcula el porcentaje de una lista de aminoacidos en una secuencia 
    proteica

CATEGORY
    Protein sequence

USAGE
    py amino_acid_content.py [-h] -s SEQUENCE [-a AMINOACIDS] 
        [-o path/to/output/file] [-r ROUND]

ARGUMENTS
    -h, --help            show this help message and exit
    -s SEQUENCE, --sequence SEQUENCE
                        Protein sequence to analyze
    -a AMINOACIDS, --aminoacids AMINOACIDS
                        Amino acids to search (single-letter code)
    -o path/to/output/file, --output path/to/output/file
                        Path for the output file
    -r ROUND, --round ROUND
                        Number of digits to round

SEE ALSO
    AT_GC_percentage

'''

import argparse

from ProteinTools import get_aa_percentage


# Crear el parser
parser = argparse.ArgumentParser(description="Script que calcula el "
        + "contenido de un aminoacido en una secuencia proteica.")

# Agregar y almacenar los argumentos
parser.add_argument("-s", "--sequence",
                    help="Protein sequence to analyze",
                    type=str,
                    required=False)
                    
parser.add_argument("-f", "--file",
                    metavar="path/to/input/file",
                    help="Path for a file with a protein sequence "
                          + "(FASTA format is allowed)",
                    type=str,
                    required=False)

parser.add_argument("-n", "--newfile",
                    metavar="path/to/new/file",
                    help="Path to create a file with the protein "
                          + "sequence with format FASTA",
                    type=str,
                    required=False)
                    
parser.add_argument("-a", "--aminoacids",
                    help="Amino acids to search (single-letter code)",
                    type=list,
                    required=False)

parser.add_argument("-o", "--output",
                    metavar="path/to/output/file",
                    help="Path for the output file",
                    type=str,
                    required=False)
                    
parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    required=False)
  
args = parser.parse_args()


# Recibir secuencia y aminoacido como argumentos desde linea de comandos
protein_sequence = args.sequence
amino_acids_list = args.aminoacids

# Obtener el contenido de aminoacido en la secuencia
amino_acid_content = get_aa_percentage(protein_sequence, amino_acids_list)

# Redondear el porcentaje si fue solicitado por el usuario
if args.round:
    amino_acid_content = round(amino_acid_content, args.round)

# Imprimir el porcentaje en el archivo indicado por el usuario
if args.output:
        with open(args.output, 'w') as output_file:
            print(f"Secuencia proteica: {protein_sequence} \
                \nAminoacidos: {amino_acids_list} \
                \n\n Contenido de {amino_acids_list} en la secuencia:"
                + f" {amino_acid_content} %",
                  file=output_file)
                  
        print(f"\nSe ha generado el archivo {args.output}"
              + f" con el contenido de {amino_acids_list}.\n\n")

# Imprimir resultado a pantalla si no fue solicitado un archivo output
else:
    print(f"\nSecuencia proteica: {protein_sequence} \
        \nAminoacidos: {amino_acids_list} \
        \n\n Contenido de {amino_acids_list} en la secuencia:"
        + f" {amino_acid_content} %\n\n")
    