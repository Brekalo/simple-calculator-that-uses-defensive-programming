# Simple calculator that uses defensive programming

> **Table of Contents:**
> * Project description
> * Code description
> * Usage

#### **Project description:**
The program contains several functions, it is a basic framework for a simple calculator program that can perform arithmetic equations interactively and read equations from a file, displaying the results and storing them in a file named equations.txt. It demonstrates the use of functions, exception handling, file input/output operations, and user input validation.

#### **Code description:**
1. The code begins by importing the os module, which provides functions for interacting with the operating system.
2. A custom exception `class InvalidOperatorError` is defined to handle invalid operator inputs.
3. The `performArithmeticOperation():` function takes three arguments: `firstNumber`, `secondNumber`, and `operator`. It performs basic arithmetic operations based on the operator provided and returns the result.
4. The `loadEquationsFromFile():` function takes a file `filePath` as an argument (as input), which represents the path to a file containing equations. It first checks if the file exists using `os.path.exists()` and `raises` a `FileNotFoundError` if it does not exist. If the file exists, it proceeds to open the file and read each line.
 - For each line in the file, it splits the line into a list of strings using `line.strip().split()`. Each element in the list represents a part of the equation: `firstNumber`, `operator`, and `secondNumber`.
- It tries to perform the arithmetic operation by calling the `performArithmeticOperation()` function with the parsed values. If the operation succeeds, it appends the formatted equation to the `formattedEquations` list.
- If an exception occurs during the arithmetic operation, it appends an error message to the `formattedEquations` list.
 - After processing all the lines in the file, it prints a message indicating that reading from the file is complete and returns the `formattedEquations` list.
5. The `simpleCalculatorInteractive():` function sets up an interactive calculator interface using a `while loop`. It prompts the user for `input`, allowing them to choose an option: to perform a calculation, read equations from a file, or exit the program. Based on the user's input, it performs the corresponding actions.
- If the user selects option "1", it prompts the user to enter the first number, second number, and operator. It then calls the `performArithmeticOperation()` function to perform the calculation and prints the result.
- It appends the equation and result to a file named "equations.txt" using the `open()` function in `append` mode.
- If the user selects option "2", it prompts the user to enter the file name, and then calls the `loadEquationsFromFile()` function with the provided file name and prints the formatted equations.
- If the user selects option "3", it asks the user if they want to quit the program. If the user responds with "yes", the program breaks out of the while loop and ends. Otherwise, it continues the loop.
6. The code uses exception handling to catch and handle potential errors. 
- If the user enters an invalid choice, it raises a `ValueError` and prints an error message.
- If a `ZeroDivisionError` for division by zero, occurs during the arithmetic operation, it prints an error message.
- If any other `Exception` occurs, it prints an error message is displayed to the user.
7. After each iteration of the `while loop`, it prints a message indicating that the operation is complete.
8. The `if __name__ == "__main__":` condition ensures that the `simpleCalculatorInteractive` function is only executed when the script is run directly and not when imported as a module.

#### **Usage:**
The program demonstrates a basic calculator program which handles error handling and files operations.
You can further expand or customize it to suit your specific needs, or integrate it into bigger projects.