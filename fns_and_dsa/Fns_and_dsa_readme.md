This project delves into the fundamentals of functions, data structures, and modules in Python. You’ll explore how to define and utilize functions, effectively manage data using various built-in structures, and leverage modules and libraries to extend Python’s capabilities.

Project Objectives:
By the end of this project, you should be able to:

Define the purpose and importance of functions in Python programming.
Construct functions using def and lambda keywords, understanding proper syntax.
Work with function parameters, argument passing mechanisms, default values, and keyword arguments.
Explain the concept of return values and utilize the return statement effectively.
Distinguish between local and global variable scope within functions.
Apply global and nonlocal keywords appropriately to manage variable scope.
Identify common Python data structures: Lists, Tuples, Sets, and Dictionaries.
Select the appropriate data structure based on the type of data and operations needed.
Perform operations on Lists (indexing, slicing, appending, etc.).
Utilize Dictionary methods, understand the immutability of Tuples, and perform Set operations.
Explain the concepts of modules and packages in Python.
Create and use custom modules, and import standard modules provided by Python.
Install and use external Python libraries using pip.
Identify some essential Python libraries and their functionalities (e.g., requests).
Comprehend the LEGB rule (Local, Enclosing, Global, Built-in) for understanding variable scope in Python.
Implement best practices for effective variable scope management.
Explain the concept of namespaces in Python and differentiate between their types.
Describe the lifecycle of a namespace and how scope resolution works in Python.
This project equips you with the building blocks for creating well-organized and efficient Python programs. By mastering these concepts, you’ll be able to write clean, maintainable, and reusable code.

Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Arithmetic Operations Function
mandatory
Create a Python script named arithmetic_operations.py. In this script, define a function that performs basic arithmetic operations. This function, perform_operation, will be imported and used in a separate main.py script, which we provide.

Requirements for arithmetic_operations.py:
Function Definition:
Define a function named perform_operation.
Parameters: num1 (float), num2 (float), and operation (string). The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.
Return the result of the arithmetic operation.
Provided main.py for Testing:
from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
Here is an example output

>>> python .\main.py
Arithmetic Operations
Enter the first number: 5
Enter the second number: 6
Enter the operation (add, subtract, multiply, divide): add
Result: 11.0
Note: - Focus on implementing the perform_operation function in arithmetic_operations.py. Ensure your function correctly handles the operations based on the inputs. - You do not need to create or modify main.py. It is provided for you to test your function. The checker will use this main.py to import your arithmetic_operations.py script and test its functionality.

Repo:

GitHub repository: alx_be_python
Directory: fns_and_dsa
File: arithmetic_operations.py
 
1. Shopping List Manager
mandatory
Objective: Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.

Task Description:
Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.

Requirements:
Core Functionality:

Your script should start with an empty list named shopping_list.
Implement functionality to add items to the list, remove items, and display the current list.
User Interface:

Use a loop to continuously display a menu with options to the user until they choose to exit. The menu should offer options to add an item, remove an item, view the list, and exit.
For adding items, prompt the user for the item name and append it to shopping_list.
For removing items, ask the user for the item name and remove it from shopping_list. If the item is not found, display a message indicating so.
To view the list, print each item in shopping_list to the console.
Ensure your script handles invalid menu choices gracefully.
shopping_list_manager.py Skeleton:
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
Note for Students:

You are responsible for completing the main() function with the appropriate logic to handle adding, removing, and displaying items in the shopping_list.
This task introduces you to working with lists in a practical scenario, enhancing your understanding of how dynamic data structures can be manipulated and utilized in Python programs.
Repo:

GitHub repository: alx_be_python
Directory: fns_and_dsa
File: shopping_list_manager.py
 
2. Explore `datetime` Module
mandatory
Objective: Familiarize yourself with Python’s datetime module by writing a script that performs specified operations with dates and times.

Task Instructions:
Your task is to create a Python script named explore_datetime.py. This script will demonstrate your ability to use the datetime module for handling dates and times in Python.

Part 1: Display the Current Date and Time

Research how to use the datetime module to obtain the current date and time.
Create a function with a name display_current_datetime and
save the current date inside a current_date variable
Format and print the current date and time in a readable format, such as “YYYY-MM-DD HH:MM:SS”.
Part 2: Calculate a Future Date

Prompt the user to enter a number of days (as an integer).
Create a function with a name calculate_future_date and
saves the future date inside a future_date variable
Calculate what the date will be after adding the specified number of days to the current date.
Print the future date in a format like “YYYY-MM-DD”.
Guidance:
Start by importing the necessary components from the datetime module.
Look into the datetime.now() function to get the current date and time.
Use timedelta(days=number_of_days) to represent the duration to add to the current date.
Remember, Python’s official documentation is an excellent resource for learning how to use the standard library modules.
Example Output (Hypothetical):
Current date and time: 2024-03-25 15:30:45
Enter the number of days to add to the current date: 10
Future date: 2024-04-04
Repo:

GitHub repository: alx_be_python
Directory: fns_and_dsa
File: explore_datetime.py
 
3. Temperature Conversion Tool
mandatory
Objective: Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors.

Task Description:
Create a Python script named temp_conversion_tool.py. This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

Requirements:
Define Global Conversion Factors:

At the top of your script, define two global variables FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR to store the conversion factors (e.g., (5/9) for F to C and (9/5) for C to F, respectively).
Implement Conversion Functions:

Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
Inside each function, use the respective global conversion factor to perform the conversion.
User Interaction:

Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
Based on the user’s input, call the appropriate conversion function and display the converted temperature.
If gthe user entered a wrong input,raise an error “Invalid temperature. Please enter a numeric value.”
Guidance:
Remember to access global variables using the global keyword if you need to modify them inside functions. However, for this task, you’ll only be reading their values.
Use input validation to ensure that the user enters a valid temperature and unit.
Example Output (Hypothetical):
Enter the temperature to convert: 100
Is this temperature in Celsius or Fahrenheit? (C/F): F
100.0°F is 37.77777777777778°C
Or:

Enter the temperature to convert: 0
Is this temperature in Celsius or Fahrenheit? (C/F): C
0.0°C is 32.0°F
Repo:

GitHub repository: alx_be_python
Directory: fns_and_dsa
File: temp_conversion_tool.py
 
