def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a / b

def get_valid_float(prompt):
    """
    Expert Tip: Encapsulating the try-except block in a helper function 
    keeps the main logic clean and DRY (Don't Repeat Yourself).
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print(f"⚠️  '{user_input}' is not a valid number. Please try again.")

def main():
    # Mapping symbols to our custom functions
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    print("===  Pure Python Calculator ===")
    
    while True:
        # 1. Get Inputs
        num1 = get_valid_float("\nEnter the first number: ")
        
        op = input("Enter an operation (+, -, *, /): ").strip()
        while op not in operations:
            print(f"⚠️  Invalid operator. Please choose from: {', '.join(operations.keys())}")
            op = input("Enter an operation: ").strip()
            
        num2 = get_valid_float("Enter the second number: ")

        # 2. Execution with Error Handling
        try:
            # We retrieve the function from our dict and call it immediately
            calculation_func = operations[op]
            result = calculation_func(num1, num2)
            
            # Formatting: If the result is a whole number, show it as an int
            display_result = int(result) if result % 1 == 0 else round(result, 4)
            
            print(f"\n✅ Result: {num1} {op} {num2} = {display_result}")
            
        except ZeroDivisionError as e:
            print(f"\n🛑 Math Error: {e}")
        except Exception as e:
            print(f"\n🛑 An unexpected error occurred: {e}")

        # 3. Loop Control
        if input("\nCalculate again? (y/n): ").lower() != 'y':
            print("Exiting. Have a great day!")
            break

if __name__ == "__main__":
    main()