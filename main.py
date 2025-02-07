#develop these two functions

   
def introduce_developer():
    print("Hello, My name is Gabriela, I developed this program.")
    print("This application is called Number Converter.")

def welcome_user():
    print("Welcome!")
    introduce_developer()

def main_menu():
    print("Option 1: reset app")
    print("Option 2: binary converter")
    print("Option 3: octal converter")
    print("Option 4: decimal converter")
    print("Option 5: hexadecimal converter")
    print("Option 6: exit app")

def start_program():
    welcome_user()
    main_menu()
    pass

start_program()
