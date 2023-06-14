
"""
Task 1
- Create a simple calculator application that asks a user to enter two numbers 
nd the operation (e.g. +, -, x, etc.) that they'd like to perform on the numbers. 
Display the answer to the equation. Every equation entered by the user should be written to a text file. 
Use defensive programming to write this program in a manner that is robust and handles unexpected events and user inputs.
- Now extend your program to give the user the option to either enter two numbers and an operator, like before, 
or to read all of the equations from a new txt file (the user should add the name of the txt file as an input) 
and print out all of the equations together with the results. 
Use defensive coding to ensure that the program does not crash if the file does not exist 
and that the user is prompted again to enter the name of the file.
"""

# ask the user to input two numbers and operator
def performArithmeticOperation():
    firstNumber = input("Please enter the 1st number:\n > ")
    secondNumber = input("Please enter the 2nd number:\n > ")
    operator = input(
        "Please enter the operator (+, -, *, /):\n > ")

# using 'try-except' block is to catch any 'ValueError' exceptions that might occur when converting the input numbers
    try:
        firstNumber = int(firstNumber)
        secondNumber = int(secondNumber)
    except ValueError:
        print("Incorrect entry! Please enter a number.")
        return

# using 'if-elif-else' to determine the operator entered by the user
    if operator == "+":
        result = firstNumber + secondNumber
    elif operator == "-":
        result = firstNumber - secondNumber
    elif operator == "*":
        result = firstNumber * secondNumber
    elif operator == "/":

        # 'try-except' block is to catch any 'ZeroDivisionError' exceptions that might occur when the user tries to divide a number by zero
        try:
            result = firstNumber / secondNumber
        except ZeroDivisionError:
            print("Incorrect entry! Cannot be divided by zero.")
            return
    else:
        print("Incorrect entry! Please enter the operator (+, -, *, /).")
        return
# displays the result of the quationsFilePath
    print(f"The result is: {result}")

    # using 'with open' is to open a file "equations.txt" in append mode and write the equation and its result to the file
    with open("equations.txt", "a") as my_file:
        my_file.write(f"{firstNumber} {operator} {secondNumber} = {result}\n")


# using 'while True' is to call the 'performArithmeticOperation' repeatedly until the user chooses to exit
while True:
    performArithmeticOperation()
    userExit = input("Would you like to calculate again? (Yes/No):\n > ")
    if userExit.lower() != "yes":
        # using 'break' is to exit the 'while' loop if the user choose not to perform another quationsFilePath
        break
