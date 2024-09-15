from Bio import SeqIO

def count_reverse_complements(fasta_file):
    count_match_reverse = 0 

    with open(fasta_file, "r") as fasta_file:
        list_fasta = list(SeqIO.parse(fasta_file, "fasta"))

    for sequence in list_fasta:
        if sequence.seq == sequence.seq.reverse_complement():
            count_match_reverse += 1 

    return count_match_reverse


