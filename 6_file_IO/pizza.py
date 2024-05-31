import sys
from tabulate import tabulate
import csv


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith('.csv'):
    print("Not a CSV file")
    sys.exit(1)

table = []

try:
    with open(sys.argv[1], 'r') as file:
        data = csv.reader(file)
        for line in data:
            table.append(line)            
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(table[1:], headers=table[0], tablefmt='grid'))