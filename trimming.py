from Bio import SeqIO
from Bio.Seq import Seq

def trimming(fastq_file, quality_cutoff):

    with open(fastq_file, "r") as fastq_file:
        fastq_list = list(SeqIO.parse(fastq_file, "fastq"))
    
    for fastq in fastq_list:
        start_index = 0 
        stop_index = len(fastq.seq)
        base = 0 

        while fastq.letter_annotations["phred_quality"][base] < quality_cutoff:
            start_index += 1
            base += 1 
        
        base = len(fastq.seq)-1
        while fastq.letter_annotations["phred_quality"][base] < quality_cutoff:
            stop_index -= 1 
            base -= 1 

        phred_qual = fastq[start_index:stop_index].letter_annotations["phred_quality"]
        fastq.letter_annotations = {}

        fastq.seq = Seq(fastq[start_index:stop_index].seq)
        fastq.letter_annotations["phred_quality"] = phred_qual

    return fastq_list


def write_fastq_trimmed(trimmed_fastq, fastq_output):
    with open(fastq_output, "w") as output:
        SeqIO.write(trimmed_fastq, output, "fastq")
