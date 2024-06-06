import sys
import csv

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith('.csv') or not sys.argv[2].endswith('.csv'):
    print("Not a CSV file")
    sys.exit(1)

output = []
try:
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            name = line['name'].split(',')
            output.append({'first': name[1].strip(), 'last': name[0].strip(), 'house': line['house']})
except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}")
    sys.exit(1)

try:
    with open(sys.argv[2], 'w', newline='') as file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for line in output:
            writer.writerow(line)
except Exception as e:
    print(f"Could not write to {sys.argv[2]}: {e}")
    sys.exit(1)