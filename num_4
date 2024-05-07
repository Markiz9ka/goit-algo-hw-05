def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
    return inner


def input_error2(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and new phone."
    return inner

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

@input_error2
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone 
        return 'Contact updated.'
    else:
        return 'Name not found.'
  
def show_phone(name, contacts):
    phone = contacts.get(name)
    if phone:
        return f"Phone number for {name}: {phone}"
    else:
        return f"Contact {name} not found."
    
def main():
    global contacts
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            print(contacts)
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            if args:
                print(show_phone(args[0], contacts))
            else:
                print("Please provide a name to lookup the phone number.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
