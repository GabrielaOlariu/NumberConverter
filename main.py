#develop these two functions

   
def introduce_developer():
    print("Hello, My name is Gabriela, I developed this program.")
    print("This application is called Number Converter.")

def welcome_user():
    print()
    print("Welcome!")
    introduce_developer()

def main_menu():
    print()
    print("This program offers the following options:")
    print("Option 1: reset app")
    print("Option 2: binary converter")
    print("Option 3: octal converter")
    print("Option 4: decimal converter")
    print("Option 5: hexadecimal converter")
    print("Option 6: exit app")

def choose_option():
    option = int(input("What option do you chose?"))
    match option:
        case 1:
            print("Reset app")
            start_program()
        case 2:
            print("binary converter")
        case 3:
            print("octal converter")
        case 4:
            print("decimal converter")
        case 5:
            print("hexadecimal converter")
        case 6:
            print("exit app")

def start_program():
    welcome_user()
    main_menu()
    choose_option()
    pass

start_program()
