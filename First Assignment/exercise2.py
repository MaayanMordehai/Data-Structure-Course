"""exercise2 module
   Functions:
     - bigCross2
     - get_direction_count_matrix
"""

def bigCross2(M, m):
    """
    This function finds the biggest cross - O(m^2)
    Parameters: 
        M - boolean matrix of mxm
        m - size of the cols and rows in the matrix
    Returns: 
        biggest cross point 
        biggest cross size
    """
    temp_matrix = get_direction_count_matrix(M, m)

    biggest_cross_size = -1
    biggest_cross_point = [-1, -1]

    for row in range(m):
        for col in range(m):
            # getting the cross size, -1 to not include the middle point
            cross_size = min(temp_matrix[row][col].values())-1

            if cross_size > biggest_cross_size:
                biggest_cross_size = cross_size
                biggest_cross_point = [col, row]
    return biggest_cross_point, biggest_cross_size


def get_direction_count_matrix(M, m):
    """
    This function creating matrix of dictionaries that containes the direction and the number of 1s in this direction on the M including the current point.
    Parameters:
        M - boolean matrix of mxm
        m - size of the cols and rows in the matrix
    Returns:
        matrix - the matrix of dictionaries
    """

    # setting the matrix as mxm with default value
    matrix = [[{'up' : 0, 'down': 0, 'left': 0, 'right': 0} for i in range(m)] for i in range(m)]

    #
    # Setting the new matrix
    # setting the up and left values by going over the matrix from the start
    # and setting the down and right values by going over the matrix from the end 
    #

    # starting from the first and last rows
    x_from_start = 0
    x_from_end = m - 1

    while x_from_start < m and x_from_end >= 0:
        # setting to the begging and ending of the row
        y_from_start = 0
        y_from_end= m - 1

        while y_from_start < m and y_from_end >= 0:
            # if there is a cross in the current point from the start
            if M[y_from_start][x_from_start]:
                # counting the point itself
                matrix[y_from_start][x_from_start]['up']+=1
                matrix[y_from_start][x_from_start]['left']+=1

                # adding the number of 1s up
                if y_from_start - 1 >= 0:
                    matrix[y_from_start][x_from_start]['up']+=matrix[y_from_start-1][x_from_start]['up']

                # adding the number of 1s left
                if x_from_start - 1 >= 0:
                    matrix[y_from_start][x_from_start]['left']+=matrix[y_from_start][x_from_start-1]['left']

            # if there is a cross in the current point from the end
            if M[y_from_end][x_from_end]:
                # counting the point itself
                matrix[y_from_end][x_from_end]['down']+=1
                matrix[y_from_end][x_from_end]['right']+=1

                # adding the number of 1s down
                if y_from_end + 1 < m:
                    matrix[y_from_end][x_from_end]['down']+=matrix[y_from_end+1][x_from_end]['down']

                # adding the number of 1s right
                if x_from_end + 1 < m:
                    matrix[y_from_end][x_from_end]['right']+=matrix[y_from_end][x_from_end+1]['right']
            # going to the next col from start and end
            y_from_start+=1
            y_from_end-=1
        # going to the next row from start and end
        x_from_start+=1
        x_from_end-=1
     
    return matrix
