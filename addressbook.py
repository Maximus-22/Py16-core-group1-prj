import json
import re
from datetime import datetime
from prettytable import PrettyTable
from collections import UserDict
from colorama import Fore, Style

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
        # Check the format +38-000-0000000 or +380000000000
        if re.match(r'^\+\d{2}-\d{3}-\d{7}$', value) or re.match(r'^\+\d{12}$', value):
            return True

        # Check the format 000-0000000 or 0000000000
        if re.match(r'^\d{3}-\d{7}$', value) or re.match(r'^\d{10}$', value):
            return True

        # If none of the above formats match, return False
        return False


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
        self.phones = self.process_phones(phones)
        self.emails = [str(email) for email in emails] if emails else []
        self.birthday = birthday

    def process_phones(self, phones):
        processed_phones = []
        for phone_field in phones:
            phone = str(phone_field)
            phone_numbers = re.split(r'[,\s]+', phone)
            for phone_number in phone_numbers:
                if Phone.validate_phone(phone_number):
                    processed_phones.append(str(Phone(phone_number)))
                else:
                    raise ValueError(f"Error: Invalid phone number: {phone_number}")
        return processed_phones

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def delete_phone(self, phone):
        new_phones = [p for p in self.phones if p.value != phone]
        self.phones = new_phones

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if isinstance(phone, Phone) and phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                # Оновлення телефонів у списку об'єкта Record
                self.update_record_phones()
                break

    def update_record_phones(self):
        # Оновлюємо список телефонів об'єкта Record
        self.phones = [str(phone) for phone in self.phones]




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
        result += f"Phones: {', '.join(self.phones)}\n"
        result += f"Emails: {', '.join(self.emails)}\n"
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
            # Serialize birthdays to strings
            for record_data in data["records"]:
                if record_data["birthday"]:
                    record_data["birthday"] = record_data["birthday"].value.strftime('%Y-%m-%d')
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
        found_record_names = set()  

        for record in self.data.values():
            if query in record.name.lower() and record.name not in found_record_names:
                found_records.append(record)
                found_record_names.add(record.name)

            for phone in record.phones:
                if query in phone.lower() and record.name not in found_record_names:
                    found_records.append(record)
                    found_record_names.add(record.name)

            for email in record.emails:
                if query in email.lower() and record.name not in found_record_names:
                    found_records.append(record)
                    found_record_names.add(record.name)

        return found_records


    def get_upcoming_birthday_contacts(self, days):
        today = datetime.now().date()
        upcoming_birthday_contacts = []

        for record in self.data.values():
            if record.birthday:
                if isinstance(record.birthday, str):
                    # If birthday is loaded as a string, parse it
                    record.birthday = Birthday(datetime.strptime(record.birthday, "%Y-%m-%d"))

                next_birthday = datetime(today.year, record.birthday.value.month, record.birthday.value.day).date()
                if today > next_birthday:
                    next_birthday = datetime(today.year + 1, record.birthday.value.month, record.birthday.value.day).date()
                days_left = (next_birthday - today).days

                if days_left == days:
                    upcoming_birthday_contacts.append(record)

        return upcoming_birthday_contacts


if __name__ == "__main__":
    book = AddressBook()

    while True:
        menu = PrettyTable()
        menu.field_names = [Fore.BLUE + "Option", Fore.BLUE + "Description"]

        menu.add_row(["1", "Add a Contact"])
        menu.add_row(["2", "Edit a Contact"])
        menu.add_row(["3", "Delete a Contact"])
        menu.add_row(["4", "List All Contacts"])
        menu.add_row(["5", "Save Address Book"])
        menu.add_row(["6", "Load Address Book"])
        menu.add_row(["7", "Search Contacts"])
        menu.add_row(["8", "View Upcoming Birthdays"])
        menu.add_row(["9", "Exit"])

        print(Fore.BLUE + "Address Book Menu:")
        print(menu)

        choice = input(Fore.YELLOW + "Enter your choice (1/2/3/4/5/6/7/8/9): " + Style.RESET_ALL)

        if choice == "1":
            while True:
                print("Enter contact details (or enter '0' to exit):")
                name = input("Enter the contact's name: ")
                if name == '0':
                    break

                address = input("Enter the contact's address: ")
                phone = input("Enter the contact's phone number: ")
                email = input("Enter the contact's email address: ")
                birthday = input("Enter the contact's birthday (YYYY-MM-DD): ")

                if name and address and phone and email and birthday:
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
                else:
                    print("All fields are required. Please try again or enter '0' to cancel.")

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
                            record.birthday = Birthday(datetime.strptime(new_birthday, "%Y-%m-%d"))
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
                print(record)
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
            query = input("Enter a search query: ")
            found_records = book.search_records(query)
            if found_records:
                print("Search Results:")
                for record in found_records:
                    print(record)
                    print("-" * 30)
            else:
                print("No matching records found.")

        elif choice == "8":
            days = int(input("Enter the number of days for upcoming birthdays: "))
            upcoming_birthday_contacts = book.get_upcoming_birthday_contacts(days)
            if upcoming_birthday_contacts:
                print(f"Upcoming Birthdays in {days} days:")
                for record in upcoming_birthday_contacts:
                    print(record)
                    print("-" * 30)
            else:
                print("No upcoming birthdays found.")

        elif choice == "9":
            print("Exiting the Address Book program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid choice (1/2/3/4/5/6/7/8/9).")