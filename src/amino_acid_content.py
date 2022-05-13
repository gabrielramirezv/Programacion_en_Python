'''
NAME
    amino_acid_content

VERSION
    0.2

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/amino_acid_content.py

DESCRIPTION
    Calcula el porcentaje de un aminoacido en una secuencia proteica

CATEGORY
    Protein sequence

USAGE
    py amino_acid_content.py

ARGUMENTS
    None

SEE ALSO
    AT_GC_percentage

'''

def get_aa_percentage(protein_sequence, amino_acid):
    
    # Estandarizar a mayusculas los parametros que recibe la funcion
    protein_sequence = protein_sequence.upper()
    amino_acid = amino_acid.upper()
    
    # Contar las veces que aparece el aminoacido en la secuencia proteica
    amino_acid_count = protein_sequence.count(amino_acid)
    
    # Calcular la longitud de la secuencia
    protein_sequence_length = len(protein_sequence)
    
    # Calcular el porcentaje del aminoacido dentro de la secuencia
    amino_acid_content = (amino_acid_count / protein_sequence_length) * 100
    
    # Devolver el porcentaje del aminoacido en la secuencia
    return amino_acid_content
    

# Hacer pruebas
try:
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", 'M') == 5, \
        "Parece que el calculo del porcentaje es incorrecto. \
         \nError en assert get_aa_percentage(\"MSRSLLLRFLLFLLLLPPLP\", 'M') == 5"
    
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", 'r') == 10, \
        "Parece que no se aceptan aminoacidos en minusculas. \
         \nError en assert get_aa_percentage(\"MSRSLLLRFLLFLLLLPPLP\", 'r') == 10"
    
    assert get_aa_percentage("msrslllrfllfllllpplp", 'L') == 50, \
        "Parece que no se aceptan secuencias en minusculas. \
         \nError en assert get_aa_percentage(\"msrslllrfllfllllpplp\", 'L') == 50"
         
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", 'Y') == 0, \
        "Parece que se estan contando aminoacidos ausentes. \
         \nError en assert get_aa_percentage(\"MSRSLLLRFLLFLLLLPPLP\", 'Y') == 0"
    
# Informar si la funcion esta cumpliendo su proposito adecuadamente o reportar errores
except AssertionError as assertion_error:
    print("\nAlgo salio mal.\n"+ str(assertion_error) + "\n") 
       
else:
    print("\nTodo salio bien.\n\n")