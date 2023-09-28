"""
CISC-121
Name:   Marcela Rojas
Student Number: 20365657
Email:  22mr6@queensu.ca
Date: 2023-03-30
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""
#Import the Stack class from the stacks file
from Stack_class import Stack

#Create an empty stack
stack = Stack()

#let the user to add values tp the stack
num_values = int(input("How manhy items would you like to add to the stack? "))
for i in range(num_values):
    value = input(f"Enter value {i + 1}: ")
    stack.push(value)

#Print all the current stack contents
print("Current stack contents:", stack._values)
#Pop the top value off the stack and print it
popped_value = stack.pop()
print("Popped value:", popped_value)
#Peek at the top value of the stack and print it
top_value = stack.peek()
print("Top value:", top_value)
#Reverse the stack and print the new contents
stack.reverse()
print("Reversed stack contents:", stack._values)