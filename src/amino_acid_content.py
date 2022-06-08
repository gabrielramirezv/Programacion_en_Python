'''
NAME
    amino_acid_content

VERSION
    5.0

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
    py amino_acid_content.py [-h] [-s SEQUENCE] [-f path/to/input/file] 
        [-a AMINOACIDS] [-o path/to/output/file] [-r ROUND]

ARGUMENTS
    -h, --help          Show a help message and exit
    -s SEQUENCE, --sequence SEQUENCE
                        Protein sequence to analyze
    -f path/to/input/file, --file path/to/input/file
                        Path for a file with a protein sequence 
                        (FASTA format is allowed)
    -a AMINOACIDS, --aminoacids AMINOACIDS
                        Amino acids to search (single-letter code)
    -o path/to/output/file, --output path/to/output/file
                        Path for the output file
    -r ROUND, --round ROUND
                        Number of digits to round

SEE ALSO
    AT_GC_percentage

'''

# Standard library imports
import argparse
import re

# Local application/library specific imports
from ProteinTools import get_aa_percentages
from FastaTools import get_sequence_from_fasta_file


# Definir errores para adecuado manejo de inputs
class LackOfInputError(Exception):
    pass
class DoubleInputError(Exception):
    pass


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
                    
parser.add_argument("-a", "--aminoacids",
                    help="Amino acids to search (single-letter code)",
                    type=list,
                    required=False,
                    default="ARNDCQEGHILKMFPSTWYV")

parser.add_argument("-o", "--output",
                    metavar="path/to/output/file",
                    help="Path for the output file",
                    type=str,
                    required=False)
                    
parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    required=False,
                    default=4)
  
args = parser.parse_args()


# Recibir secuencia y aminoacidos como argumentos desde linea de comandos
try:
    
    # Generar errores si no se ingreso archivo o secuencia, o si se 
    # ingresaron ambos a la vez
    if not (args.sequence or args.file):
        raise LackOfInputError("\nNo se cuenta con secuencia a analizar.")
    elif args.sequence and args.file:
        raise DoubleInputError("\nSe ingresaron secuencia y archivo a la vez.")
        
    # Si se ingresaron inputs de la forma correcta, obtener la secuencia
    elif args.sequence and not args.file:
        protein_sequence = args.sequence
    else:
        fasta_file_name = args.file
        protein_sequence = get_sequence_from_fasta_file(fasta_file_name)
        
    # Obtener la lista de aminoacidos
    amino_acids_list = args.aminoacids
    
    # Obtener decimales a redondear
    decimals = args.round
    
# Notificar exepciones al usuario
except LackOfInputError as lack_of_input_error:
    print(lack_of_input_error.args[0] 
          + " Ingrese un archivo FASTA de aminoacidos o una secuencia.\n")
except DoubleInputError as double_input_error:
    print(double_input_error.args[0] 
          + " Ingrese un archivo FASTA de aminoacidos o una secuencia.\n")


# Calcular porcentaje de aminoacidos si se leyeron datos exitosamente
else:
    
    # Obtener el contenido de aminoacidos en la secuencia
    aa_percentages_list = get_aa_percentages(
            protein_sequence, amino_acids_list, decimals)
            
    # Guardar aminoacidos a buscar en formato de string
    amino_acids = ', '.join(amino_acids_list)

    # Imprimir el porcentaje en el archivo indicado por el usuario
    if args.output:
        with open(args.output, 'w') as output_file:
            output_file.write(f"Secuencia proteica:\n")
            
            # Si el input es un archivo, escribir la secuencia 
            # linea por linea (conservar saltos de linea)
            if args.file:
                with open(fasta_file_name, 'r') as fasta_file:
                    for line in fasta_file:
                        if not re.search("^>.+", line):
                            output_file.write(line)
                            
            # Si el input es solo la secuencia, escribirla
            else:
                output_file.write(f"{protein_sequence}\n")
                
            # Escribir aminoacidos buscados
            output_file.write(f"\nAminoacidos buscados: {amino_acids} \
                \n\nContenido de aminoacidos en la secuencia:")
                
            # Escribir aminoacidos con sus porcentajes
            for position in range(0, len(amino_acids_list)):
                if aa_percentages_list[position]:
                    output_file.write(f"\n{amino_acids_list[position]}:  "
                                + f"{aa_percentages_list[position]} %")
            
            # Notificar al usuario que se ha creado el archivo
            print(f"\nSe ha generado el archivo {args.output}"
                + f" con el contenido de {amino_acids_list}.\n\n")


    # Imprimir resultado a pantalla si no fue solicitado archivo output
    else:
        print(f"\nSecuencia proteica: {protein_sequence} \
            \n\nAminoacidos buscados: {amino_acids} \
            \n\nContenido de aminoacidos en la secuencia:")
        for position in range(0, len(amino_acids_list)):
            if aa_percentages_list[position]:
                print(f"{amino_acids_list[position]}:  "
                       + f"{aa_percentages_list[position]} %")
        print('\n')
    