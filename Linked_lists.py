class Node:
    def __init__(self, data, next_node):
        self._data = data
        self._next_node = next_node

    def set_next(self, node):
        return set_next

    def get_next(self):
        return get_next

    def get_data(self):
        return get_data

class LinkedList:
    """
    A stack using a singly linked list to create a stack.
    """
    def __init__(self):
        self._head_node = None
        self._size = 0

    def __len__(self):
        """ Allows the use of len(stack) to find the number of elements in the stack """
        return self._size

    def push(self, data):
        new_node = self.set_next()
        self._head_node = new_node
        self._size += 1
        return self._head_node
        return self._size

    def pop(self):
        self._head_node = self.get_next
        self._size += 1
        return self._head_node
        return self._size

    def peek(self):
        return self._head_node
        
    def is_empty(self):
        if self._size == 0:
            empty = "The list is empty"
            return empty
        else:
            not_empty = "The list is not empty"
            return not_empty
    
    def __str__(self):
        """ Defines what should be displayed when the user prints a linked list object. """
        return "A linked list"

if __name__ == "__main__":
    my_stack = LinkedList()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print(my_stack, len(my_stack))

    while not my_stack.is_empty():
        print(my_stack.pop())