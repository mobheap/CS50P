def main():
    result = convert(input())
    print(result)


def convert(userinput):
    userinput = userinput.replace(":)" , "🙂")
    userinput = userinput.replace(":(" , "🙁")
    return userinput


main()