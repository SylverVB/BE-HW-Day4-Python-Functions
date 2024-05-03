# Lesson 5: Assignments | Python Functions

# 1. The Calculator App

# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

def add(a, b):
    return a + b

def subt(a, b):
    return a - b
    
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:               
        print("Error: Division by zero error")
        return None
    return a / b

print(f"The sum of {a} and {b} is {round(add(a, b), 2)}")
print(f"The difference between {a} and {b} is {round(subt(a, b), 2)}")
print(f"The product of {a} and {b} is {round(multiply(a, b), 2)}")

if divide(a, b) is not None:
    print(f"The quotient of {a} and {b} is {round(divide(a, b), 2)}")
else:
    print(f"Cannot divide {a} by {b}")


# 2. The Shopping List Maker

# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")
    return shopping_list

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")
    return shopping_list

def print_list(shopping_list):
    if shopping_list:
        print("Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")
    return shopping_list

def main():
    shopping_list = []

    while True:
        print("\nOptions:")
        print("1) Add item to the list")
        print("2) Remove item from the list")
        print("3) Print the shopping list")
        print("4) Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list = add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            shopping_list = remove_item(shopping_list, item)
        elif choice == '3':
            shopping_list = print_list(shopping_list)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()