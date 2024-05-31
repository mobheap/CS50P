while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        z = round((x / y) * 100)
        if z <= 1:
            print("E")
            break
        elif z >= 99:
            print("F")
            break
        else:
            print(f"{z}%")
            break
    except (ValueError, ZeroDivisionError):
        continue