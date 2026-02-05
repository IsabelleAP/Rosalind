from Bio import Entrez

def genbank_nucleotide(genus_name, date1, date2):
    Entrez.email = "isaa.alves2@gmail.com"
    term = '"{}"[Organism] AND ("{}"[Date] : "{}"[Date])'.format(genus_name, date1, date2)
    handle = Entrez.esearch(db='nucleotide', term=term)
    record = Entrez.read(handle)
    handle.close()
    return record['Count']

with open("rosalind_gbk.txt", "r") as f:
    linhas = [linha.strip() for linha in f.readlines()]
    genus_name = linhas[0]
    date1 = linhas[1]
    date2 = linhas[2]

print(genbank_nucleotide(genus_name, date1, date2))

