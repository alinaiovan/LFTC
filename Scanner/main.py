from HashTable import HashTable
from PIF import PIF
from ReadTokens import readFile, reservedWords, allReservedSepOp
from Scanner import *


class Main:

    def __init__(self):
        self.stIdentifier = HashTable(17)
        self.stConstants = HashTable(17)
        self.pif = PIF()
        self.scanner = Scanner()

    def run(self):
        readFile()
        fileName = "p1.txt"
        exceptionMessage = ""

        with open(fileName, 'r') as file:
            lineCounter = 0
            for line in file:
                lineCounter += 1
                tokens = self.scanner.tokenize(line.strip())
                for i in range(len(tokens)):
                    if tokens[i] in reservedWords + separators + operators:
                        if tokens[i] == ' ':
                            continue
                        self.pif.add(tokens[i], allReservedSepOp.index(tokens[i]),  -1)
                    elif self.scanner.isIdentifier(tokens[i]):
                        id = self.stIdentifier.add(tokens[i])
                        self.pif.add(tokens[i], allReservedSepOp.index("id"), id)
                    elif self.scanner.isConstant(tokens[i]):
                        const = self.stConstants.add(tokens[i])
                        self.pif.add(tokens[i], allReservedSepOp.index("const"), const)
                    else:
                        exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            lineCounter) + "\n"

        if exceptionMessage == '':
            print("Lexically correct\n")
            print("Constants: \n", self.stConstants)
            print("Identifiers: \n", self.stIdentifier)
            print("PIF: \n")
            self.pif.list()
        else:
            print(exceptionMessage)


main = Main()
main.run()
