from Bio.Seq import translate

def which_genetic_code(DNA_sequence, protein_sequence):
    for i in range(1,16): # For each genetic table
        if translate(DNA_sequence, table = i, to_stop=True) == protein_sequence:
            return i 
