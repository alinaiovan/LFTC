import re

from ReadTokens import operators, separators


class Scanner:

    def getStringToken(self, line, index):
        token = ''
        tildes = 0
        while index < len(line) and tildes < 2:
            if line[index] == '~':
                tildes += 1
            token += line[index]
            index += 1

        return token, index

    def isPartOfOperator(self, char):
        for op in operators:
            if char in op:
                return True
        return False

    def getOperatorToken(self, line, index):
        token = ''

        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def tokenize(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.isPartOfOperator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.getOperatorToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] == '~':
                if token:
                    tokens.append(token)
                token, index = self.getStringToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] in separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def isIdentifier(self, token):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|\d)*$', token) is not None

    def isConstant(self, token):
        return re.match(r'^(0|[+-]?[1-9]\d*)$|^~.*~$', token) is not None

    def isString(selfself, token):
        return re.match(r'^~.*~$', token) is not None