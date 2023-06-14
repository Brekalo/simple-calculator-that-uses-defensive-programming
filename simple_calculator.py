# import the os module, check if a file exists
import os


class InvalidOperatorError(Exception):
    pass

def performArithmeticOperation(firstNumber, secondNumber, operator):
    if operator == "+":
        return firstNumber + secondNumber
    elif operator == "-":
        return firstNumber - secondNumber
    elif operator == "*":
        return firstNumber * secondNumber
    elif operator == "/":
        if secondNumber == 0:
            raise ZeroDivisionError("Incorrect entry! Cannot be divided by zero.")
        return firstNumber / secondNumber
    else:
        raise InvalidOperatorError("Invalid operator!")


def loadEquationsFromFile(filePath):
    if not os.path.exists(filePath):
        raise FileNotFoundError("File not found!")
    
    formattedEquations = []
    try:
        with open(filePath, "r") as my_file:
            for line in my_file:
                equation = line.strip().split()
                firstNumber, operator, secondNumber = map(str, equation)
                try:
                    result = performArithmeticOperation(int(firstNumber), int(secondNumber), operator)
                    formattedEquations.append(f"{firstNumber} {operator} {secondNumber} = {result}")
                except Exception as ex:
                    formattedEquations.append(f"{firstNumber} {operator} {secondNumber} = Error ({ex})")
        return formattedEquations
    finally:
        print("Reading from file is complete.")


def simpleCalculatorInteractive():
    while True:
        try:
            # prompt user for input
            userOption = input("Please enter Option: '1' to calculate, or '2' to read from file, or '3' to exit:\n > ")

            if userOption == "1":
                # perform arithmetic calculation
                firstNumber = int(input("Please enter the 1st number:\n > "))
                secondNumber = int(input("Please enter the 2nd number:\n > "))
                operator = input("Please enter the operator (+, -, *, /):\n > ")
                result = performArithmeticOperation(firstNumber, secondNumber, operator)
                print(f"{firstNumber} {operator} {secondNumber} = {result}")

                # write calculation to file
                with open("equations.txt", "a") as my_file:
                    my_file.write(f"{firstNumber} {operator} {secondNumber} = {result}\n")
                print("File created and calculations written to the file.\n")

            elif userOption == "2":
                # load equations from file and display results
                filePath = input("Please enter the file name:\n > ")
                equations = loadEquationsFromFile(filePath)
                for equationResult in equations:
                    print(equationResult)

            elif userOption == "3":
                # exit the program
                userQuit = input("Would you like to quit the program? (Yes/No):\n > ")
                if userQuit.lower() == "yes":
                    break
                else:
                    continue

            else:
                raise ValueError("Invalid choice!")
            
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")
        finally:
            print("The operation is complete.\n")

# simpleCalculatorInteractive()

if __name__ == "__main__":
    simpleCalculatorInteractive()
    