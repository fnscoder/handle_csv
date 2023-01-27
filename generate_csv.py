"""
Create a script to generate a CSV file with random data.
Example output:
```
1234, randomstring
```

Add the ability to pass in command line parameters. Use an argument to pass
in the number of rows to generate.
Add another argument for the filename to use for the CSV file.

Usage: $ python generate_csv.py 5 test.csv
It will generate a CSV file called test.csv with 5 rows

If you had to generate a large number of rows (millions or more), is there
anything you would do differently to handle this?
Modify your script to handle this requirement.

Changed to use a generator to generate the rows, this way we will not load all the rows in memory at the same time.
The rows will be generated one by one.
"""
import argparse
import csv
import random
import string


def generate_rows(num_rows):
    for i in range(num_rows):
        random_string = ''.join(random.choices(string.ascii_letters, k=random.randint(1, 100)))
        yield (random.randint(1000, 9999), random_string)


parser = argparse.ArgumentParser()
parser.add_argument('num_rows', type=int, help='Number of rows to generate')
parser.add_argument('filename', type=str, help='Name of the CSV file to generate')

args = parser.parse_args()

with open(args.filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(('id', 'random_string'))
    writer.writerows(generate_rows(args.num_rows))
