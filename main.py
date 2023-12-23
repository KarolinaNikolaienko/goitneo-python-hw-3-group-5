from model.model.AddressBook import AddressBook
from model.model.Record import Record
from modules.parse_input import parse_input


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        command = parse_input(input("Enter a command: ").strip().lower())

        try:
            if command[0] in ["close", "exit", "bye", "goodbye"]:
                print("Good bye!")
                break

            elif command[0] in ["hello", "hi"]:
                print("How can I help you?")
            
            elif command[0] == "add":
                if len(command) != 3:
                    print("To ADD contact give me <name> <phone> please")
                else:
                    record = Record(command[1])
                    if record.add_phone(command[2]) != False:
                        print(book.add_record(record))
            elif command[0] == "change":
                if len(command) != 4:
                    print("To CHANGE contact give me <name> <old phone> <new phone> please")
                else:
                    found_record = book.find_record(command[1])
                    if not found_record:
                        print("Contact wasn't found")
                    else:
                        found_record.edit_phone(command[2], command[3])
            elif command[0] == "phone":
                if len(command) != 2:
                    print("To show PHONE give me <name> please")
                else:
                    found_record = book.find_record(command[1])
                    if not found_record:
                        print("Contact wasn't found")
                    else:
                        print(found_record)
            elif command[0] == "all":
                book.show_all()
            
            elif command[0] == "add-birthday":
                if len(command) != 3:
                    print("To ADD BIRTHDAY give me <name> <DD.MM.YYYY> please")
                else:
                    found_record = book.find_record(command[1])
                    if not found_record:
                        print("Contact wasn't found")
                    else:
                        found_record.add_birthday(command[2])
            elif command[0] == "show-birthday":
                if len(command) != 2:
                    print("To SHOW BIRTHDAY give me <name> please")
                else:
                    found_record = book.find_record(command[1])
                    if not found_record:
                        print("Contact wasn't found")
                    else:
                        found_record.show_birthday()
            elif command[0] == "birthdays":
                book.get_birthdays_per_week()
            
            else:
                print("Invalid command")
            
        except Exception as error:
            pass
            #print(error)

if __name__ == "__main__":
    main()