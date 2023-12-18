from model.model.Field import Field

class Name(Field):
    def __init__(self, value):
        self.__value = value
        super().__init__(value)
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = str(value).capitalize()