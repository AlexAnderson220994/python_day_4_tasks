import os

# Use the echo command to print the input string to the terminal
def echo_string_to_terminal(input_string):
    os.system(f'echo {input_string}')

# Get user input for the string to be echoed using if function
if __name__ == "__main__":
    user_input = input("Enter a string to echo to the terminal: ")

    # Call the function to echo the string
    echo_string_to_terminal(user_input)