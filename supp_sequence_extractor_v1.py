from Bio import SeqIO

def subset_fasta(fasta_file, ids_file, output_file):
    # Read the list of sequence IDs from the txt file
    with open(ids_file, 'r') as f:
        ids_to_keep = set(line.strip() for line in f)

    # Read the FASTA file and filter the records
    sequences = SeqIO.parse(fasta_file, "fasta")
    filtered_sequences = (seq for seq in sequences if seq.id in ids_to_keep)

    # Write the filtered sequences to a new FASTA file
    SeqIO.write(filtered_sequences, output_file, "fasta")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python subset_fasta.py <input_fasta> <ids_file> <output_fasta>")
        sys.exit(1)

    input_fasta = sys.argv[1]
    ids_file = sys.argv[2]
    output_fasta = sys.argv[3]

    subset_fasta(input_fasta, ids_file, output_fasta)
