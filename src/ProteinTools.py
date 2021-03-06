'''
NAME
    ProteinTools

VERSION
    1.1

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/ProteinTools.py

DESCRIPTION
    Herramientas para el manejo de secuencias proteicas

CATEGORY
    Protein sequence

USAGE
    import ProteinTools

SEE ALSO
    FastaTools

'''

def get_aa_percentages(protein_sequence, amino_acids_list, decimals=4):
    '''
    Calcula el porcentaje de los aminoacidos mencionados en una lista
    dentro de una secuencia proteica.
        Parameters:
            protein_sequence (str): Secuencia proteica a analizar
            amino_acids_list (list): Lista de aminoacidos a buscar en
                la secuencia
            decimals (int): Decimales a redondear (default=4)
        Returns:
            aa_acumulated percentage (float): Porcentaje total de la 
                secuencia que esta conformado por los aminoacidos dados
    '''
    # Estandarizar la secuencia a mayusculas
    protein_sequence = protein_sequence.upper()
    
    # Crear la lista de porcentajes
    aa_percentages_list = list()
    
    # Calcular el porcentaje para cada aminoacido y agregarlo a la lista
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
        amino_acid_percentage = round(amino_acid_percentage, decimals)
        
        # Agregar el porcentaje del aminoacido a la lista de porcentajes
        aa_percentages_list.append(amino_acid_percentage)
        
    # Devolver la lista de porcentajes
    return aa_percentages_list
