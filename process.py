import pysam as sam
import re
# 读取fasta
fasta = sam.FastaFile('data.fasta')

id = fasta.references
length = fasta.lengths
flag = 0
for i in id:
    data = fasta.fetch(i, 0, length[flag])
    flag += 1
    data_final = re.sub('[\d]','',data)
    with open('my_data.txt','a') as f:
        f.write('>')
        f.write(i)
        f.write('\n')
        f.write(data_final)
        f.write('\n')