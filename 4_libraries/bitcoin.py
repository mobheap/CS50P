import requests; import sys

while True:
    try:
        n = float(sys.argv[1])
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = r.json()
        price = n * (data["bpi"]["USD"]["rate_float"])
        print(f"${price:,.4f}")
        break
        
    except IndexError:
        print("Missing command-line argument")
        sys.exit(1)
        
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
        
    except requests.RequestException:
        sys.exit(1)