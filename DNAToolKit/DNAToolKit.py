Nucleotides = ['A','T','C','G']

# Check the seqence to be sure it is a DNA string

def dna_seq_check(dnaseq):
    tmpseq = dnaseq.upper()
    for base in tmpseq:
        if base not in Nucleotides:
            return False
        
    return tmpseq

# Return the counts of bases in DNA sequence

def nucleotides_count(dnaseq):
    count_of_base = {"A":0, "C": 0, "G":0, "T": 0}
    for base in dnaseq:
            count_of_base[base] += 1

    return count_of_base

# Convert DNA string to RNA string

def dna_to_rna(dnaseq):
    for base in dnaseq:
        if base == "T":
              tmpseq = dnaseq.replace("T","U")

    return tmpseq

# Return complementary strand of DNA string

def reverse_dna_complementary(dnaseq):
    # Create a translation table for complementary bases
    complement = str.maketrans("ATCG", "TAGC")
    
    # Reverse the sequence and translate it to its complement
    reverse_seq_comp = dnaseq[::-1].translate(complement)
    
    return reverse_seq_comp