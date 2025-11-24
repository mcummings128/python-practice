# Create two variables  left_number  and  right_number  , and assign each of them an integer.

# Create a variable  symbol  to store the operation symbol (+, -, *, or /).

# Create a last variable  result  initialized to 0, which will then contain the result of the calculation.

# Check that both variables  left_number  and  right_number  are indeed integers. If one or both are not integers, display a corresponding error message and exit the program. (Hint: Use the  isinstance()  function)

# Check that the symbol stored in the  symbol  variable corresponds to one of the 4 allowed operations (`+`, `-`, `*`, or `/`) using  match. If the symbol is incorrect, display a corresponding error message, and exit the program.

# Note that dividing a number by 0 is impossible, so you need to provide an additional conditional structure to check this case in the  match  structure. Use if-else conditions to perform this operation; if there is a division by 0, display  Error: division by zero is not allowed.  , otherwise store the calculation in the  result  variable.

# Display the result contained in the  result  variable.

def main():

    left_number = 64
    right_number = 128
    symbol = '+'
    result = 0

    if not isinstance(left_number,int) or not isinstance(right_number,int):
        print(f"error: either left_number ({left_number}) or right_number ({right_number}) is not an integer")
        sys.exit(1)

    match symbol:
        case '+':
            result = left_number + right_number
        case '-':
            result = left_number - right_number
        case '*':
            result = left_number * right_number
        case '/':
            if right_number == 0:
                print(f"Error: division by zero is not allowed.")
                sys.exit(1)
            else:
                result = left_number / right_number
        case '_':
            print(f"Error: the operation symbol must be '+', '-', '*', or '/'.")
            # print(f"symbol ({symbol}) is not +,-,*, or /.")
            sys.exit(1)

    print(f"The result of the operation is: {result}")