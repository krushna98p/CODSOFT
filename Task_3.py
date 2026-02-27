import random
import string

def generate_custom_password(length: int, complexity: int) -> str:
    """
    Generates a password based on desired length and complexity level.
    Levels:
    1 = Lowercase only
    2 = Lowercase + Uppercase
    3 = Letters + Numbers
    4 = Letters + Numbers + Symbols
    """
    # Start with lowercase as the baseline
    active_pools = [string.ascii_lowercase]
    
    # Add pools based on the chosen complexity level
    if complexity >= 2:
        active_pools.append(string.ascii_uppercase)
    if complexity >= 3:
        active_pools.append(string.digits)
    if complexity >= 4:
        active_pools.append(string.punctuation)
        
    # Combine all active pools into one giant string for general selection
    all_characters = "".join(active_pools)

    password_chars = []

    # Check if the length is long enough to guarantee one character from each active pool
    num_pools = len(active_pools)
    
    if length >= num_pools:
        # Guarantee one character from each selected category
        for pool in active_pools:
            password_chars.append(random.choice(pool))
            
        # Fill the remaining length with random choices from all allowed characters
        for _ in range(length - num_pools):
            password_chars.append(random.choice(all_characters))
    else:
        # If the password is too short to fit all requested types, just pick randomly
        for _ in range(length):
            password_chars.append(random.choice(all_characters))

    # Shuffle the list to hide any predictable patterns
    random.shuffle(password_chars)

    # Convert the list back into a single string
    return "".join(password_chars)


def run_cli():
    """Handles the user interface in the terminal."""
    print("=" * 50)
    print("   Custom Complexity Password Generator   ")
    print("=" * 50)
    
    # 1. Get Length
    while True:
        try:
            user_input = input("\nEnter the desired password length (e.g., 8, 16): ")
            length = int(user_input.strip())
            
            if length < 0:
                print(">> Error: Password length cannot be negative.")
                continue
            break
        except ValueError:
            print(">> Error: Please enter a valid whole number.")

    # 2. Get Complexity
    print("\nChoose Complexity Level:")
    print("  1 - Lowercase letters only")
    print("  2 - Lowercase & Uppercase letters")
    print("  3 - Letters & Numbers")
    print("  4 - Letters, Numbers, & Symbols")
    
    while True:
        try:
            comp_input = input("Enter complexity level (1-4): ")
            complexity = int(comp_input.strip())
            
            if complexity not in [1, 2, 3, 4]:
                print(">> Error: Please choose a level between 1 and 4.")
                continue
            break
        except ValueError:
            print(">> Error: Please enter a valid whole number (1, 2, 3, or 4).")

    # 3. Generate and Display
    final_password = generate_custom_password(length, complexity)
    
    print("\n" + "-" * 50)
    if length == 0:
        print("Generated Password: [Empty String]")
    else:
        print(f"Generated Password: {final_password}")
    print("-" * 50 + "\n")

if __name__ == "__main__":
    run_cli()