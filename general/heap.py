import random


class MaxHeap:
    """ Maximum Heap """

    def __init__(self, values=None):
        """ Constructor - initialize heap by list of values"""
        if values is None:
            values = []
        self.heap = []
        for val in values:
            self.heap.append(val)
        self.size = len(values)
        for index in range(self.size, 0, -1):
            heapify(self.heap, self.size, index)

    def maximum(self):
        """
        This function is getting the maximum value in the heap
        This is O(1)
        :return: The maximum value of the heap
        """
        if self.size > 0:
            return self.heap[0]
        raise Exception("heap is not initialized")

    def extract_max(self):
        """
        This function is removing the maximum from the list and returning it
        building the heap by moving the last leaf value to the head and doing heapify
        because moving the last leaf we know that both sides are good and the only thing that might not be is the root
        so doing heapify to it will order the entire heap
        O(log(n))
        :return: The maximum value of the heap that we just removed
        """
        max_value = self.maximum()
        self.heap = [self.heap[-1]] + self.heap[1:-1]
        self.size -= 1
        heapify(self.heap, self.size, 1)
        return max_value

    def insert(self, value):
        """
        Insert value to heap
        This is O(log(n))
        :param value: the value to add to heap
        """
        self.heap.append(value)
        self.size += 1
        # going over with heapify on the parts of the tree that changed / might change
        index = int(self.size / 2)
        while index != 0:
            heapify(self.heap, self.size, index)
            index = int(index / 2)


def heapify(lst, size, place, d=False):
    """
    This function is ordering some place in the tree to fit the heap
    The heap list is starting from 0 but places are user friendly - root is 1
    This is O(log(n))
    :param place: the place in the heap that has a leaf that needs to be ordered
    """
    # We have a binary tree as list so
    # Define parameters as the left and right places of the given place in tree
    index_left = place * 2
    index_right = place * 2 + 1

    # Initialize as the given root
    largest_place = place
    # Checking if left leaf exists - if so, checking which leaf is bigger left or current root
    if index_left - 1 < size and lst[place - 1] < lst[index_left - 1]:
        largest_place = index_left
    # Checking if right leaf exists - if so, checking which leaf is bigger right or current root
    if index_right - 1 < size and lst[largest_place - 1] < lst[index_right - 1]:
        largest_place = index_right
    # If the heap is not order correctly in this place the largest place won't be the current root
    if largest_place != place:
        # Replacing the current root with the biggest value from left or right
        tmp = lst[place - 1]
        lst[place - 1] = lst[largest_place - 1]
        lst[largest_place - 1] = tmp
        # Make sure the leaf we just replaced fit to its new place
        if d:
            print("heapify")
        heapify(lst, size, largest_place)


def test():
    print("testing maximum value 100 times on random lists")
    for i in range(100):
        a = [random.randint(0, 1000) for i in range(100)]
        heap = MaxHeap(a)
        if max(a) != heap.maximum():
            raise Exception(f"something wrong, didn't pass on {a}")
    print("passed")
    print("-----------------------------------------------------------")
    print("testing extract max function and the heap max after")
    for i in range(100):
        a = [random.randint(0, 1000) for i in range(100)]
        heap = MaxHeap(a)
        for j in range(20):
            a_max = max(a)
            a.remove(max(a))
            heap_max = heap.extract_max()
            if a_max != heap_max:
                raise Exception(f"something wrong, didn't pass on {a} 1")
            if max(a) != heap.maximum():
                raise Exception(f"something wrong, didn't pass on {a} 2")
    print("passed")
    print("===========================================================")
    print("testing with insert")
    print("===========================================================")
    print("testing maximum value 100 times on random lists")
    for i in range(100):
        a = [random.randint(0, 1000) for i in range(100)]
        heap = MaxHeap()
        for val in a:
            heap.insert(val)
        if max(a) != heap.maximum():
            raise Exception(f"something wrong, didn't pass on {a}")
    print("passed")
    print("-----------------------------------------------------------")
    print("testing extract max function and the heap max after")
    for i in range(100):
        a = [random.randint(0, 1000) for i in range(100)]
        heap = MaxHeap()
        for val in a:
            heap.insert(val)
        for j in range(30):
            a_max = max(a)
            a.remove(max(a))
            heap_max = heap.extract_max()
            if a_max != heap_max:
                raise Exception(f"something wrong, didn't pass on {a} 1")
            if max(a) != heap.maximum():
                raise Exception(f"something wrong, didn't pass on {a} 2")
    print("passed")


if __name__ == "__main__":
    test()
