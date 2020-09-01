
"""exercise1 module
   Functions:
     - bigCross1
     - get_cross_branch_size
"""

def bigCross1(M, m):
    """
    This function find the biggest cross - O(m^3)
    Parameters: 
        M - boolean matrix of mxm
        m - size of the cols and rows in the matrix
    Returns: 
        biggest cross point 
        biggest cross size
    """
    biggest_cross_size = -1
    biggest_cross_point = [-1, -1]

    # Going over the rows
    for row in range(m):
        # going over the cols
        for col in range(m):

            # if there is a cross in the current point
            if (M[row][col]):
                # getting the size of the cross branch in current point
                cross_size = get_cross_branch_size(M, m, row, col)

				# if we found a cross bigger than the biggest cross so far
                if cross_size > biggest_cross_size:
                    biggest_cross_size = cross_size
                    biggest_cross_point = [col, row]

    return biggest_cross_point, biggest_cross_size


def get_cross_branch_size(M, m, row, col):
    """
    This function finds the cross branch size
    Parameters:
        M - boolean matrix of mxm
        m - size of the cols and rows in the matrix
        col - the column of the middle cross point
    Returns: 
        the size of the cross branch
    """
 
    # The directions of the cross - down, up, right, left
    directions = [{'x': 0, 'y': -1}, {'x': 0, 'y': 1}, {'x': 1, 'y': 0}, {'x': -1, 'y': 0}]
    length_directions = [0 for i in range(len(directions))]

    for index in range(len(directions)):
        x, y = col, row

        # going in the direction until there are no more 1s
        while 0 <= x < m and 0 <= y < m and M[y][x]:
            x += directions[index]['x']
            y += directions[index]['y']
            length_directions[index]+=1
    # -1 so the middle point will not be counted
    return min(length_directions)-1