def parse_input(user_input):
    # Розділяємо введений рядок на команду та аргументи
    cmd, *args = user_input.split()
    # Перетворення команди до нижнього регістру
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    # Перевірка чи користувач передав два аргументи: ім'я та номер телефону
    if len(args) != 2:
        return "Invalid command. Please provide username and phone number separated by space."
    username, phone = args
    # Додаємо новий контакт до словника контактів
    contacts[username] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide username and new phone number separated by space."
    username, new_phone = args
    # Перевірка, чи ім'я користувача існує у словнику контактів
    if username not in contacts:
        return "Contact not found."
    contacts[username] = new_phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Please provide username."
    username = args[0]
    if username not in contacts:
        return "Contact not found."
    return contacts[username]

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = "\n".join([f"{username}: {phone}" for username, phone in contacts.items()])
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        # Очікуємо введення команди користувачем
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        # Перевіряє, чи введена команда є однією з команд завершення роботи
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # Відповідаємо на команди
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
