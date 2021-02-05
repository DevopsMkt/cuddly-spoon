# define the function
def calculate():
    print('Please choose your operator adding(+) subtracting(-) multiplying(*) didviding(/) for power(**) for module(%)')

    number_1 = int(input("Enter your first digit: "))
    operation = input("Enter your operator: ")
    number_2 = int(input("Enter your first digit: "))


# adding
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        print("You were adding.\n")
        print("How do I know that I'm a smart progammer ;)\n")

# subtracting
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        print("You were subtracting.\n")
        print("How do I know that I'm a smart progammer ;)\n")

# mulitplaying
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        print("You were mulitplaying.")
        print("How do I know that I'm a smart progammer ;)\n")

# dividing
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        print("You were dividing.\n")
        print("How do I know that I'm a smart progammer ;)\n")

# for power
    elif operation == '**':
        print('{} ** {} = '.format(number_1, number_2))
        print(number_1 ** number_2)
        print("You were using for power.\n")
        print("How do I know that I'm a smart progammer ;)\n")

# module
    elif operation == '%':
        print('{} % {} = '.format(number_1, number_2))
        print(number_1 % number_2)
        print("You were using module.\n")
        print("How do I know that I'm a smart progammer ;)\n")

    # if they get a error
    else:
        print("Your number you have typed is invalid, please restart your program!")
    # add again() here as a function outside the calculate()
    again()


def again():
    cal_again = input("Do you want to calculate again? Y = yes or N = no: ")

    # Taking user input
    if cal_again.upper() == 'Y':
        calculate()
    elif cal_again.upper() == 'N':
        print('Leave kid ;-;')
    else:
        again()


def welcome():
    print("Welcome to my calculator made by Pepa pig lol made in python :D")


# use calculate() for the function
welcome()
calculate()
