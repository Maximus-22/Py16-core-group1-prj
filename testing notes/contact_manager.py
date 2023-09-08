import json
import re
from datetime import datetime, timedelta

class ContactManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_path, 'r') as file:
                contacts = json.load(file)
            return contacts
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def validate_phone(self, phone):
        phone_pattern = re.compile(r'^\+380\d{9}$')
        return bool(phone_pattern.match(phone))

    def validate_email(self, email):
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+(\.\w+)+$')
        return bool(email_pattern.match(email))

    def add_contact(self, name, address, phone, email, birthday):
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number format.")
        
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        
        contact = {
            "name": name,
            "address": address,
            "phone": phone,
            "email": email,
            "birthday": birthday
        }
        
        self.contacts.append(contact)
        self.save_contacts()

    def edit_contact(self, phone, name=None, address=None, email=None, birthday=None):
        for contact in self.contacts:
            if contact["phone"] == phone:
                if name is not None:
                    contact["name"] = name
                if address is not None:
                    contact["address"] = address
                if email is not None and self.validate_email(email):
                    contact["email"] = email
                if birthday is not None:
                    contact["birthday"] = birthday

        self.save_contacts()

    def delete_contact(self, phone):
        self.contacts = [contact for contact in self.contacts if contact["phone"] != phone]
        self.save_contacts()

    def get_upcoming_birthday_contacts(self, days):
        today = datetime.now()
        upcoming_birthday_contacts = []

        for contact in self.contacts:
            birthday = datetime.strptime(contact["birthday"], "%Y-%m-%d")
            next_birthday = birthday.replace(year=today.year)

            if today > next_birthday:
                next_birthday = next_birthday.replace(year=today.year + 1)

            days_until_birthday = (next_birthday - today).days
            if 0 <= days_until_birthday <= days:
                upcoming_birthday_contacts.append(contact)

        return upcoming_birthday_contacts

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if (
                query.lower() in contact["name"].lower()
                or query.lower() in contact["address"].lower()
                or query.lower() in contact["phone"].lower()
                or query.lower() in contact["email"].lower()
            ):
                results.append(contact)
        return results

if __name__ == "__main__":
    manager = ContactManager("contacts.json")