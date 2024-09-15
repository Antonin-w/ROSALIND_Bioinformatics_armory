from Bio import SeqIO
from statistics import mean

def number_reads_below_threshold(quality_threshold, fastq_file):

    with open(fastq_file, "r") as fastq_file:
        fastq_dict = list(SeqIO.parse(fastq_file, "fastq"))

    read_below_threshold = 0

    for fastq in fastq_dict:
        if mean(fastq.letter_annotations["phred_quality"]) < quality_threshold:
            read_below_threshold += 1 

    return read_below_threshold
