from Bio import SeqIO
from statistics import mean

def count_position_low_quality(fastq_file, quality_threshold):
    
    with open(fastq_file, "r") as fastq_file:
        fastq_list = list(SeqIO.parse(fastq_file, "fastq"))

    list_quality_score = []

    # Merge quality score in one list
    for fastq in fastq_list:
        list_quality_score.append(fastq.letter_annotations["phred_quality"])
    
    # Calculate mean and check if below threshold or not
    mean_quality = [sum(score) / len(score) for score in zip(*list_quality_score)]

    count_position_below_threshold = 0

    for x in mean_quality: 
        count_position_below_threshold += 1 if x < quality_threshold else 0

    return count_position_below_threshold








