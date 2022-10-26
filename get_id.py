import pysam as sam

fasta = sam.FastaFile('data.fasta')
id = fasta.references
for i in id:
    with open('ID.txt', 'a') as file:
        file.write(i)
        file.write('\n')