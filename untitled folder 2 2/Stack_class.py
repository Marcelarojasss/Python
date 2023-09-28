"""
CISC-121
Name:   Marcela Rojas
Student Number: 20365657
Email:  22mr6@queensu.ca
Date: 2023-03-30
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""

class Stack:
    def __init__(self):
        """
        Initializes an empty stack and then Data is stored in a list.
        """
        self._values = []

    def is_empty(self):
        """
        Returns True when the stack is empty, False if its not
        """
        return len(self._values) == 0

    def push(self, value):
        """
        Adds the "value" to the top of the stack
        """
        self._values.append(value)

    def pop(self):
        """
        Removes and returns the value at the top of the stack
        If the stack is empty, returns None
        """
        if self.is_empty():
            return None
        else:
            return self._values.pop()

    def peek(self):
        """
        Returns the value at the top of the stack, without removing it.
        If the stack is empty, returns None.
        """
        if self.is_empty():
            return None
        else:
            return self._values[-1]

    def reverse(self):
        """
        Reverses the order of the values in the stack.
        """
        self._values.reverse()