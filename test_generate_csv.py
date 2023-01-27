import csv
import os
import subprocess
import unittest


class TestGenerateCSV(unittest.TestCase):

    def setUp(self):
        self.ten_rows = '10'
        self.filename = 'testing.csv'

    def test_generate_csv_cli(self):
        """Test that the script can handle a valid number of rows and filename"""
        result = subprocess.run(['python', 'generate_csv.py', self.ten_rows, self.filename], capture_output=True)
        assert result.returncode == 0
        self.assertTrue(os.path.exists(self.filename))
        os.remove(self.filename)

    def test_generate_csv(self):
        """Test generating 10 rows of data"""
        subprocess.run(['python', 'generate_csv.py', self.ten_rows, self.filename], capture_output=True)

        with open(self.filename, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), int(self.ten_rows) + 1)

        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['id', 'random_string'])
            for i, row in enumerate(reader):
                self.assertEqual(len(row), 2)
                self.assertTrue(row[0].isdigit())
                self.assertTrue(1000 <= int(row[0]) <= 9999)
                self.assertTrue(row[1].isalpha())
                self.assertTrue(1 <= len(row[1]) <= 100)

        os.remove(self.filename)

    def test_generate_csv_invalid_num_rows(self):
        """Test that the script can handle an invalid number of rows"""
        num_rows = '-1'
        result = subprocess.run(['python', 'generate_csv.py', num_rows, self.filename], capture_output=True)
        assert 'argument num_rows must be a positive integer' in result.stderr.decode()

    def test_generate_csv_no_args(self):
        """Test that the script can handle when the user does not pass any argument"""
        result = subprocess.run(['python', 'generate_csv.py'], capture_output=True)
        assert result.returncode == 2
        assert 'the following arguments are required: num_rows, filename' in result.stderr.decode()

    def test_generate_csv_large_file(self):
        """Test generating 1000000 rows of data"""
        num_rows = '1_000_000'
        subprocess.run(['python', 'generate_csv.py', num_rows, self.filename], capture_output=True)

        self.assertTrue(os.path.exists(self.filename))
        # Check that the file was created

        with open(self.filename, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), int(num_rows) + 1)

        os.remove(self.filename)


if __name__ == '__main__':
    unittest.main()
