from Bio import SeqIO
import sys, getopt, math, re
from BCBio.GFF import GFFExaminer
from os import path
import pprint
from BCBio import GFF
import csv


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

    print ("opening " + mrna_path)

    fasta_sequences = SeqIO.parse(open(mrna_path), 'fasta')
    for fasta in fasta_sequences:
        if count < n:
            name, sequence = fasta.id, str(fasta.seq)
            ofh.write('>' + name + '\n' + sequence + '\n')
            count += 1
            selected_mrna.append(name)
    ofh.close()

    simple_gff_trimmer(gff_path, selected_mrna)


def simple_gff_trimmer(gff_path, selected_mrna):
    with open(gff_path, 'rb') as tsvin, open('new.csv', 'wb') as csvout:
        tsvin = csv.reader(tsvin, delimiter='\t')
        csvout = csv.writer(csvout)
        write = False

        for row in tsvin:
            if len(row) > 1:
                contig = row[0]
                type = row[3]
                info = row[-1]
                if type == 'mRNA':
                    write = False
                    info_split = info.split(';')
                    id = info_split[0]
                    if 'ID=' + id in selected_mrna:
                        write = True
                        csvout.write(row)
                else:
                    if write:
                        csvout.write(row)


if __name__ == "__main__":
    main(sys.argv[1:])

    """
    Take a mrna and GFF file.  
    Pick N mRNA at random and trim everything down to that.

    """

"""
This function didnt quite work out for me.  It should read in a GFF file, cross ref to the included mRNA, and print the matching child/parents
"""


def failed_GFF_Trimmer(gff_path, selected_mrna):
    examiner = GFFExaminer()
    in_handle = open(gff_path)
    out_handle = open("out.gff", "w")

    selected_parents = {}

    for parent in GFF.parse(in_handle):
        for child in parent.features:
            for child_two in child.sub_features:
                if child_two.type == 'mRNA':
                    if child_two.id in selected_mrna:
                        selected_parents[parent.id] = parent

    for parent in selected_parents:
        item = selected_parents[parent]
        print(item)
        GFF.write(item, out_handle)
