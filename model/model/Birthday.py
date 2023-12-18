from model.model.Field import Field
from datetime import datetime, date

class Birthday(Field):
    def __init__(self, value):
        self.__value = value
        super().__init__(value)
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = datetime.strptime(value, "%d.%m.%Y").date()