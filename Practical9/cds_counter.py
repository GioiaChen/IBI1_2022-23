# Coding sequence counter
import re  # use re to deal with string-type variables

# Create a string variable to store the sequence.
seq: str = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'

s = seq.find('ATG')  # Mark the position of the start codon 'ATG' with variable s.
# Since there is only one ATG which serves as the start codon,
# the number of the legal sequences that end with those stop codon will be directly equals to the number of stop codons.
# Use re.findall to pick out all the stop codon,
# then use len to count the total number of them.
# Use '|' to find all the stop codons at the same time and start finding from the index of the start codon.
count = len(re.findall(r'TAA|TAG|TGA', seq[s:]))
print(count)
