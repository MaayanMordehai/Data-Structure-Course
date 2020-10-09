
class HashTableNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


def hash1(key):
    # just something simple for testing
    return key * 5


def hash2(key):
    # just something simple for testing
    return (key * 3) % 7


class HashTable:
    MAX_SIZE = 256

    def __init__(self, hash_func1=hash1, hash_func2=hash2):
        self._hash1 = hash_func1
        self._hash2 = hash_func2
        self._size = 0
        self._hash_table = [None for i in range(self.MAX_SIZE)]

    def get(self, key):
        hash1_result = self._hash1(key)
        hash2_result = self._hash2(key)
        for i in range(self.MAX_SIZE):
            index = (hash1_result + i * hash2_result) % self.MAX_SIZE
            if self._hash_table[index] is not None and self._hash_table[index].key == key:
                return self._hash_table[index].value
        return -1

    def set(self, key, value):
        inserted = False
        hash1_result = self._hash1(key)
        hash2_result = self._hash2(key)
        for i in range(self.MAX_SIZE):
            index = (hash1_result + i * hash2_result) % self.MAX_SIZE
            if self._hash_table[index] is None:
                inserted = True
                self._hash_table[index] = HashTableNode(key, value)
                self._size += 1
                break
            elif self._hash_table[index].key == key:
                inserted = True
                self._hash_table[index].value = value
                break
        if not inserted:
            print(f"table is full can't insert: {value}, or can't insert after {self.MAX_SIZE} tries of double hashing")

    def remove(self, key):
        removed = False
        hash1_result = self._hash1(key)
        hash2_result = self._hash2(key)
        for i in range(self.MAX_SIZE):
            index = (hash1_result + i * hash2_result) % self.MAX_SIZE
            if self._hash_table[index] is not None and self._hash_table[index].key == key:
                removed = True
                self._hash_table[index] = None
                self._size -= 1
                break
        if not removed:
            print(f"The given key is not exists in the hash table")

    @property
    def size(self):
        return self._size

    def max_size(self):
        return self.MAX_SIZE

    def display_full_table(self):
        for i in range(self.MAX_SIZE):
            if self._hash_table[i] is None:
                print(f"index {i} -> ")
            else:
                print(f"index {i} -> key {self._hash_table[i].key} value {self._hash_table[i].value}")

    def display_table(self):
        print_string = "{"
        for i in range(self.MAX_SIZE):
            if self._hash_table[i] is not None:
                print_string += f"{self._hash_table[i].key} : {self._hash_table[i].value}, "
        print_string = print_string[:-2] + "}"
        print(print_string)


def main():
    table = HashTable()
    table.set(1, "Maayan")
    table.set(2, "Shiraz")
    table.set(3, "Guy")
    table.set(4, "Roi")
    print("==================================================")
    print("double_hash: ")
    table.display_table()
    print(table.get(1))
    print(table.get(2))
    print(table.get(3))
    print(table.get(4))
    table.remove(1)
    print(table.get(1))
    table.display_table()
    print("==================================================")


if __name__ == "__main__":
    main()
