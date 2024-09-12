from Bio import SeqIO

def convert_fastq_to_fasta(fastq_file, fasta_file):
    g = open(fasta_file, "w")

    with open(fastq_file, "r") as fastq_file:
        fastq_dict = SeqIO.to_dict(SeqIO.parse(fastq_file, "fastq"))

        for sequence in fastq_dict.values():
            g.write(">" + sequence.id + "\n")
            g.write(str(sequence.seq) + "\n")

    g.close()
