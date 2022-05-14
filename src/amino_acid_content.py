'''
NAME
    amino_acid_content

VERSION
    1.1

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/amino_acid_content.py

DESCRIPTION
    Calcula el porcentaje de un aminoacido en una secuencia proteica

CATEGORY
    Protein sequence

USAGE
    py amino_acid_content.py [-h] -s SEQUENCE -a AMINOACID 
        [-o path/to/output/file] [-r ROUND]

ARGUMENTS
    -h, --help            show this help message and exit
    -s SEQUENCE, --sequence SEQUENCE
                        Protein sequence to analyze
    -a AMINOACID, --aminoacid AMINOACID
                        Amino acid to search (single-letter code)
    -o path/to/output/file, --output path/to/output/file
                        Path for the output file
    -r ROUND, --round ROUND
                        Number of digits to round

SEE ALSO
    AT_GC_percentage

'''

def get_aa_percentage(
        protein_sequence, 
        amino_acids_list=['A','I','L','M','F','W','Y','V']):
    
    # Estandarizar a mayusculas los parametros que recibe la funcion
    protein_sequence = protein_sequence.upper()
    
    aa_acumulated_percentage = 0
    
    for amino_acid in amino_acids_list:
        
        amino_acid = amino_acid.upper()
        
        # Contar las veces que aparece el aminoacido en la secuencia proteica
        amino_acid_count = protein_sequence.count(amino_acid)
        
        # Calcular la longitud de la secuencia
        protein_sequence_length = len(protein_sequence)
        
        # Calcular el porcentaje del aminoacido dentro de la secuencia
        amino_acid_percentage = (amino_acid_count / protein_sequence_length) * 100
        
        aa_acumulated_percentage += amino_acid_percentage
        
    # Devolver el porcentaje del aminoacido en la secuencia
    return aa_acumulated_percentage


# Hacer pruebas
try:
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5, \
        "Hubo un error en assert get_aa_percentage(\"MSRSLLLRFLLFLLLLPPLP\", [\"M\"]) == 5"
        
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55, \
        "Hubo un error en assert get_aa_percentage(\"MSRSLLLRFLLFLLLLPPLP\", ['M', 'L']) == 55"
        
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70, \
        "Hubo un error en assert get_aa_percentage(\"MSRSLLLRFLLFLLLLPPLP\", ['F', 'S', 'L']) == 70"
        
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65, \
        "Hubo un error en assert get_aa_percentage(\"MSRSLLLRFLLFLLLLPPLP\") == 65"

# Informar si la funcion esta cumpliendo su proposito adecuadamente o reportar errores
except AssertionError as assertion_error:
    print("\nAlgo salio mal.\n"+ str(assertion_error) + "\n") 

else:
    print("\nTodo salio bien.\n\n")
    