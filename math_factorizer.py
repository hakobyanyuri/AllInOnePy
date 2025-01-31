def get_factors(num):
    """
    Function to calculate all factors of a given number.
    
    Parameters:
    num (int): The number for which factors need to be calculated.
    
    Returns:
    list: A list of factors of the number.
    """
    factors = []  # Initialize an empty list to store factors
    for i in range(1, num + 1):  # Loop through numbers from 1 to the given number
        if num % i == 0:  # Check if 'i' is a factor of 'num'
            factors.append(i)  # Add 'i' to the factors list
    return factors

if __name__ == "__main__":
    # Input: Get a number from the user
    n = int(input("Enter a number to find its factors: "))
    
    # Output: Print the list of factors
    print(f"Factors of {n}: {get_factors(n)}")
