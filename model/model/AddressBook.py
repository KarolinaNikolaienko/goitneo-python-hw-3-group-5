from collections import UserDict
from model.model.Record import Record
from model.decorators.input_error import input_error
from modules.birthdays import get_birthdays_per_week as birthdays

class AddressBook(UserDict):
    def add_record(self, record:Record):
        if self.data and (record.name.value.lower() in self.data): # self.find_record(record.name.value) != None
            self.data[record.name.value.lower()].add_phone(record.phones[0].value)
        else:
            self.data[record.name.value.lower()] = record
        return "Contact added"

    def find_record(self, name):
        return self.data.get(name.lower(), None)
    
    @input_error #Key error posible
    def delete_record(self, name): 
        return f"Contact {self.data.pop(name.lower()).name.value} was deleted from adress book"
    
    def show_all(self):
        if self.data:
            for record in self.data.values():
                print(record)
        else:
            print("The book is empty")
    
    @input_error
    def get_birthdays_per_week(self):
        if self.data:
            birthday_list = []
            for record in self.data.values():
                contact = {}
                contact["name"] = record.name.value
                contact["birthday"] = record.birthday.value
                birthday_list.append(contact)
            birthdays_next_week = birthdays(birthday_list).items()
            if not birthdays_next_week:
                print("There are no birthdays on the next week")
            else:
                for day, names in birthdays_next_week:
                    print(day + ': ' + ', '.join(names))
        else:
            print("The book is empty")