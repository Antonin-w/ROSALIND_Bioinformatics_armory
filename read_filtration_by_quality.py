from Bio import SeqIO
from math import floor

def number_reads_filtered(quality_threshold, percentage_bases, fastq_file):

    with open(fastq_file, "r") as fastq_file:
        fastq_list = list(SeqIO.parse(fastq_file, "fastq"))

    count_reads_filtered = 0

    for fastq in fastq_list:
        absolute_base = len(fastq.letter_annotations["phred_quality"]) / 100 * percentage_bases
        count_passed_threshold = len([x for x in fastq.letter_annotations["phred_quality"] if x >= quality_threshold])
        
        if count_passed_threshold > absolute_base:
            count_reads_filtered += 1 
    
    return count_reads_filtered
        