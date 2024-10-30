# Isabell Mora
# UWYO COSC 1010
# 10-28-24
# Lab 07
# Lab Section: 
# Sources, people worked with, help given to: 
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered
result = 1
con = 1
while con:
    upper_bound_user = input("Enter non-negative integer: ")
    if upper_bound_user.isdigit():
        u_bound = int(upper_bound_user)
        if u_bound == 0 or u_bound == 1:
            result = 1
        for value in range(2, u_bound + 1):
            result *= value

    
        print(result)
        con = 0
    else:
        print("Please enter valid integer")


print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 
num_sum = 0 
n_sum = 1
while n_sum:
    sum_1 = input("Please enter any number of integers or exit to stop: ")
    sum_1 = sum_1.lower()
    if sum_1 == "exit":
        n_sum = 0 
    if sum_1[0] == "-":
        sum_1 = sum_1.replace("-","")
        
        if sum_1.isdigit():
            num_sum -= int(sum_1)
        else:
            print("Please enter valid integer")
    elif sum_1.isdigit():
            num_sum += int(sum_1)
    else:
        print("Please enter valid integer")



print(f"Your final sum is {num_sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

calc_user = input("Please input in the form of 'operand operator operand': ")
calc_user = calc_user.replace(" ","")

calculator = "+-*/%"
calculator2 = None
calculator_pos = 0

for num in calculator:
    if num in calc_user:
        op = calc_user.split(num)
        if len(op) == 2:
            integer1, integer2, = op
            calculator = num
            break

if calculator and integer1 and integer2: 
    integer1, integer2 = calc_user.split(calculator)
    try:
        integer1 = float(integer1)
        integer2 = float(integer2)

        if calculator == "+":
            output = integer1 + integer2
        elif calculator == "-":
            output = integer1 - integer2
        elif calculator == "*":
            output = integer1 * integer2
        elif calculator == "/":
            output = integer1 / integer2 if integer2 != 0 else "No zero in denominator"
        elif calculator == "%": 
            output = integer1 % integer2 if integer2 != 0 else "No zero in denominator"
        else: 
            output = "Invalid operation"
    except ValueError: 
        output = "Please enter valid integers"
else: 
    output = "No operation found!"
print("Output:",output)

    

