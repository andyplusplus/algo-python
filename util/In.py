__author__ = 'andy'

import re

class In:
    Inpath="D:/z_books/dataStructure/Algorithms_4e_RobertSedgewick/algs4-data/"
    def __init__(self, fileName, delim=" "):
        fileName = self.Inpath + fileName
        infile = open(fileName, 'r')
        str = infile.read()
        self.lines = str.splitlines()
        self.items = None
        self.__i = 0
        self.__split2Items(delim)

    def reset(self):
        self.__i = 0

    def __split2Items(self, delim):
        if(not self.items):
            self.items = []
            for line in self.lines:
                if delim == " ":
                    a = re.split(r"\s+", line)
                else:
                    a = re.split(delim+"+", line)
                if "" in a: a.remove("")
                self.items.extend(a)

    def readint(self):
        return int(self.readString())

    def readString(self):
        if self.__i < len(self.items):
            value = self.items[self.__i]
            self.__i += 1
            return value

    def readLine(self):
        if(self.__i < len(self.lines)):
            value = self.lines[self.__i]
            self.__i += 1
            return value

def test():
    iin = In("tinyCG.txt")
    print(iin.items)

if __name__ == '__main__':
    test()