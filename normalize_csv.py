"""
takes two parameters:
input_file: The path to the input file, a pipe-delimited CSV file.
output_file: The path to the output file, a comma-delimited CSV file.
The function opens the input file, reads it line by line, and writes the output file line by line, replacing the pipe
separator with a comma, and surrounding any fields that contain a comma with double quotes.
It also replaces any double quotes in the input fields with two double quotes, which is the correct way to escape
double quotes in a CSV file.

BONUS 1:
    Add in the ability to accept command line parameters for:
        the input delimiter to use ('|' should be the default)
        the quote character to use (" by default)
"""
import argparse
import csv
import sys


def normalize_csv(input_file, output_file, delimiter, quotechar):
    with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
        reader = csv.reader(input_csv, delimiter=delimiter)
        writer = csv.writer(output_csv, delimiter=',', quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            writer.writerow(row)


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    parser.add_argument('--delimiter', type=str, default='|')
    parser.add_argument('--quotechar', type=str, default='"')
    args = parser.parse_args(args)

    normalize_csv(args.input_file, args.output_file, args.delimiter, args.quotechar)


if __name__ == '__main__':
    main(sys.argv[1:])
