import re

commands = ["hello", "add", "change", "phone", "show all", "good bye", "close", "exit"]

phone_book = {"Masha": "380990000000"}


def input_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except KeyError as ex:
            error = f'\n\tEnter correct command, please.'
        except ValueError as ex:
            error = f'\n\tEnter the correct name or/and phone number.'
        except IndexError as ex:
            error = f'\n\tEnter correct , please.'
        return error

    return wrapper


def valid_phone(phone_number):
    if len(phone_number) == 12:
        phone_number = f'+{phone_number}'
    elif len(phone_number) == 10:
        phone_number = f'+38{phone_number}'
    else:
        raise ValueError
    return phone_number


def input_parser(input_command: str):
    raw_user_input = re.search(r'(?:^add\b|^change\b|^phone\b)', input_command)
    command = raw_user_input.group() if raw_user_input else False
    phone_number = ''.join(re.findall('\d+', input_command))
    input_list = input_command.strip().split(" ")
    if len(input_list) > 1:
        name = input_list[1].upper()
    else:
        raise ValueError
    return command, name, phone_number


@input_error
def handler_parser(command, name, number):
    if command == "add":
        return add_contact(name, number)
    if command == "change":
        return change_contact(name, number)
    if command == "phone":
        return find_contact_by_name(name)


def add_contact(name, number):
    if name in phone_book:
        return f'Contact {name} already in phone book\n'
    elif not name == False and not number == False:
        phone_book[name] = valid_phone(number)
        return f'New contact {name}: {number}> has been saved successfully\n'
    else:
        raise ValueError


def change_contact(name, number):
    if name in phone_book:
        phone_book[name] = number
        return f"{name} successfully updated"
    elif name == False in phone_book:
        return f'\n\tThere is no such contact <{name}> in phone book. Add contact as new one\n'
    else:
        raise ValueError


def find_contact_by_name(name):
    if name in phone_book:
        phone = phone_book.get(name)
        return f"{name}:{phone}"
    elif name == False in phone_book:
        return f'\n\tThere is no such contact <{name}> in phone book. Add contact as new one\n'
    else:
        raise ValueError


def main():
    while True:
        command = input("Waiting for your command:\n")
        command = command.casefold()
        if command == "hello":
            print("Hello! How can I help you?")
        elif command == "show all":
            print(phone_book)
        elif command == "good bye" or command == "close" or command == "exit":
            print("Bye!\n")
            break
        else:
            command, name, number = input_parser(command)
            print(handler_parser(command, name, number))


if __name__ == '__main__':
    main()
