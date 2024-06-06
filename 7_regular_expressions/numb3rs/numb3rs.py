import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = re.compile(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$')
    match = pattern.match(ip)
    if not match:
        return False
    
    segments = match.groups()
    for segment in segments:
        if not 0 <= int(segment) <= 255:
            return False
    
    return True

if __name__ == "__main__":
    main()