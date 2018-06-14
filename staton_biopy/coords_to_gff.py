
import sys
import csv

def convert_gff(argv):
    input_file = argv[0]

    output_file = input_file + ".gff"
    with open(input_file, "r") as datafile:
        for line in datafile:

            split = line.split("\t")
            query_id = split[0]
            reference_id = split[5]
            q_start = split[6]
            q_end = split[7]
            r_start = split[8]
            r_end = split[9]
            p_id = split[10]
            p_sim = split[11]
            q_strand = split[17]

            attributes = "ID=" + query_id + ", Name=" + query_id + ";"

            final = "\t"
            print final.join([reference_id, "nucmer",
                              "alignment", r_start,
                              r_end,".",
                              q_strand, ".",
                              attributes

                              ])

            "GFF format:" \
            "0: seqid" \
            "1: source" \
            "2: type" \
            "3: start" \
            "4: end" \
            "5: score" \
            "6: strand" \
            "7: phase" \
            "8: attributes (tag=values)" \
            "9: feature id" \
            "10: name" \
            "alias" \
            "parent" \
            "target" \
            "gap" \
            "note" \
            "dbxref" \
            "ontology_term" \
            "is_circular" \
            ""

if __name__ == "__main__":
    convert_gff(sys.argv[1:])