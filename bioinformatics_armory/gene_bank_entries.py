from Bio import Entrez

Entrez.email = "havetoputyouremail@gmail.com"

def how_many_entries(genus_name, mindate, maxdate):

    term = genus_name + "[Organism]"
    request = Entrez.esearch(db="nucleotide", term=term, mindate=mindate, maxdate=maxdate, datetype="pdat")
    record = Entrez.read(request)
    return record["Count"]



