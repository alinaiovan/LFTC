from LinkedList import LinkedList


class PIF:
    def __init__(self):
        self.__content = LinkedList()

    def add(self,token ,posToken, pos):
        self.__content.add((token, posToken , pos))

    def __str__(self):
        return str(self.__content)

