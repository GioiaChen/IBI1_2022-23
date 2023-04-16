# Identifying those genes containing a 'TAG' stop codon
import re

# Open the fasta file which contains the DNA sequence information and only for reading.
dna = open("C:/Users/gioia/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")

# Each DNA sequence is shown separately in different lines, making it difficult for localizing the codons.
# Open a new file to store all those sequences with their names and write each sequence in one single line.
file = open("gene_file.fa", "w")  # Open the new file in the mode of writing.
dna_list = dna.read().split(">")  # Split the original file from the position of each DNA name.
for seq in dna_list:
    if seq:
        seq_name = seq.split("\n")[0]
        seq_fa = "".join(seq.split("\n")[1:])
        file.write(">" + seq_name + "\n" + seq_fa + "\n")
file = open("gene_file.fa", "r")  # Change the new file into reading mode.

# Create a file to store the selected DNA sequences which end with 'TGA'
selected = open("TGA_genes.fa", "w")

# Optimize regular expression using re.compile.
# The regular expression need to be used frequently later for searching.
# Repeated calls to a regular expression reuse this regular expression object, which be more efficient.
dna_name_pattern = re.compile(r'>(\S+)')  # Find the lines of dna names.
dna_sequence_pattern = re.compile('TGA$')  # Find the sequences that end with TGA.

dna_name = ''
dna_sequence = ''

for line in file:
    if line.startswith('>'):  # Pick out the lines of dna names.
        dna_name = dna_name_pattern.search(line).group()
    else:
        dna_sequence = line
        if dna_sequence_pattern.search(line):  # Search for the targeted sequences.
            selected.write('{}\n{}\n'.format(dna_name, dna_sequence))
selected.close()
file.close()
dna.close()  # Close all the files.
