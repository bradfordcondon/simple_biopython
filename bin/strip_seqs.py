from Bio import SeqIO

import sys

def main(argv):

    input_file = argv[0]
    output_file = "test.fna"

    if argv[1]:
        output_file = argv[1]

    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
    write_empty(fasta_sequences, output_file)


def write_empty(fasta_sequences, output_file):
    """Given a SeQIO FASTA object and an output file name,
     write out the FASTA file with just the name, no sequences"""
    with open(output_file, "w") as out_file:
            for fasta in fasta_sequences:
                name, sequence = fasta.id, str(fasta.seq)
                new_sequence =  ''
                out_file.write('>' +name + '\n')


if __name__ == "__main__":
    main(sys.argv[1:])