# Complementing a strand of DNA

import pandas as pd

dna_string = input((" "))

def dna_complementar(seq):
    complementar = ""
    for nucleotideo in seq:
        if nucleotideo == "A":
            complementar += "T"
        elif nucleotideo == "T":
            complementar += "A"
        elif nucleotideo == "G":
            complementar += "C"
        else:
            complementar += "G"
    return complementar

complementar = dna_complementar(dna_string)

complementar_reversa = complementar[::-1]

complementar_reversa