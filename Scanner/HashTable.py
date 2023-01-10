class HashTable:

    def __init__(self, size):
        self.__items = [[] for _ in range(size)]
        self.__size = size

    def hash(self, key):
        new_pos = 0
        for character in key:
            new_pos += ord(character) - ord('0')
        return new_pos % self.__size

    def contains(self, key):
        return key in self.__items[self.hash(key)]

    def remove(self, key):
        self.__items[self.hash(key)].remove(key)

    def __str__(self) -> str:
        result = ""
        for i in range(self.__size):
            result = result + str(i) + "-" + str(self.__items[i]) + "\n"
        return result

    def add(self, key):
        if self.contains(key):
            return self.getPos(key)
        self.__items[self.hash(key)].append(key)
        return self.getPos(key)

    def getPos(self, key):
        pos = self.hash(key)
        list_index = 0
        for item in self.__items[pos]:
            if item != key:
                list_index += 1
            else:
                break
        return pos, list_index
