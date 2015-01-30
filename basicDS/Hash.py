__author__ = 'andy'

class HashTable_my:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, str):
        return str%self.size
        sum = 0
        for pos in range(len(str)):
            sum += ord(str[pos])
        return sum%self.size

    def rehash(self, old_hash, size):
        return (old_hash+1)%size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
               self.data[hashvalue] == data
            else:
                next_slot = self.rehash(hashvalue, len(self.slots))
                while(None!=self.slots[hashvalue] and \
                        self.slots[next_slot] != key):
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        hashvalue = self.hashfunction(key)
        while(self.slots[hashvalue] != None and self.slots[hashvalue] != key):
            hashvalue = self.rehash(hashvalue, self.size)
        if(self.slots[hashvalue] == key):
            return self.data[hashvalue]
        else:
            return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

def test():
    h = HashTable_my()
    h[54] = "cat"
    h[26] = "dog"
    h[93] = "lion"
    h[17] = "tiger"
    print(h.slots)
    print(h.data)

test()


'''
practise doing something
2
3
4
5
6
76

'''