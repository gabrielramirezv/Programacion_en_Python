dna_file = open("data/dna.txt", "r")
dna = dna_file.read()
dna_file.close()

fasta_file = open("results/dna.fasta", "w")
fasta_file.write(f">sequence_name\n{dna}")
fasta_file.close()