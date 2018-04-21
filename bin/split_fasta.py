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

    print(bite_size)

    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')

if __name__ == "__main__":
    main(sys.argv[1:])
