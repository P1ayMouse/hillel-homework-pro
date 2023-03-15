class HashTable:
    def __init__(self):
        self.base = 100
        self.container = [None] * self.base

    def get_hash(self, value: int) -> int:
        return value % self.base

    def add_value(self, value):
        v_hash = self.get_hash(value)

        if self.container[v_hash] is None:
            self.container[v_hash] = [value]

        else:
            self.container[v_hash].append(value)


if __name__ == '__main__':
    hashtable = HashTable()
    hashtable.add_value(35)
    hashtable.add_value(678)
    hashtable.add_value(43)
    hashtable.add_value(231)
    hashtable.add_value(31)
    hashtable.add_value(131)
    hashtable.add_value(46)
    print(hashtable.get_hash(231))
    print(hashtable.container)


