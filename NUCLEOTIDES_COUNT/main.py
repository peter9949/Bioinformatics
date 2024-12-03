from DNAToolKit import *
import random

# Creating a random DNA sequence for testing
RandDNASeq = ''.join([random.choice(Nucleotides)
                for nuc in range(50)])

DNAVal = seqcheck(RandDNASeq)
print(DNAVal)
print(basecount(DNAVal))
