from Bio.Seq import Seq

def DNA_stats(dna):
    seq = Seq(dna)
    stats = {}
    
    for i in "ACGT":
        stats[i] = seq.count(i)
    
    res = ' '.join(str(val) for key, val in stats.items())

    return res
