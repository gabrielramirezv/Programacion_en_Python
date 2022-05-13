'''
NAME
    amino_acid_content

VERSION
    0.1

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    

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

## 1. Inicio de la funcion
def get_aa_percentage(protein_sequence, amino_acid):
    
## 2. Estandarizar a mayusculas los parametros que recibe la funcion
    protein_sequence = protein_sequence.upper()
    amino_acid = amino_acid.upper()
    
## 3. Contar las veces que aparece el aminoacido en la secuencia proteica
    amino_acid_count = protein_sequence.count(amino_acid)
    
## 4. Calcular la longitud de la secuencia
    protein_sequence_length = len(protein_sequence)
    
## 5. Calcular el porcentaje del aminoacido dentro de la secuencia
    amino_acid_content = (amino_acid_count / protein_sequence_length) * 100
    
## 6. Fin de la funcion (devolver el porcentaje del aminoacido en la secuencia)
    return amino_acid_content