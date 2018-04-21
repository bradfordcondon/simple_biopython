from Bio import SeqIO
import sys, getopt, math


def main(argv):
    usage = 'split_fasta.py -i <input file> -n <number of output files>'
    input_file = ''
    out_count = 1
    try:
        opts, args = getopt.getopt(argv, "hi:n:", ["ifile="])
        # all of the tutorials use getOptError but mine was out of date!
    except getopt.error:
        print usage
        sys.exit(2)

    for opt, arg, in opts:
        if opt == '-h':
            print usage
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt == "-n":
            out_count = int(arg)

    # open file
    file = open(input_file, 'r').read()

    total_count = file.count(">")

    # file.close()

    bite_size = math.ceil(total_count / out_count)

    print(str(total_count) + " input sequences.  Generating " + str(int(bite_size)) + " output files" )

    placeholder = 1
    output_file = input_file + "." + str(placeholder)

    ofh = open(output_file, "w")

    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
    for fasta in fasta_sequences:
        # check if we need a new output file.
        if placeholder % 10000 == 0 :
            print "Processing sequence " + str(placeholder)
        if placeholder % bite_size == 0:
            ofh.close()
            output_file = input_file + "." + str(int(placeholder / bite_size))
            ofh = open(output_file, "w")
        name, sequence = fasta.id, str(fasta.seq)
        ofh.write('>' + name + '\n' + sequence + '\n')
        placeholder += 1
    ofh.close()

if __name__ == "__main__":
    main(sys.argv[1:])
