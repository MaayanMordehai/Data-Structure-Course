import random


# region LinkedList definition
class Node:
    """ This class is a node of a linked list """

    def __init__(self, val):
        """ Constructor of a node - setting the value """
        self.val = val
        self.next = None


class LinkedList:
    """ This class is a Linked list """

    def __init__(self):
        """ Constructor of a Linked List - initiating as an empty list """
        # This is the head node of the linked list
        self.head = None
# endregion


def create_random_linked_list():
    """
    This function creates a random linked list according to the following:
    - randomize between snake or snail in probability of 0.5 each
    - For snake:
        - randomize between adding a node (probability of 0.99) or ending the list (probability of 0.01)
    - For snail:
        - randomize between adding a node (probability of 0.98) or making this the last node in loop
        (probability of 0.02)
        - randomize in each node is it the node that starts the loop (probability of 0.015 it does)
        - if there is no node to start the loop choosing the head node to start it
    :return: the randomized linked list
    """
    my_list = LinkedList()

    # Choosing between snake and snail
    choices = ["Snake", "Snail"]
    probability = [0.5, 0.5]
    chosen = random.choices(choices, probability)[0]

    if chosen == "Snake":
        # Choosing between adding node or end linked list
        # adding node in probability of 0.99, ending linked list in probability of 0.01
        adding_choices = [True, False]
        adding_probabilities = [0.99, 0.01]
        # initiating the previous node as None - in the beginning there is no previous node
        pre_node = None
        # checking if need to add node
        add_new_node = random.choices(adding_choices, adding_probabilities)[0]
        while add_new_node:
            # The new node
            node = Node(random.randint(1, 20))
            if not pre_node:
                # if we have not started the list yet The node is the head node
                my_list.head = node
            else:
                # adding the new node after the previous node
                pre_node.next = node
            # setting the previous node for the next iteration
            pre_node = node
            # checking if need to add more nodes
            add_new_node = random.choices(adding_choices, adding_probabilities)[0]

    elif chosen == "Snail":
        # The starting loop node choices and probabilities
        loop_node_choices = [True, False]
        loop_node_probabilities = [0.015, 0.985]

        # The adding new node choices and probabilities
        adding_choices = [True, False]
        adding_probabilities = [0.99, 0.01]

        # initiating the current node, previous node and starting loop node as none - there are no nodes yet
        curr_node = None
        pre_node = None
        loop_node = None

        # checking if need to add node
        add_new_node = random.choices(adding_choices, adding_probabilities)[0]
        while add_new_node:
            # The new node
            curr_node = Node(random.randint(1, 20))
            if not pre_node:
                # if we have not started the list yet The node is the head node
                my_list.head = curr_node
            else:
                # adding the new node after the previous node
                pre_node.next = curr_node
            # if we have not found a starting loop node yet
            if not loop_node:
                # checking if the current node will be the starting loop node
                is_loop_node = random.choices(loop_node_choices, loop_node_probabilities)[0]
                if is_loop_node:
                    loop_node = curr_node
            # setting the previous node for the next iteration
            pre_node = curr_node
            # checking if need to add more nodes
            add_new_node = random.choices(adding_choices, adding_probabilities)[0]

        # if we have not found our starting loop node - setting it to the head node
        if not loop_node:
            loop_node = my_list.head

        # if curr_node in None the linked list is empty so there is noting to do
        if curr_node:
            # setting the last node to point on the starting loop node
            curr_node.next = loop_node

    return my_list


def snake_or_snail(linked_list):
    """
    This Function is finding the starting of a loop according to Floyd's algorithm
    looping over the list with two pointers - one fast, goes x2 nodes and one slow only x1 nodes.
    If they meet there is a loop. They have to meet after maximum of 2 loop rounds.
    so this is O(n)
    :param linked_list: The linked list
    :return: The starting of a loop if a loop exists, if not - returns None
    """

    slow = linked_list.head
    fast = linked_list.head
    first_iteration = True
    while slow and slow.next and fast and fast.next and fast.next.next:
        if slow == fast and not first_iteration:
            # found a loop
            break
        slow = slow.next
        fast = fast.next.next
        first_iteration = False

    if slow != fast or first_iteration:
        # There is no loop - it is a snake
        return None

    """
    Getting the start of the loop, The logic:
    a = The number of nodes from head to start of loop
    b = The number of nodes from start of loop to meeting point
    c = The number of nodes in the loop
    d = Number of full loop rounds slow did
    e = Number of full loop rounds fast did
    The slow speed was 1
    The fast speed was 2 
    so: a + b + c*d = 2*(a + b + c*e) => a + b = c*(d - 2*e )
    we got that a+b is multiple of c
    So if we take two pointer - one from head one from meeting point and have them continue a steps in same speed,
    after a steps:
        - the pointer from head will reach the start of a loop
        - since a+b is a multiple of c - the pointer from the meeting point will also be at the start of the loop
    """
    from_start = linked_list.head
    from_meeting = fast
    while from_start != from_meeting:
        from_start = from_start.next
        from_meeting = from_meeting.next
    return from_start


def print_linked_list(linked_list):
    """
    This function prints the linked list and it's info
    :param linked_list: the linked list
    :return: stdout - prints the info and the linked list nicely
    """
    loop_start_node = snake_or_snail(linked_list)
    loop_count = None

    if loop_start_node:
        print("The linked list is a Snail!")
    else:
        print("The linked list is a Snake!")

    node = linked_list.head
    count = 0
    # printing the nodes until loop start nodes - if snake until None
    while node != loop_start_node:
        count += 1
        print(node.val, end=" -> ")
        node = node.next

    if not node:
        # node is None - this is a snake and we printed all of it's values
        print("null")
    else:
        # node is not None - this is a snail and we need to print the loop
        # Printing the loop start and counting it
        # the \u21b1 is for the special arrow sign
        print(u'\u21b1', node.val, end="")
        node = node.next
        count += 1
        # counting first loop node
        loop_count = 1
        # printing the rest of the loop
        while node != loop_start_node:
            count += 1
            loop_count += 1
            print(" -> ", node.val, end="")
            node = node.next
        # got to end - The \u21b2 is for the special arrow sign
        print(u'\u21b2')

    print("linked list count is : ", count)
    if loop_count:
        print("linked list loop count is : ", loop_count)


if __name__ == '__main__':
    lst = create_random_linked_list()
    print_linked_list(lst)
