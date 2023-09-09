import os, subprocess, sys
from colorama import Fore, Style
from datetime import datetime, timedelta
from prettytable import PrettyTable
from config_addressbook import Address, AddressBook, Birthday, Email, Name, Phone, Record
from config_notes import NoteManager
import main_cleaner as folder_cleaner
import main_minicalc

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


# SECTION BASE MENU
def main_menu():
    while True:
        clear_screen()
        print("+" + "-" * 50 + "+")
        print("Welcome to your Personal Assistant!\n")
        print("1. Contacts")
        print("2. Notes")
        print("3. Sorting files")
        print("4. Mini Calculator")
        print("5. Game BanderoGoose")
        print("6. Quit\n")
        print("+" + "-" * 50 + "+\n")

        choice = input("Select an option [1 / 2 / 3 / 4 / 5 / 6]: ")

        if choice == "1":
            contacts_menu()
        elif choice == "2":
            notes_menu()
        elif choice == "3":
            files_menu()
        elif choice == "4":
            clear_screen()
            main_minicalc.main()
            input("Press Enter to continue.")
        elif choice == "5":
            try:
                script_name = "main_banderogoose.py"
                subprocess.run(["python", script_name], check = True)
            except subprocess.CalledProcessError:
                print(f"An error occurred while executing the script {script_name}.")
        elif choice == "6":
            sys.exit()
        else:
            input("Incorrect choice. Press Enter to continue.")


# SECTION OF CONTACTS
def contacts_menu():
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


# SECTION OF NOTES
def notes_menu():
    note_manager = NoteManager("notes.json")

    while True:
        clear_screen()
        print("Нотатки")
        print("1. Додати нотатку")
        print("2. Редагувати нотатку")
        print("3. Видалити нотатку")
        print("4. Пошук нотаток")
        print("5. Сортувати нотатки за тегами")
        print("6. Назад")

        choice = input("Оберіть опцію (1/2/3/4/5/6): ")

        if choice == "1":
            add_note(note_manager)
        elif choice == "2":
            edit_note(note_manager)
        elif choice == "3":
            delete_note(note_manager)
        elif choice == "4":
            search_notes(note_manager)
        elif choice == "5":
            sort_notes_by_tags(note_manager)
        elif choice == "6":
            return
        else:
            input("Некоректний вибір. Натисніть Enter для продовження.")

def add_note(note_manager):
    clear_screen()
    print("Додати нотатку")
    title = input("Заголовок: ")
    body = input("Тіло нотатки: ")
    tags = input("Теги (через кому): ").split(',')

    note_manager.add_note(title, body, tags)
    input("Нотатку успішно додано. Натисніть Enter для продовження.")

def edit_note(note_manager):
    clear_screen()
    print("Редагувати нотатку")
    title = input("Введіть заголовок нотатки для редагування: ")
    note = note_manager.search_notes(title)

    if note:
        print("Поточні дані:")
        print(f"Заголовок: {note['title']}")
        print(f"Тіло нотатки: {note['body']}")
        print(f"Теги: {', '.join(note['tags'])}")

        new_title = input("Новий заголовок (або Enter для збереження поточного): ")
        new_body = input("Нове тіло нотатки (або Enter для збереження поточного): ")
        new_tags = input("Нові теги (через кому) (або Enter для збереження поточних): ").split(',')

        note_manager.edit_note(title, new_title, new_body, new_tags)
        input("Нотатку успішно відредаговано. Натисніть Enter для продовження.")
    else:
        input("Нотатка з таким заголовком не знайдена. Натисніть Enter для продовження.")

def delete_note(note_manager):
    clear_screen()
    print("Видалити нотатку")
    title = input("Введіть заголовок нотатки для видалення: ")
    note = note_manager.search_notes(title)

    if note:
        print("Дані нотатки:")
        print(f"Заголовок: {note['title']}")
        print(f"Тіло нотатки: {note['body']}")
        print(f"Теги: {', '.join(note['tags'])}")

        confirmation = input("Ви впевнені, що хочете видалити цю нотатку? (Так/Ні): ")

        if confirmation.lower() == "так":
            note_manager.delete_note(title)
            input("Нотатку успішно видалено. Натисніть Enter для продовження.")
    else:
        input("Нотатка з таким заголовком не знайдена. Натисніть Enter для продовження.")

def search_notes(note_manager):
    clear_screen()
    print("Пошук нотаток")
    query = input("Введіть пошуковий запит (заголовок або теги): ")
    results = note_manager.search_notes(query)

    if results:
        print("Результати пошуку:")
        for i, note in enumerate(results, start=1):
            print(f"{i}. Заголовок: {note['title']}")
            print(f"   Тіло: {note['body']}")
            print(f"   Теги: {', '.join(note['tags'])}")

        input("Натисніть Enter для продовження.")
    else:
        input("За вашим запитом не знайдено жодної нотатки. Натисніть Enter для продовження.")

def sort_notes_by_tags(note_manager):
    clear_screen()
    print("Сортування нотаток за тегами")
    tag = input("Введіть тег для сортування нотаток: ")
    sorted_notes = note_manager.sort_notes_by_tags(tag)

    if sorted_notes:
        print(f"Відсортовані нотатки за тегом '{tag}':")
        for i, note in enumerate(sorted_notes, start=1):
            print(f"{i}. {note['title']} - {note['body']} ({', '.join(note['tags'])})")

        input("Натисніть Enter для продовження.")
    else:
        input(f"Нотатки з тегом '{tag}' не знайдені. Натисніть Enter для продовження.")


# SECTION OF CLEAN FOLDER
def files_menu():

    while True:
        clear_screen()
        print("The script will help to sort the files in the specified folder by their extension by categories.")
        print("1. Sort files by category")
        print("2. Quit")

        choice = input("Select an option [1 / 2]: ")

        if choice == "1":
            folder_path = input("Enter the folder to sort (preferably in the working folder): ")
            folder_cleaner.main(folder_path)
            input("Files have been successfully sorted by category. Press Enter to continue.")
        elif choice == "2":
            return
        else:
            input("Incorrect choice. Press Enter to continue.")



if __name__ == "__main__":
    main_menu()
