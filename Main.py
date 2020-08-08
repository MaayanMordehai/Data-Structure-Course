from exercise1 import bigCross1
from exercise2 import bigCross2
from random import getrandbits
from datetime import datetime

def generate_matrix(m):
    """
    This function generates a random matrix of 1s and 0s only
    Parameters:
        m - the size of the matrix
    Returns:
        The matrix
    """
    return [[getrandbits(1) for i in range(0, m)] for i in range(0, m)]

def generate_worst_case_matrix(m):
    """
    This function genrates our worst case matrix which is matrixs of 1s only
    Parameters:
        m - the size of the matrix
    Returns:
        The matrix
    """
    return [[1 for i in range(0, m)] for i in range(0, m)]

def test_cross_func(func, M, m):
    """
    This function tests a biggest Cross function execution time, and prints the findings.
    Parameters:
        func - the function
        M - the matrix we are using for the test
        m - the size of the matrix M
    """
    print("testing {} on matrix size {}".format(func.__name__, m))
    start_time = datetime.now()
    point, size = func(M, m)
    end_time = datetime.now()
    print("Biggest Cross: middle point {} branch size {}".format(point, size))
    print("time taken: {}".format(end_time - start_time))

def main():
    # Creating the test matrixs
    first_matrix_size = 15
    first_matrix =  generate_worst_case_matrix(first_matrix_size)
    second_matrix_size = 50
    second_matrix =  generate_matrix(second_matrix_size)

    # Testing bigCross1 O(m^3) vs bigCross2 O(m^2)
    print("=====================================================================")
    test_cross_func(bigCross1, first_matrix, first_matrix_size)
    print("---------------------------------------------------------------------")
    test_cross_func(bigCross2, first_matrix, first_matrix_size)
    print("=====================================================================")
    test_cross_func(bigCross1, second_matrix, second_matrix_size)
    print("---------------------------------------------------------------------")
    test_cross_func(bigCross2, second_matrix, second_matrix_size)
    print("=====================================================================")


if __name__ == '__main__':
    main()