def dna_coding(sequence):
    # Convert sequence to uppercase
    sequence = sequence.upper()

    # Find the indices of the start and stop codons
    start_index = sequence.find('ATG')
    stop_index = sequence.find('TGA')

    # Calculate the length of the sequence
    seq_len = len(sequence)

    # Calculate the distance between the start and stop codons
    if start_index == -1 or stop_index == -1:
        coding_len = 0
    else:
        coding_len = stop_index - start_index + 3

    # Calculate the percentage of the sequence that is coding
    coding_percent = (coding_len / seq_len) * 100

    # Determine whether the sequence is protein-coding, non-coding, or unclear
    if coding_percent > 50:
        return coding_percent, 'protein-coding'
    elif coding_percent < 10:
        return coding_percent, 'non-coding'
    else:
        return coding_percent, 'unclear'


# Example
dna_sequence = input("Please input a DNA sequence here:")
percent, label = dna_coding(dna_sequence)
print(f'The DNA sequence is {percent:.2f}% coding and should be labeled as {label}.')
