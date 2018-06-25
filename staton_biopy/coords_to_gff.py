import sys
import csv


def convert_gff(argv):
    input_file = argv[0]
    parent = {}

    output_file = input_file + ".gff"
    with open(input_file, "r") as datafile:
        for line in datafile:
            parsed = parse_line(line)

            query_id = parsed["query_id"]
            reference_id = parsed["reference_id"]
            q_start = parsed["q_start"]
            q_end = parsed["q_end"]
            strand = parsed["strand"]

            reference_index = parent.get(reference_id)

            if !reference_index:
                parent[reference_id] = {query_id: {"start": q_start, "stop": q_stop}}

            else:
                query_index = reference_index.get(query_id)

                if !query_index:
                    parent[reference_id][query_id] = {"start": q_start, "stop": q_stop}

                else:
                    current = parent[reference_id][query_id]
                    prev_start = current["start"]
                    prev_end = current["end"]
                    if q_start < prev_start:
                        current["start"] = q_start
                    if q_end > prev_end:
                        current["end"] = prev_end


        datafile.seek(0)

        for line in datafile:
            parsed = parse_line(line)
            query_id = parsed["query_id"]
            reference_id = parsed["reference_id"]
            q_start = parsed["q_start"]
            q_end = parsed["q_end"]
            strand = parsed["strand"]





    """After going first time, loop through again and print out parent info"""

    attributes = "ID=" + reference_id + "; Name=" + reference_id + ";"
    print_out(query_id, print_start, print_end, print_strand, attributes)


def print_out(query_id, start, end, strand, attributes):
    final = "\t"
    print final.join([query_id, "nucmer",
                      "alignment", start,
                      end, ".",
                      strand, ".",
                      attributes

                      ])


def parse_line(line):
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
    print_strand = "+"
    print_start = q_start
    print_end = q_end

    if q_strand == "Minus":
        print_strand = "-"
        print_start = q_end
        print_end = q_start

    return {"query_id": query_id, "reference_id": reference_id, "q_start": print_start, "q_end": print_end, "strand": print_strand}

if __name__ == "__main__":
    convert_gff(sys.argv[1:])
