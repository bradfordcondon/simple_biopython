from Bio import SeqIO
import sys, getopt, math, re, pprint


def main(argv):
    usage = 'concat_duplicates.py <input file>'

    try:
        input_file = argv[0]
    except IOError:
        print usage
        sys.exit()

    # open file
    file = open(input_file, 'r').read()

    output_file = "concatenated.fasta"

    ofh = open(output_file, "w")

    names = {}
    duplicate_names = {}
    duplicate_seqs = {}

    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        if name in names:
            duplicate_names[name] = name
        else:
            names[name] = name

    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
    if name in duplicate_names:
        new_seq = sequence
        if name in duplicate_seqs:
            new_seq = duplicate_seqs[name]
            #remove * from sequence
            length = len(new_seq)
            new_seq = new_seq[1:length]
            new_seq = new_seq + sequence
        duplicate_seqs[name] = new_seq
    else:
        ofh.write('>' + name + '\n' + sequence + '\n')

    for name, sequence in duplicate_seqs.items():
        ofh.write('>' + name + '\n' + sequence + '\n')

    ofh.close()


if __name__ == "__main__":
    main(sys.argv[1:])

    """"
   Concatenate duplicate FASTA records into a single record.
    """
