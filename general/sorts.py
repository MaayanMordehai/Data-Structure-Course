import random
from heap import MaxHeap


def heap_sort(lst, size):
    """
    This functions is sorting a list according to heap sort in O(nlog(n))
    :param lst: The list to sort
    :param size: The size of the list
    :return: The sorted list
    """
    heap = MaxHeap(lst)
    sorted_lst = []
    for i in range(size):
        sorted_lst.append(heap.extract_max())
    return sorted_lst[::-1]


def count_sort(lst, size, max_value=1000):
    """
    Count sort is for use when you know your value can't pass max_value.
    Is good when your value options are not too many, if it is too many you can also have memory problem.
    O(n)
    """
    counts = [0 for i in range(max_value+1)]
    # creating counts arr - O(size)
    for i in lst:
        if i > max_value or i < 0 or not isinstance(i, int):
            raise Exception("This value is not in count sort options")
        counts[i] += 1

    # setting each as the sum of its value and previse value - O(max_value)
    pre = 0
    for i in range(max_value+1):
        counts[i] += pre
        pre = counts[i]

    # setting output list - O(size)
    output = [None for i in range(size)]
    for i in lst:
        output[counts[i]-1] = i
        counts[i] -= 1

    return output


def basic_testing_sort_func(func):
    print("============================================================")
    print("testing {} sorting function".format(func.__name__))
    for i in range(100):
        a = [random.randint(0, 1000) for i in range(100)]
        a_sorted = sorted(a)
        h_sorted = func(a, len(a))
        for j in range(len(a)):
            if a_sorted[j] != h_sorted[j]:
                raise Exception(f"something wrong, sort did'nt pass on {a}")
    print("passed")


def test():
    basic_testing_sort_func(heap_sort)
    basic_testing_sort_func(count_sort)


if __name__ == "__main__":
    test()
