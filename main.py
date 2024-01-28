from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)
        
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    # реалізація класу
        
    def add_phone(self, phone: str):
        phone = Phone(phone)
        if phone not in self.phones:
            self.phones.append(phone)

    def remove_phone(self, phone: str):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)

    def edit_phone(self, phone: str, new_phone):
        new_phone = Phone(new_phone)
        for i in self.phones:
            if i.value == phone:
                i.value = new_phone.value
                return          
        raise ValueError
                
    def find_phone(self, phone: str):
        for i in self.phones:
            if i.value == phone:
                return i
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        if record not in self.data:
            self.data[record.name.value] = record

    def find(self, record):
        return self.data.get(record, None)

    def delete(self, record):
        try:
            del self.data[record]
        except KeyError:
            print('Contact not found')


