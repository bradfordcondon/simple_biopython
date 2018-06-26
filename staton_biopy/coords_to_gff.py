import sys
import csv
import pprint


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

            if reference_index is None:
                parent[reference_id] = {
                    query_id: {"start": q_start, "end": q_end, "strand": strand, "sections": [line]}}

            else:
                query_index = reference_index.get(query_id)

                if query_index is None:
                    parent[reference_id][query_id] = {"start": q_start, "end": q_end, "strand": strand,
                                                      "sections": [line]}

                else:
                    current = parent[reference_id][query_id]
                    prev_start = current["start"]
                    prev_end = current["end"]
                    sections = current["sections"]
                    if q_start < prev_start:
                        current["start"] = q_start
                    if q_end > prev_end:
                        current["end"] = prev_end
                    sections.append(line)
                    parent[reference_id][query_id] = {"start": q_start, "end": q_end, "strand": strand,
                                                      "sections": sections}

    for parent_id, query_package in parent.items():
        for query_id, record in query_package.items():
            parent_start = record["start"]
            parent_end = record["end"]
            strand = record["strand"]
            attributes = "ID=" + parent_id + "; Name=" + parent_id + ";"
            print_out(query_id, parent_start, parent_end, strand, attributes)
            count = 1

            sections = record["sections"]

            for section in sections:
                parsed = parse_line(section)
                query_id = parsed["query_id"]
                reference_id = parsed["reference_id"]
                q_start = parsed["q_start"]
                q_end = parsed["q_end"]
                strand = parsed["strand"]

                attributes = "Parent=" + reference_id + "; ID=" + reference_id + "_" + str(
                    count) + "; Name=" + reference_id + "_" + str(count) + ";"

                print_out(query_id, q_start, q_end, strand, attributes)

                count += 1


def print_out(query_id, start, end, strand, attributes):
    final = "\t"
    type = "scaffold"

    if attributes.find("Parent=") != -1:
        type = "alignment"

    print final.join([query_id, "nucmer",
                      type, start,
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

    return {"query_id": query_id, "reference_id": reference_id, "q_start": print_start, "q_end": print_end,
            "strand": print_strand}


if __name__ == "__main__":
    convert_gff(sys.argv[1:])
