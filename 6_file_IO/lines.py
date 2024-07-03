import sys

complexity = 0

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not sys.argv[1].endswith('.py'):
    print("Not a Python file")
    sys.exit(1)

try:
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

for line in lines:
    if line.isspace():
        pass
    elif line.lstrip().startswith('#'):
        pass
    else:
        complexity += 1

print(complexity)