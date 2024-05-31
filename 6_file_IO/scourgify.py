import sys
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

try:
    with open(sys.argv[1], 'r') as file:
        data = csv.reader(file)            
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")