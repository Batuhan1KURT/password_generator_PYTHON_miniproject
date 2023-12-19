
import random
import string
from sys import exit

# Define character lists using string module constants
number_list = string.digits
special_char_list = string.punctuation
lower_case_char = string.ascii_lowercase
upper_case_char = string.ascii_uppercase

# Function to determine the password options based on user input
def password_selection(enter):
    options = {
        1: [number_list],
        2: [number_list, lower_case_char],
        3: [number_list, upper_case_char],
        4: [number_list, lower_case_char, upper_case_char],
        5: [number_list, lower_case_char, upper_case_char, special_char_list],
    }
    return options.get(enter, [])

# Function to generate a random password
def randomiser():
    # Display menu for password options
    print("1: Only Numbers")
    print("2: Numbers and Lower Case Characters")
    print("3: Numbers and Upper Case Characters")
    print("4: Numbers, Lower and Upper Case Characters")
    print("5: Numbers, Lower and Upper Case Characters and Special Characters")
    
    # Get user input for password option and length
    user_selection = int(input("Enter your choice: "))
    print("")
    password_length = int(input("How long do you want your password: "))
    
    # Check if user input is within the valid range
    if not (1 <= user_selection <= 5):
        print("Unexpected input, ERROR!")
        exit()

    # Generate password by choosing characters randomly from selected options
    created_password = "".join(random.choice(password_selection(user_selection)) for _ in range(password_length))
    
    # Display the generated password
    print(created_password)

# Main function to initiate password generation
def main():
    randomiser()

# Check if the script is run as the main program
if __name__ == "__main__":
    main()
