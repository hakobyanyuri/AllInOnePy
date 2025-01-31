def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9

def get_temperature_input(unit):
    """
    Get valid numeric temperature input from the user.
    
    Parameters:
    unit (str): The unit of temperature (°C or °F).
    
    Returns:
    float: The valid temperature entered by the user.
    """
    while True:
        try:
            temp = float(input(f"Enter the temperature in degrees {unit}: "))
            return temp
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    """Main function to handle user choice and perform conversion."""
    while True:  # Loop to allow multiple conversions
        print("\nSelect conversion type:")
        print("1: Celsius to Fahrenheit")
        print("2: Fahrenheit to Celsius")
        print("3: Exit")
        
        choice = input("Enter your choice: ").strip()  # Strip removes accidental spaces
        
        if choice == "1":
            c = get_temperature_input("Celsius")  # Get valid Celsius input
            f = celsius_to_fahrenheit(c)
            print(f"{c}°C ---> {f:.2f}°F")  # Formatted output

        elif choice == "2":
            f = get_temperature_input("Fahrenheit")  # Get valid Fahrenheit input
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F ---> {c:.2f}°C")  # Formatted output
        
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break  # Exit the loop

        else:
            print("Incorrect choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
