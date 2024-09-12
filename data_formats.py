from Bio import Entrez
from Bio import SeqIO

Entrez.email = "havetoputyouremail@gmail.com"

def shortest_fasta(IDs):
    IDs = ','.join(IDs.split()) # Convert to fit Entrez.efetch format
    request = Entrez.efetch(db="nucleotide", id=[IDs], rettype="fasta")
    records = list(SeqIO.parse(request, "fasta"))
    
    length_fasta = [len(sequence.seq) for sequence in records]
    shortest_fasta_index = length_fasta.index(min(length_fasta))

    print(">" + records[shortest_fasta_index].description + "\n" + records[shortest_fasta_index].seq)
