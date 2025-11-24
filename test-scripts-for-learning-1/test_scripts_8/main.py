# #### 2. Call the functions
# * In the `main.py` file, first import the `operations` module
# * Create a `main` function and add the instructions within the function:
#     * Call the `sum` function with the parameters `3` and `5`
#     * Print the result of the sum using the `print` function.
#     * Call the `product` function with the parameters `8` and `2`
#     * Print the result of the product using the `print` function.

# #### 3. Call the `main` function

import operations

def main():
    
    sum = operations.sum(3,5)
    print(f"The sum of 3 + 5 is {sum}")
    product = operations.product(8,2)
    print(f"The product of 8 * 2 is {product}")

if __name__ == "__main__":
    main()