import json
import re
from datetime import datetime
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number")
        super().__init__(value)

    @staticmethod
    def validate_phone(value):
        return value.isdigit() and len(value) == 10

    def __str__(self):
        return self.value

class Email(Field):
    def __init__(self, value):
        if not self.validate_email(value):
            raise ValueError("Invalid email")
        super().__init__(value)

    @staticmethod
    def validate_email(value):
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+(\.\w+)+$')
        return bool(email_pattern.match(value))

    def __str__(self):
        return self.value

class Name(Field):
    def __str__(self):
        return self.value

class Address(Field):
    def __str__(self):
        return self.value

class Birthday(Field):
    def __init__(self, value):
        if not self.validate_birthday(value):
            raise ValueError("Invalid birthday")
        super().__init__(value)

    @staticmethod
    def validate_birthday(value):
        return isinstance(value, datetime) and value <= datetime.now()

    def __str__(self):
        return self.value.strftime('%Y-%m-%d')

class Record:
    def __init__(self, name: Name, address: Address, phones: list, emails: list=None, birthday: Birthday=None):
        self.name = str(name)
        self.address = str(address)
        self.phones = [str(phone) for phone in phones]
        self.emails = [str(email) for email in emails] if emails else []
        self.birthday = str(birthday) if birthday else None

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def delete_phone(self, phone):
        new_phones = [p for p in self.phones if p.value != phone]
        self.phones = new_phones

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def days_to_birthday(self):
        if not self.birthday:
            return None

        today = datetime.now().date()
        next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day).date()

        if today > next_birthday:
            next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day).date()

        days_left = (next_birthday - today).days
        return days_left

    def __str__(self):
        result = f"Name: {self.name}\n"
        result += f"Address: {self.address}\n"
        result += "Phones:\n"
        for phone in self.phones:
            result += f"  {phone}\n"
        result += "Emails:\n"
        for email in self.emails:
            result += f"  {email}\n"
        if self.birthday:
            result += f"Birthday: {self.birthday}\n"
        result += "-" * 30
        return result

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name] = record

    def iterator(self):
        return self.data.values()

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            data = {
                "records": [record.__dict__ for record in self.values()]
            }
            json.dump(data, file, indent=4)

    @classmethod
    def load_from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                book = cls()
                for record_data in data["records"]:
                    name = Name(record_data["name"])
                    address = Address(record_data["address"])
                    phones = [Phone(phone) for phone in record_data["phones"]]
                    emails = [Email(email) for email in record_data["emails"]]
                    birthday = Birthday(datetime.strptime(record_data["birthday"], "%Y-%m-%d")) if record_data["birthday"] else None
                    record = Record(name, address, phones, emails, birthday)
                    book.add_record(record)
                return book
        except FileNotFoundError:
            return cls()

    def search_records(self, query):
        query = query.lower()
        found_records = []
        for record in self.data.values():
            if query in record.name.lower():
                found_records.append(record)
            for phone in record.phones:
                if query in phone.lower():
                    found_records.append(record)
            for email in record.emails:
                if query in email.lower():
                    found_records.append(record)
        return found_records

if __name__ == "__main__":
    book = AddressBook()

    while True:
        print("Address Book Menu:")
        print("1. Add a Contact")
        print("2. Edit a Contact")
        print("3. Delete a Contact")
        print("4. List All Contacts")
        print("5. Save Address Book")
        print("6. Load Address Book")
        print("7. Search Contacts")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            while True:
                name = input("Enter the contact's name: ")
                address = input("Enter the contact's address: ")
                phone = input("Enter the contact's phone number: ")
                email = input("Enter the contact's email address: ")
                birthday = input("Enter the contact's birthday (YYYY-MM-DD): ")
                
                try:
                    name_field = Name(name)
                    address_field = Address(address)
                    phone_field = Phone(phone)
                    email_field = Email(email)
                    birthday_field = Birthday(datetime.strptime(birthday, "%Y-%m-%d"))
                    record = Record(name_field, address_field, [phone_field], [email_field], birthday_field)
                    book.add_record(record)
                    print(f"Contact {name} added successfully!")
                    break
                except ValueError as e:
                    print(f"Error: {e}")
                    print("Please enter valid data.")

        elif choice == "2":
            name = input("Enter the contact's name to edit: ")
            if name in book.data:
                record = book.data[name]
                print(f"Editing Contact: {record.name}")
                print("1. Edit Name")
                print("2. Edit Address")
                print("3. Edit Phone")
                print("4. Edit Email")
                print("5. Edit Birthday")
                edit_choice = input("Enter your choice (1/2/3/4/5): ")

                if edit_choice == "1":
                    while True:
                        new_name = input("Enter the new name: ")
                        try:
                            record.name = new_name
                            print(f"Contact {name} name updated to {new_name}")
                            break
                        except ValueError as e:
                            print(f"Error: {e}")
                            print("Please enter a valid name.")

                elif edit_choice == "2":
                    while True:
                        new_address = input("Enter the new address: ")
                        try:
                            record.address = new_address
                            print(f"Address updated for {record.name}")
                            break
                        except ValueError as e:
                            print(f"Error: {e}")
                            print("Please enter a valid address.")

                elif edit_choice == "3":
                    old_phone = input("Enter the old phone number: ")
                    while True:
                        new_phone = input("Enter the new phone number: ")
                        try:
                            record.edit_phone(old_phone, new_phone)
                            print(f"Phone number updated for {record.name}")
                            break
                        except ValueError as e:
                            print(f"Error: {e}")
                            print("Please enter a valid phone number.")

                elif edit_choice == "4":
                    while True:
                        new_email = input("Enter the new email address: ")
                        try:
                            record.emails[0] = new_email
                            print(f"Email address updated for {record.name}")
                            break
                        except ValueError as e:
                            print(f"Error: {e}")
                            print("Please enter a valid email address.")

                elif edit_choice == "5":
                    while True:
                        new_birthday = input("Enter the new birthday (YYYY-MM-DD): ")
                        try:
                            record.birthday = new_birthday
                            print(f"Birthday updated for {record.name}")
                            break
                        except ValueError as e:
                            print(f"Error: {e}")
                            print("Please enter a valid birthday (YYYY-MM-DD).")

        elif choice == "3":
            name = input("Enter the contact's name to delete: ")
            if name in book.data:
                del book.data[name]
                print(f"Contact {name} deleted successfully!")

        elif choice == "4":
            print("List of All Contacts:")
            for record in book.data.values():
                print(record)  # Используем метод __str__ для вывода контакта
                print("-" * 30)

        elif choice == "5":
            filename = input("Enter the filename to save the address book (address_book.json): ")
            book.save_to_file(filename)
            print(f"Address book saved to {filename} successfully!")

        elif choice == "6":
            filename = input("Enter the filename to load the address book from (address_book.json): ")
            book = AddressBook.load_from_file(filename)
            print(f"Address book loaded from {filename} successfully!")

        elif choice == "7":
            search_query = input("Enter the search query: ")
            found_records = book.search_records(search_query)
            if found_records:
                print("Search results:")
                for record in found_records:
                    print(record)  # Используем метод __str__ для вывода контакта
                    print("-" * 30)
            else:
                print("No matching records found.")

        elif choice == "8":
            print("Exiting the Address Book program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid choice (1/2/3/4/5/6/7/8).")
