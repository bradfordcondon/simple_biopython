from Bio import SeqIO

import sys

input_file = sys.argv[1]
output_file = "test.fna"

fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
with open(output_file, "w") as out_file:
    #  In python the with keyword is used when working with unmanaged resources (like file streams).
    #  It is similar to the using statement in VB.NET and C#. It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown. It provides 'syntactic sugar' for try/finally blocks.
        for fasta in fasta_sequences:
            name, sequence = fasta.id, str(fasta.seq)
            new_sequence =  ''
            out_file.write('>' +name + '\n')

