import re
from datetime import datetime
from model.model.Name import Name
from model.model.Phone import Phone
from model.model.Birthday import Birthday
from model.decorators.input_error import input_error
from model.model.errors import PhoneNumError, BirthdayError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    @input_error
    def add_phone(self, phone):
        if re.findall(r"^\d{10}$", phone):
            self.phones.append(Phone(phone))
        else:
            raise PhoneNumError
        #print("Phone was added")
    
    @input_error
    def edit_phone(self, old_phone, new_phone):
        changes = False
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.phones.insert(index, Phone(new_phone))
                changes = True
                print(f"Phone for {self.name.value} was changed")
        if not changes:
            print("No phone was found")
    
    @input_error
    def remove_phone(self, phone):
        changes = False
        for index, phone_ in enumerate(self.phones):
            if phone_.value == phone:
                self.phones.remove(phone_)
                changes = True
                print(f"Phone for {self.name.value} was deleted")
        if not changes:
            print("No phone was found")
    
    def find_phone(self, phone):
        found_phone = "No phone was found"
        for phone_ in self.phones:
            if phone_.value == phone:
                found_phone = phone_
                break
        return found_phone
    
    @input_error
    def add_birthday(self, birthday):
        if re.findall(r"^(?:0?[0-9]|[12][0-9]|3[12]).(?:0?[1-9]|1[12]).(?:\d{4})$", birthday) and datetime.strptime(birthday, "%d.%m.%Y").date() < datetime.now().date():
            self.birthday = Birthday(birthday)
            print("Birthday was added")
        else:
            raise BirthdayError
    
    def show_birthday(self):
        if self.birthday:
            print(f"{self.name.value}'s birthday is {datetime.strftime(self.birthday.value, "%d.%m.%Y")}")
        else:
            print(f"Birthday wasn't added for {self.name.value}")
    
    def __str__(self):
        return f"{self.name.value}\t{'; '.join(p.value for p in self.phones)}"
