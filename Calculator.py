# simple calculator
try:
  # prompt user
    num1 = float(input("Please Enter The first number: "))
    operator = input("Please choose the operator (+) for addition, (-) for subtraction, (*) for multiplication"
                     "(/) for division , (%) for remainder: ")
    num2 = float(input("Please Enter The second number: "))
    
    if operator == '+':
        result = num1 + num2
        print("The result is: ", result)
    elif operator == '-':
        result = num1 - num2
        print("The result is: ", result)
    elif operator == '*':
        result = num1 * num2
        print("The result is: ", result)
    elif operator == '/':
        try:
            if True:
                result = num1 / num2
                print(result)
        except ZeroDivisionError as err:
            print(err, " oops! zero division occur ")
    elif operator == '%':
        if operator == '%':
            result = num1 % num2
            print("The result is: ", result)
    else:
        raise TypeError


except ValueError:
    print("wrong value, suggest integer or decimal")
finally:
    print("All Done")

