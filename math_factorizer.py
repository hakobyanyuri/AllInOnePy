def get_factors(num):
    """
    Function to calculate all factors of a given number efficiently.
    
    Parameters:
    num (int): The number for which factors need to be calculated.
    
    Returns:
    list: A sorted list of factors of the number.
    """
    factors = set()  # Use a set to avoid duplicates
    for i in range(1, int(num**0.5) + 1):  # Loop only up to square root of num
        if num % i == 0:  # Check if 'i' is a factor of 'num'
            factors.add(i)  # Add 'i' to the set
            factors.add(num // i)  # Add the corresponding factor
    
    return sorted(factors)  # Return sorted factors for readability

if __name__ == "__main__":
    try:
        # Input: Get a number from the user
        n = int(input("Enter a number to find its factors: "))
        if n <= 0:
            raise ValueError("Please enter a positive integer.")
        
        # Output: Print the list of factors
        print(f"Factors of {n}: {get_factors(n)}")
    except ValueError as e:
        print(f"Invalid input: {e}")
