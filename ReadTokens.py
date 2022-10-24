reservedWords = []
separators = []
operators = []


def readFile():
    with open('token.in', 'r') as f:
        for i in range(5):
            operators.append(f.readline().strip())
        for i in range(13):
            separator = f.readline().strip()
            if separator == "space":
                separator = " "
            separators.append(separator)
        for i in range(17):
            reservedWords.append(f.readline().strip())