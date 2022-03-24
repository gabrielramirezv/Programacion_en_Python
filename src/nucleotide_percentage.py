dna_file_name = input("Ingresa la ruta y nombre del archivo que contiene la secuencia de DNA:\n")

dna_file_name = dna_file_name.rstrip("\n")

dna_file = open(dna_file_name)
dna = dna_file.read()

print(f"La secuencia es {dna} \n Porcentaje de AT y GC \n AT: {((dna.count('A') + dna.count('T')) / len(dna)) * 100} % \n GC: {((dna.count('G') + dna.count('C')) / len(dna)) * 100} %")