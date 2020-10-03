

import random


class Node:
    """ This class is a node in Binary Search Tree """

    def __init__(self, data):
        """ Constructor of a node - setting the value """
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        """
        This Function is inserting data to the right node in the tree
        :param data: The data to insert
        """
        if self.data:
            if data[0] < self.data[0]:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def build_tree():
    """
    This Function is building binary tree of 1000 nodes
    :return: The root node of the tree
    """
    tree = Node(None)
    taken_points = []
    for i in range(1000):
        point = [random.uniform(0, 100), random.uniform(0, 100)]
        # if a point is taken - continue randomize points
        while point in taken_points:
            point = [random.uniform(0, 100), random.uniform(0, 100)]
        taken_points.append(point)
        tree.insert(point)
    return tree


def nearest_right_point(tree, x, nearest_point=None):
    """
    This Function is finding the nearest right point to x line.
    this is O(log(n)) in the average case
    :param tree: The root node of the tree
    :param x: The x line
    :param nearest_point: The point of the minimal difference
    :return: The nearest point
    """

    # The end of the tree
    if not tree:
        if not nearest_point:
            # There are no points from the right
            return [0, 0]
        return nearest_point

    # if the current node is closer to the x value (from the right)
    if 0 < tree.data[0] - x and (nearest_point is None or tree.data[0] - x < nearest_point[0] - x):
        nearest_point = tree.data

    # if x is smaller then current node x going over left subtree else right
    if x < tree.data[0]:
        return nearest_right_point(
            tree.left,
            x,
            nearest_point
        )
    return nearest_right_point(
        tree.right,
        x,
        nearest_point
    )


def main():
    line = -1
    while not isinstance(line, float) or line < 0 or line > 100:
        try:
            line = float(input("insert line x - needs to be between 0-100\n"))
        except Exception:
            print("line must be a real number ...")
    print("testing on random tree with 1000 nodes")
    print(f"nearest right point is {nearest_right_point(build_tree(), line)}")


if __name__ == '__main__':
    main()
