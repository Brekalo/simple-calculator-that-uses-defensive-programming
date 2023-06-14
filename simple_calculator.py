import os


# using the 'map' to unpack the equation list into 3 separate variables (firstNumber, operator, secondNumber) instead of indexing each element separately
# added a 'finally' block to 'loadEquationsFromFile' and 'simpleCalculatorInteractive', 
# but finally block in 'performArithmeticOperation' it is not necessary because there no resources to be open that need to be closed



def performArithmeticOperation(firstNumber, secondNumber, operator):
    try:
        if operator == "+":
            return firstNumber + secondNumber
        elif operator == "-":
            return firstNumber - secondNumber
        elif operator == "*":
            return firstNumber * secondNumber
        elif operator == "/":
            if secondNumber == 0:
                raise ZeroDivisionError("Cannot divide by zero./n")
            return firstNumber / secondNumber
        else:
            raise ValueError("Invalid operator!")
    except Exception as ex:
        return f"Error: {ex}"



def loadEquationsFromFile(filePath):
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
    except FileNotFoundError:
        print("File not found!")
        return []
    finally:
        print("Reading from file is complete.")
        


def simpleCalculatorInteractive():
    while True:
        try:
            userOption = input(
                "Please enter Option: '1' to calculate, or '2' to read from file:\n > ")
            if userOption == "1":
                firstNumber = int(input("Please enter the 1st number:\n > "))
                secondNumber = int(input("Please enter the 2nd number:\n > "))
                operator = input(
                    "Please enter the operator (+, -, *, /):\n > ")
                result = performArithmeticOperation(firstNumber, secondNumber, operator)
                print(f"{firstNumber} {operator} {secondNumber} = {result}")
                with open('equations.txt', "a") as my_file:
                    my_file.write(
                        f"{firstNumber} {operator} {secondNumber} = {result}\n")
                    print("File created and calculations written to the file.")
            elif userOption == "2":
                filePath = input("Please enter the file name:\n > ")
                equations = loadEquationsFromFile(filePath)
                for equationResult in equations:
                    print(equationResult)
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


# this checks whether the script is being executed as the 'main' code, and calls the 'simpleCalculatorInteractive' to start the main program loop
if __name__ == "__main__":
    simpleCalculatorInteractive()
    