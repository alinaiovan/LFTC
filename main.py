from HashTable import HashTable
from ReadTokens import readFile, reservedWords
from Scanner import *


class Main:

    def __init__(self):
        self.stIdentifier = HashTable(17)
        self.stConstants = HashTable(17)
        self.scanner = Scanner()

    def run(self):
        readFile()
        fileName = "p.txt"
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
                    elif self.scanner.isIdentifier(tokens[i]):
                        self.stIdentifier.add(tokens[i])
                    elif self.scanner.isConstant(tokens[i]):
                        self.stConstants.add(tokens[i])
                    else:
                        exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            lineCounter) + "\n"


        if exceptionMessage == '':
            print("Lexically correct\n")
            print("Constants: \n", self.stConstants)
            print("Identifiers: \n", self.stIdentifier)
        else:
            print(exceptionMessage)


main = Main()
main.run()
