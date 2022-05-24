import calendar

commands = ["hello", "add ...", "change ...", "phone ...", "show all", "good bye", "close", "exit"]

phone_book = {"Masha": "+380976567654", "Sasha": "+380937236707"}


def command_parser(input_command: str):
    input_list = input_command.split(" ")
    command = input_list[0]
    if command == "add":
        add_contact(input_list[1], input_list[2])
    if command == "change":
        change_contact(input_list[1], input_list[2])
    if command == "phone":
        find_contact_by_name(input_list[1])


def add_contact(name, number):
    phone_book[name] = number


def change_contact(name, number):
    phone_book[name] = number


def find_contact_by_name(name):
    phone = phone_book.get(name)
    print(f"{phone}")


def main():
    while True:
        command = input("Waiting for your command:")
        command = command.lower()
        if command == "hello":
            print("Hello! How can I help you?")
        if command == "show all":
            print(phone_book)
        if command == "good bye" or command == "close" or command == "exit":
            print("Bye!")
            break

        command_parser(command)


if __name__ == '__main__':
    main()
