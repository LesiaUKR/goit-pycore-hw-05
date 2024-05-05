from decorators import *


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(contacts,  name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact {name} isn't found. You can add it by 'add' command."


@input_error
def show_phone(contacts,  name):
    if name in contacts:
        print(f"{name} phone is {contacts[name]}")
    else:
        print(f"Contact {name} isn't found.")


def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Set command (add, hello, change, phone, all, exit):")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(contacts, *args))
        elif command == "phone":
            print(show_phone(contacts, args[0]))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command or arguments.")


if __name__ == "__main__":
    main()
