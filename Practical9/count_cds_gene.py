# Count the number of coding sequences contained within each gene
import re  # Use re to deal with string-type variables.

# Ask the user to input one of the three stop codons.
# The user might accidentally input a wrong codon, so there should be error message printed out to warn them about it.
# The while loop here makes sure that the file won't run until a correct stop codon is inputted.
while True:
    stop_codon = input("Please input the stop codon:")  # Use function input which allows the user to type the codon.
    if not stop_codon == "TAA" and not stop_codon == "TAG" and not stop_codon == "TGA":
        error = "You are inputting an incorrect stop codon!!!" \
                "\nPlease choose one codon from TAA, TAG and TGA and re-input it."
        print(error)  # Print out the warnings.
    else:
        break

# Read the dna sequences.
dna = open("C:/Users/gioia/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")

# Open a new file to store all those sequences with their names and write each sequence in one single line.
file = open("gene_file.fa", "w")
dna_list = dna.read().split(">")
for seq in dna_list:
    if seq:
        seq_name = seq.split("\n")[0]
        seq_fa = "".join(seq.split("\n")[1:])  # Combing the lines into one.
        file.write(">" + seq_name + "\n" + seq_fa + "\n")  # Write the modified sequences in the file.

# Change the file into reading mode.
file = open("gene_file.fa", "r")

# Create a file to
selected = open("{}_stop_genes.fa".format(stop_codon), "w")
gene_name_pattern = re.compile(r'>(\S+)')
stop_codon_pattern = re.compile("{}$".format(stop_codon))
# Define two objects to store the names and sequences separately.
gene_name = ''
gene_sequence = ''
count = 0
for line in file:
    if line.startswith('>'):
        gene_name = gene_name_pattern.search(line).group()
    else:
        gene_sequence = line
        if stop_codon_pattern.search(line):
            count = len(re.findall(stop_codon, gene_sequence))  # Find out all the targeted stop codons and count the number of them.
            selected.write('{}:  {}\n{}\n'.format(gene_name, count, gene_sequence))
selected.close()
file.close()
dna.close()  # Close all the files.
