reservedWords = []
separators = []
operators = []

allReservedSepOp = ['const', 'id']


def readFile():
    with open('token.in', 'r') as f:
        for i in range(5):
            char = f.readline().strip()
            operators.append(char)
            allReservedSepOp.append(char)
        for i in range(13):
            char = f.readline().strip()
            if char == "space":
                char = " "
            separators.append(char)
            allReservedSepOp.append(char)
        for i in range(17):
            char = f.readline().strip()
            reservedWords.append(char)
            allReservedSepOp.append(char)
