import random
from heap import MaxHeap


def heap_sort(lst):
    """
    This functions is sorting a list according to heap sort in O(nlog(n))
    :param lst: The list to sort
    :return: The sorted list
    """
    size = len(lst)
    heap = MaxHeap(lst)
    sorted_lst = []
    for i in range(size):
        sorted_lst.append(heap.extract_max())
    return sorted_lst[::-1]


def count_sort(lst, max_value=1000):
    """
    Count sort is for use when you know your value can't pass max_value.
    k needs to be O(n), if k is O(n^2) then count sort is worst then comparing sorts of O(nlog(n))
    O(k + n) (k is max_value)
    count sort is unstable sort.
    :param lst: The list to sort
    :param max_value: The maximum value possible in the list
    :return: The sorted list
    """
    size = len(lst)
    counts = [0 for i in range(max_value+1)]
    # creating counts arr - O(size)
    for i in lst:
        if i > max_value or i < 0 or not isinstance(i, int):
            raise Exception("This value is not in count sort options")
        counts[i] += 1

    # setting each as the sum of its value and previse value - O(max_value)
    for i in range(1, max_value+1):
        counts[i] += counts[i - 1]
    # setting output list - O(size)
    output = [None for i in range(size)]
    for i in lst:
        output[counts[i]-1] = i
        counts[i] -= 1

    return output


def radix_sort(lst, base=10):
    """
    Radix sort, sorting digit by digit. this is O(d*(n + k)) = O(n + k)
    d - digit number, k - base, n - size of the list
    Sorting first the lowest digits, and continuing until finished.
    Radix sort need helper fot the sorting by digit. The helper must be stable sort algorithm.
    Here using count sort with some changes for stability and by digit sort as helper.
    :param lst:
    """
    maximum = max(lst)
    count = 1
    sorted_lst = lst
    while int(maximum / count) > 0:
        sorted_lst = _radix_helper(sorted_lst, count, base)
        count *= base
    return sorted_lst


def _radix_helper(lst, count, base=10):
    """
    Using an adjusted count sort to sort each time the next digit
    This is O(n + k) - k is the base
    Adjust the count sort to be stable sort
    :param lst: The list to sort
    :param count: base ** number of time the function as run
    :param base: The base for the counting - default 10
    :return: The sorted list
    """
    size = len(lst)
    counts = [0 for i in range(base)]
    # creating counts arr - O(size)
    for val in lst:
        counts[int((val / count) % base)] += 1

    # setting each as the sum of its value and previse value
    for i in range(1, base):
        counts[i] += counts[i - 1]

    # setting output list - O(size)
    output = [None for i in range(size)]
    # passing on the list upside down for the sort to be stable
    # stable sort is mandatory for radix algorithm
    for val in lst[::-1]:
        output[counts[int((val / count) % base)]-1] = val
        counts[int((val / count) % base)] -= 1

    return output


def basic_testing_sort_func(func):
    print("============================================================")
    print("testing {} sorting function".format(func.__name__))
    for i in range(100):
        a = [random.randint(0, 1000) for i in range(10)]
        a_sorted = sorted(a)
        h_sorted = func(a)
        for j in range(len(a)):
            if a_sorted[j] != h_sorted[j]:
                raise Exception(f"something wrong, sort did'nt pass on {a}")
    print("passed")


def test():
    basic_testing_sort_func(heap_sort)
    basic_testing_sort_func(count_sort)
    basic_testing_sort_func(radix_sort)


if __name__ == "__main__":
    test()
