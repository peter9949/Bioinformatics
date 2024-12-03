Nucleotides = ['A','T','C','G']

# Check the seqence to be sure it is a DNA string

def seqcheck(dnaseq):
    tmpseq = dnaseq.upper()
    for base in tmpseq:
        if base not in Nucleotides:
            return False
    return tmpseq

# Return the counts of bases in the passed DNA sequence

def basecount(dnaseq):
    count_of_base = {"A":0, "C": 0, "G":0, "T": 0}
    for base in dnaseq:
            count_of_base[base] += 1
    return count_of_base

