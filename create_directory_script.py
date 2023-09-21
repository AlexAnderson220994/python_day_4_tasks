import os


# Use os.mkdir to create the directory
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get user input for the directory name
if __name__ == "__main__":
    directory_name = input("Enter the name of the directory you want to create: ")

    # Call the function to create the directory
    create_directory(directory_name)