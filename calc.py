# Simple Calculator Input function
def calculatorFunction():
    num1 = float(input("Enter the number: "))
    operator = input("Enter an operator ( - + / *): ")
    num2 = float(input("Enter the number: "))

    if operator == "+":
        result = float(round(num1 + num2, 2))
        print(result)
    elif operator == "-":
        result = float(round(num1 - num2, 2))
        print(result)
    elif operator == "/":
        result = float(round(num1 / num2, 2))
        print(result)
    elif operator == "*":
        result = float(round(num1 * num2, 2))
        print(result)
    else:
        print("Invalid operator")
    

calculatorFunction()

# ----------------------------------------------------------------

# Calculator Function v2.0
# Trying to create a state where contiuous calculations can be
# performed within one session. How to use while & for loops to
# achieve this?

# def calculatorFunction():
#     num1 = float(input("Enter the number: "))
#     operator = input("Enter an operator ( - + / *): ")
#     num2 = float(input("Enter the number: "))
#     i = 0
#     while i > 1:
#         if operator == "+":
#             result = float(round(num1 + num2, 2))
#             print(result)
#             return result
#         elif operator == "-":
#             result = float(round(num1 - num2, 2))
#             print(result)
#             return result
#         elif operator == "/":
#             result = float(round(num1 / num2, 2))
#             print(result)
#             return result
#         elif operator == "*":
#             result = float(round(num1 * num2, 2))
#             print(result)
#             return result
#         elif operator == "!":
#             i +=1
#             return i
#         else:
#             print("Invalid operator")
#         print(result)
#         session = result
#         break


# calculatorFunction()
