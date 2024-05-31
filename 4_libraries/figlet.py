import sys; from pyfiglet import Figlet

figlet = Figlet()
availablefonts = figlet.getFonts()

try:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in availablefonts:
        f = sys.argv[2]
        figlet.setFont(font=f)
        z = input("Input: ")
        print(figlet.renderText(z))
    else:
        sys.exit(1)
except IndexError:
    z = input("Input: ")
    print(figlet.renderText(z))
except:
    sys.exit(1)