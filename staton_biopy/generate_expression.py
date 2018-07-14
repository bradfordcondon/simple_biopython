import sys
from faker import Faker
import random
from Bio import SeqIO
import xml.etree.cElementTree as ET


def create_expression(args):
    output_file = "expression.tsv"
    biomaterial_file = args[0]
    biomaterial_list = extract_biomats(biomaterial_file)
    biomaterial_n = len(biomaterial_list)

    ofh = open(output_file, "w")
    line = ""
    for name in biomaterial_list:
        line = line + "\t" + name  # first column should be empty so this is OK

    line = line + "\n"
    ofh.write(line)

    gene_FASTA = args[1]
    gene_list = extract_feature_names(gene_FASTA)
    print "generating output file\n"

    for name in gene_list:
        line = name
        count = 0
        while count < int(biomaterial_n):
            line = line + "\t" + str(random.randint(1, 501))
            count += 1

        line = line + "\n"
        ofh.write(line)


def extract_biomats(biomaterials):
    print "reading biomaterial file\n"
    names = []
    tree = ET.parse(biomaterials)
    root = tree.getroot()
    for child in root:
        names.append(child.attrib["accession"])

    return names


def extract_feature_names(fasta):
    print "reading FASTA file\n"
    names = []
    for record in SeqIO.parse(fasta, "fasta"):
        names.append(record.id)
    return names


if __name__ == "__main__":
    create_expression(sys.argv[1:])
