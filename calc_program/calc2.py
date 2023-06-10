print("Use 'q' as an operator to exit calculator")

def is_valid_number(input_value): # checks if input is a number
    try:
        float(input_value) # will try to make it a float
        return True # if it can it is an number
    except ValueError:
        return False 

def main():
    inUseOperators = ["+", "-", "/", "*", "**"]
    exit = False # exit status set to false initially
  
    while True:

        while True: # will loop untill input is correct or user input exit code
            num1 = input("Enter the number: ")

            if is_valid_number(num1): # checks if it is a digit
                break # if it  is then it will break out of the loop
            elif num1 == 'q':
                exit = True
                break
            else:
                print("Please input a valid number!") # error message

        while True:
          operator = input("Enter an operator: ")
          if operator == 'q':
            exit = True
            break
          if operator in inUseOperators: # iterates list untill found
            break
          else:
            print("Please input a valid operator ( - + / *):")

        if exit:
          break

        while True:
            num2 = input("Enter the number: ")

            if is_valid_number(num2):
                break
            elif num2 == 'q':
                exit = True
                break
            else:
                print("Please input a valid number!")

        if exit: # exits out of program if user inputs correct value
            break

        while True:

            if operator == "+":
                result = round(float(num1) + float(num2), 2)
                print(result)
                break
            elif operator == "-":
                result = round(float(num1) - float(num2), 2)
                print(result)
                break
            elif operator == "/":
                result = round(float(num1) / float(num2), 2)
                print(result)
                break
            elif operator == "*":
                result = round(float(num1) * float(num2), 2)
                print(result)
                break
            elif operator == "**":
                result = round(float(num1) ** float(num2), 2)
                print(result)
                break 
        

# Perform arithmetic

if __name__ == "__main__":
    main()
