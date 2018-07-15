from Bio import SeqIO
import sys, getopt, math, re
from BCBio.GFF import GFFExaminer
from os import path
import pprint


def main(argv):
    usage = 'split_fasta.py [n] [mrna FASTA] [polypeptide FASTA] [GFF]'
    out_count = 1
    if len(argv) < 4:
        print usage
        sys.exit()
    n = argv[0]
    mrna = argv[1]
    polyp = argv[2]
    gff = argv[3]
    selected_mrna = []

    mrna_path = path.relpath(mrna)
    polyp_path = path.relpath(polyp)
    gff_path = path.relpath(gff)

    ofh = open("mrna_mini.fasta", "w")
    count = 0

    fasta_sequences = SeqIO.parse(open(mrna_path), 'fasta')
    for fasta in fasta_sequences:
        if count < n:
            name, sequence = fasta.id, str(fasta.seq)
            ofh.write('>' + name + '\n' + sequence + '\n')
            count += 1
            selected_mrna.append(name)
    ofh.close()

    print ("opening " + mrna_path)

    examiner = GFFExaminer()
    in_handle = open(gff_path)

    pprint.pprint(examiner.parent_child_map(in_handle))


if __name__ == "__main__":
    main(sys.argv[1:])

    """
    Take a mrna, polypeptide, and GFF file.  
    Pick N mRNA at random and trim everything down to that.

    """
