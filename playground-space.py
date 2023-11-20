
def dna_to_rna(dna):
    if dna == '': # if the DNA sequence is empty, return an empty string
        return dna
    else:
        rna = dna.replace('T', 'U')
        return rna # return the RNA sequence instead of printing it
  
    
dna_sequence = 'AGTTCTTAAT' # DNA sequence
rna_sequence = dna_to_rna(dna_sequence) # RNA sequence
print(f'"{dna_sequence}" => "{rna_sequence}"')

# optimized code
def dna_to_rna(dna):
    # Check if the DNA sequence is non-empty
    if dna: # if dna does not equal ''
        return dna.replace('T', 'U')
    else:
        # Return the empty string directly becuase dna is empty
        return dna

# Example usage
dna_sequence = 'AGTTCTTAAT'  # DNA sequence
rna_sequence = dna_to_rna(dna_sequence)  # RNA sequence
print(f'"{dna_sequence}" => "{rna_sequence}"')



