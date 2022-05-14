'''
NAME
    amino_acid_content

VERSION
    2.0

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

def get_aa_percentage(
        protein_sequence, 
        amino_acids_list=['A','I','L','M','F','W','Y','V']):
    
    # Estandarizar la secuencia a mayusculas
    protein_sequence = protein_sequence.upper()
    
    # Inicializar el porcentaje acumulado a cero
    aa_acumulated_percentage = 0
    
    # Calcular el porcentaje para cada aminoacido y acumularlo
    for amino_acid in amino_acids_list:
        
        # Estandarizar el aminoacido a mayusculas y contar sus 
        # repeticiones en la secuencia
        amino_acid = amino_acid.upper()
        amino_acid_count = protein_sequence.count(amino_acid)
        
        # Calcular la longitud de la secuencia
        protein_sequence_length = len(protein_sequence)
        
        # Calcular el porcentaje del aminoacido dentro de la secuencia
        amino_acid_percentage = (amino_acid_count 
                                 / protein_sequence_length) * 100
        
        # Acumular el porcentaje
        aa_acumulated_percentage += amino_acid_percentage
        
    # Devolver el porcentaje del aminoacido en la secuencia
    return aa_acumulated_percentage


# Crear el parser
parser = argparse.ArgumentParser(description="Script que calcula el "
        + "contenido de un aminoacido en una secuencia proteica.")

# Agregar y almacenar los argumentos
parser.add_argument("-s", "--sequence",
                    help="Protein sequence to analyze",
                    type=str,
                    required=True)
                    
parser.add_argument("-a", "--aminoacids",
                    help="Amino acids to search (single-letter code)",
                    type=list,
                    required=False)

parser.add_argument("-o", "--output",
                    metavar="path/to/output/file",
                    help="Path for the output file",
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
    