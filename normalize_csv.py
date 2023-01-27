"""
takes two parameters:
input_file: The path to the input file, a pipe-delimited CSV file.
output_file: The path to the output file, a comma-delimited CSV file.
The function opens the input file, reads it line by line, and writes the output file line by line, replacing the pipe
separator with a comma, and surrounding any fields that contain a comma with double quotes.
It also replaces any double quotes in the input fields with two double quotes, which is the correct way to escape
double quotes in a CSV file.
"""
import csv


def normalize_csv(input_file, output_file):
    with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
        reader = csv.reader(input_csv, delimiter='|')
        writer = csv.writer(output_csv)

        for row in reader:
            for i in range(len(row)):
                if ',' in row[i]:
                    row[i] = f'"{row[i]}"'
                elif '"' in row[i]:
                    row[i] = row[i].replace('"', '""')
            writer.writerow(row)


normalize_csv('pipes.csv', 'pipes_normalized.csv')
