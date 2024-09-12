from re import finditer
from Bio.Seq import translate
from Bio.Seq import reverse_complement

def proteins(sequence):
    # Return a list of protein that can be translated from an ORF of sequence (direct)
    proteins = []
    index_start_codons = [start_codon.start() for start_codon in finditer("ATG", sequence)]
    # for start_codon in index_start_codons:

    for start_codon in index_start_codons:
        # Adjust the sequence length (multiple of 3 needed)
        if len(sequence[start_codon:]) % 3 == 0: 
            sequence_adjusted = sequence
        elif (len(sequence[start_codon:]) + 1) % 3 == 0:
            sequence_adjusted = sequence + "N"
        elif (len(sequence[start_codon:]) + 2) % 3 == 0:
            sequence_adjusted = sequence + "NN"

        proteins.append(translate(sequence_adjusted[start_codon:], to_stop=True))

    return proteins

def longest_protein(sequence):
    # Return the longest protein that can be translated from an ORF of sequence (direct & reverse)
    longest_prot = proteins(sequence) + proteins(reverse_complement(sequence))
    return max(longest_prot, key=len)

