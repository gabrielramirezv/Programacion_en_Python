'''
NAME
    ProteinTools

VERSION
    0.1

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    

DESCRIPTION
    Herramientas para el manejo de secuencias proteicas

CATEGORY
    Protein sequence

USAGE
    import ProteinTools

SEE ALSO
    AT_GC_percentage

'''

def get_aa_percentage(
        protein_sequence, 
        amino_acids_list=['A','I','L','M','F','W','Y','V']):
    '''
    Calcula el porcentaje de los aminoacidos mencionados en una lista
    dentro de una secuencia proteica.
        Parameters:
            protein_sequence (str): Secuencia proteica a analizar
            amino_acids_list (list): Lista de aminoacidos a buscar en
                la secuencia
        Returns:
            aa_acumulated percentage (float): Porcentaje total de la 
                secuencia que esta conformado por los aminoacidos dados
    '''
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
