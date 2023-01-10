from LinkedList import LinkedList


class PIF:
    def __init__(self):
        self.__content = LinkedList()

    def add(self, posToken,  token, pos):
        self.__content.add((posToken, token, pos))

    def list(self):
        self.__content.list()

