# handle csv

### 1 retrieve_manufactures.py
Write a script to connect to the following API ["https://swapi.dev/api/vehicles/"].
Retrieve the JSON data, and list the first 5 unique manufacturers.


### 2 generate_csv.py
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


### 3 normalize_csv.py
Write a function to normalize CSV files by converting a pipe-delimited file 
into a comma-delimited file.
Your original file will look like this:

    Planet|Manufacturer|Model|Type|Passengers
    Yavin|Ubrikkian" Industries|Sail Barge|sailbarge|500
    Bespin|Bespin Motors|Storm IV, Twin-Pod|repulsorcraft|0
    Kuat|Kuat Drive Yards|AT-ST|walker|0

When you run your script, the output should look like this:

    Planet,Manufacturer,Model,Type,Passengers
    Yavin,"Ubrikkian"" Industries",Sail Barge,sailbarge,500
    Bespin,Bespin Motors,"Storm IV, Twin-Pod",repulsorcraft,0
    Kuat,Kuat Drive Yards,AT-ST,walker,0

It's valid for a comma to be in your input data. You'll need to surround 
strings with commas in them with double quotes when writing your output file.

It's also valid for double quote characters to be in your input - you will 
need to double up quotes.

BONUS 1:
    Add in the ability to accept command line parameters for:
        the input delimiter to use ('|' should be the default)
        the quote character to use (" by default)

BONUS 2:
    Try to automatically detect the delimiter and quote character if they are 
    not supplied on the command line.
    If either the delimiter or the quote character are provided, assume the 
    other one is the default. But if both are missing, you should try to 
    automatically detect them.
    NOTE: This may not work for all files.
