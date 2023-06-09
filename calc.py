# Simple Calculator Input function
print("Use 'q' as an operator to exit calculator")
input("Press return to continue...")
print()
def calculatorFunction():
    inUseOperators = ["+", "-", "/", "*", "q"]
    num1 = input("Enter the number: ")
    operator = input("Enter an operator ( - + / *): ")
    num2 = input("Enter the number: ")
    num = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
      
    if operator == "+":
        result = round(float(num1) + float(num2), 2)
        print(result)
        calculatorFunction()
    elif operator == "-":
        result = round(float(num1) - float(num2), 2)
        print(result)
        calculatorFunction()
    elif operator == "/":
        result = round(float(num1) / float(num2), 2)
        print(result)
        calculatorFunction()
    elif operator == "*":
        result = round(float(num1) * float(num2), 2)
        print(result)
        calculatorFunction()
    elif operator == "q":
        print("exit")
    
    
    
    # Experimenting with try and catch

    # elif isinstance(num, float) == (num1 and num2):
    #     try:
    #         print("Input field has to be a number")
    #         calculatorFunction()
    #     except:
    #         print(num1, num2)
    
    # if (num1 and num2).isspace == True:
    #     try:
    #         print("Input field cannot be empty")
    #         calculatorFunction()
    #     except:
    #         print(num1, num2)
  
    elif operator != inUseOperators:
        try:
            (operator in inUseOperators) == False
        except:
            print("Invalid operator")
            calculatorFunction()
        else:
            print(f'Operator state: {operator}')
    # elif operator == inUseOperators:
    #     print(f'Operator state: {operator}')
    # e
            
            # print("Invalid value for number")
            # calculatorFunction()

    
    #     # else:
    #     #     operator == "break"
    #     #     return None
        
    

calculatorFunction()