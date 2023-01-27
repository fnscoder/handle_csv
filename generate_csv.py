"""
Create a script to generate a CSV file with random data.
Example output:
```
1234, randomstring
```
"""
import csv
import random
import string


with open('random_data.csv  ', mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(('id', 'random_string'))

    for i in range(random.randint(1, 100)):
        random_string = ''.join(random.choices(string.ascii_letters, k=random.randint(1, 100)))
        writer.writerow((random.randint(1000, 9999), random_string))
