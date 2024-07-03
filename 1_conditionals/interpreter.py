calc = input("Expression: ")
x , y , z = calc.split(" ")
x = float(x)
z = float(z)
if y == "+":
    result = round(x + z,1)
elif y == "-":
    result = round(x - z,1)
elif y == "*":
    result = round(x * z,1)
elif y == "/":
    result = round(x / z,1)
print(result)