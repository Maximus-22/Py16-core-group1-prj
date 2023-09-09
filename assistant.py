import os
import sys
from datetime import datetime, timedelta
# from contact_manager import ContactManager
from note_manager import NoteManager
# from file_manager import FileManager

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def main_menu():
    while True:
        clear_screen()
        print("Вітаємо у вашому Персональному Помічнику!")
        print("1. Контакти")
        print("2. Нотатки")
        print("3. Файли")
        print("4. Вихід")

        choice = input("Оберіть опцію (1/2/3/4): ")

        if choice == "1":
            contacts_menu()
        elif choice == "2":
            notes_menu()
        elif choice == "3":
            files_menu()
        elif choice == "4":
            sys.exit()
        else:
            input("Некоректний вибір. Натисніть Enter для продовження.")

# def contacts_menu():
#     contact_manager = ContactManager("contacts.json")

#     while True:
#         clear_screen()
#         print("Контакти")
#         print("1. Додати контакт")
#         print("2. Редагувати контакт")
#         print("3. Видалити контакт")
#         print("4. Пошук контактів")
#         print("5. День народження")
#         print("6. Назад")

#         choice = input("Оберіть опцію (1/2/3/4/5/6): ")

#         if choice == "1":
#             add_contact(contact_manager)
#         elif choice == "2":
#             edit_contact(contact_manager)
#         elif choice == "3":
#             delete_contact(contact_manager)
#         elif choice == "4":
#             search_contacts(contact_manager)
#         elif choice == "5":
#             upcoming_birthdays(contact_manager)
#         elif choice == "6":
#             return
#         else:
#             input("Некоректний вибір. Натисніть Enter для продовження.")

# def add_contact(contact_manager):
#     clear_screen()
#     print("Додати контакт")
#     name = input("Ім'я: ")
#     address = input("Адреса: ")
#     phone = input("Номер телефону: ")
#     email = input("Email: ")
#     birthday = input("День народження (рррр-мм-дд): ")

#     try:
#         contact_manager.add_contact(name, address, phone, email, birthday)
#         input("Контакт успішно додано. Натисніть Enter для продовження.")
#     except ValueError as e:
#         input(f"Помилка: {e}. Натисніть Enter для продовження.")

# def edit_contact(contact_manager):
#     clear_screen()
#     print("Редагувати контакт")
#     phone = input("Введіть номер телефону контакта для редагування: ")
#     contact = contact_manager.get_contact(phone)

#     if contact:
#         print("Поточні дані:")
#         print(f"Ім'я: {contact['name']}")
#         print(f"Адреса: {contact['address']}")
#         print(f"Номер телефону: {contact['phone']}")
#         print(f"Email: {contact['email']}")
#         print(f"День народження: {contact['birthday']}")

#         name = input("Нове ім'я (або Enter для збереження поточного): ")
#         address = input("Нова адреса (або Enter для збереження поточної): ")
#         email = input("Новий email (або Enter для збереження поточного): ")
#         birthday = input("Новий день народження (рррр-мм-дд) (або Enter для збереження поточного): ")

#         try:
#             contact_manager.edit_contact(phone, name, address, email, birthday)
#             input("Контакт успішно відредаговано. Натисніть Enter для продовження.")
#         except ValueError as e:
#             input(f"Помилка: {e}. Натисніть Enter для продовження.")
#     else:
#         input("Контакт з таким номером телефону не існує. Натисніть Enter для продовження.")

# def delete_contact(contact_manager):
#     clear_screen()
#     print("Видалити контакт")
#     phone = input("Введіть номер телефону контакта для видалення: ")
#     contact = contact_manager.get_contact(phone)

#     if contact:
#         print("Дані контакту:")
#         print(f"Ім'я: {contact['name']}")
#         print(f"Адреса: {contact['address']}")
#         print(f"Номер телефону: {contact['phone']}")
#         print(f"Email: {contact['email']}")
#         print(f"День народження: {contact['birthday']}")

#         confirmation = input("Ви впевнені, що хочете видалити цей контакт? (Так/Ні): ")

#         if confirmation.lower() == "так":
#             contact_manager.delete_contact(phone)
#             input("Контакт успішно видалено. Натисніть Enter для продовження.")
#     else:
#         input("Контакт з таким номером телефону не існує. Натисніть Enter для продовження.")

# def search_contacts(contact_manager):
#     clear_screen()
#     print("Пошук контактів")
#     query = input("Введіть пошуковий запит (ім'я, email або номер телефону): ")
#     results = contact_manager.search_contacts(query)

#     if results:
#         print("Результати пошуку:")
#         for i, contact in enumerate(results, start=1):
#             print(f"{i}. {contact['name']} ({contact['phone']}) - {contact['email']}")

#         input("Натисніть Enter для продовження.")
#     else:
#         input("За вашим запитом не знайдено жодного контакту. Натисніть Enter для продовження.")

# def upcoming_birthdays(contact_manager):
#     clear_screen()
#     print("Дні народження")
#     days = int(input("Введіть кількість днів для пошуку близьких днів народження: "))

#     today = datetime.now()
#     upcoming_date = today + timedelta(days=days)
#     upcoming_birthday_contacts = contact_manager.get_upcoming_birthday_contacts(days)

#     if upcoming_birthday_contacts:
#         print(f"Контакти з близькими днями народження (через {days} днів):")
#         for contact in upcoming_birthday_contacts:
#             birthday_date = datetime.strptime(contact['birthday'], "%Y-%m-%d")
#             days_until_birthday = (birthday_date - today).days
#             print(f"{contact['name']} ({contact['phone']}) - {contact['birthday']} (через {days_until_birthday} днів)")

#         input("Натисніть Enter для продовження.")
#     else:
#         input("На жаль, за заданий період близьких днів народження не знайдено. Натисніть Enter для продовження.")




########################################################        BLOCK NOTES     ##############################################################################



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
        print("6. Показати всі нотатки")
        print("7. Видалити всі нотатки")
        print("8. Назад")

        choice = input("Оберіть опцію (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            add_note(note_manager)
        elif choice == "2":
            edit_note(note_manager)
        elif choice == "3":
            delete_note(note_manager)
        elif choice == "4":
            search_notes(note_manager)
        elif choice == "5":
            tags_input = input("Введіть теги (через кому) для сортування: ")
            tags = [tag.strip() for tag in tags_input.split(',')]
            sort_notes_by_tags(note_manager, tags)
        elif choice == "6":
            show_all_notes(note_manager)
        elif choice == "7":
            clear_all_notes(note_manager)
        elif choice == "8":
            return
        else:
            input("Некоректний вибір. Натисніть Enter для продовження.")

def add_note(note_manager):
    clear_screen()
    print("Додати нотатку")
    title = input("Заголовок: ")
    body = input("Тіло нотатки: ")
    if not body:
        input("Поле 'Тіло нотатки' не може бути пустим. Натисніть Enter для продовження.")
        return
    tags = input("Теги (через кому): ").split(',')

    note_manager.add_note(title, body, tags)
    input("Нотатку успішно додано. Натисніть Enter для продовження.")

def edit_note(note_manager):
    clear_screen()
    print("Редагувати нотатку")
    title = input("Введіть заголовок нотатки для редагування: ")

    if not title:
        input("Ви нічого не ввели, будь ласка спробуйте ще. Натисніть Enter для продовження.")
        return
    
    note = note_manager.search_notes(title)

    if note:
        note = note[0]

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
    if not title:
        input("Поле 'Заголовок нотатки' не може бути пустим. Натисніть Enter для продовження.")
        return
    notes = note_manager.search_notes(title)

    if notes:
        note = notes[0]
        print("Дані нотатки:")
        print(f"Заголовок: {note['title']}")
        print(f"Тіло нотатки: {note['body']}")
        print(f"Теги: {', '.join(note['tags'])}")

        confirmation = input(f"Ви впевнені, що хочете видалити нотатку '{note['title']}'? (Так/Ні): ")
        if confirmation.lower() == "так":
            note_manager.delete_note(note['title'])
            input("Нотатку успішно видалено. Натисніть Enter для продовження.")
        elif confirmation.lower() == "ні":
            input("Видалення нотатки скасовано. Натисніть Enter для продовження.")
    else:
        input("Нотатка з таким заголовком не знайдена. Натисніть Enter для продовження.")

def search_notes(note_manager):
    clear_screen()
    print("Пошук нотаток")
    query = input("Введіть пошуковий запит (заголовок або теги): ")

    if not query:
        input("Ви нічого не ввели, будь ласка спробуйте ще. Натисніть Enter для продовження.")
        return
    
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

def sort_notes_by_tags(note_manager, tags):
    clear_screen()
    print("Сортування нотаток за тегами")

    if not tags:
        input("Ви не ввели жодного тегу. Натисніть Enter для продовження.")
        return
    
    sorted_notes = []
    exact_match_notes = []

    for tag in tags:
        notes = note_manager.search_notes(tag)
        if notes:
            exact_match_notes.extend(notes)

    all_notes = note_manager.show_all_notes()
    for note in all_notes:
        if note not in exact_match_notes:
            sorted_notes.append(note)

    if exact_match_notes:
        print(f"Нотатки з точним збігом по тегам '{', '.join(tags)}':")
        for i, note in enumerate(exact_match_notes, start=1):
            print(f"{i}. Заголовок: {note['title']}")
            print(f"   Тіло: {note['body']}")
            print(f"   Теги: {', '.join(note['tags'])}")

    sorted_notes.sort(key=lambda x: ', '.join(x['tags']))
    if sorted_notes:
        print("Інші нотатки відсортовані за алфавітом по тегу:")
        for i, note in enumerate(sorted_notes, start=1):
            print(f"{i}. {note['title']} - {note['body']} - ({', '.join(sorted(note['tags']))})")

    input("Натисніть Enter для продовження.")


def show_all_notes(note_manager):
    print("Всі нотатки:")
    all_notes = note_manager.show_all_notes()

    if all_notes:
        for i, note in enumerate(all_notes, start=1):
            print(f"{i}. Заголовок: {note['title']}")
            print(f"   Тіло: {note['body']}")
            print(f"   Теги: {', '.join(note['tags'])}")
    else:
        print("Список нотаток порожній.")

    input("Натисніть Enter для продовження.")

def clear_all_notes(note_manager):
    clear_screen()
    print("Видалення всіх нотаток")
    confirmation = input("Ви впевнені, що хочете видалити всі нотатки? (Так/Ні):")

    if confirmation.lower() == "так":
        note_manager.clear_all_notes()
        input("Усі нотатки були видалені. Натисніть Enter для продовження.")
    elif confirmation.lower() == "ні":
        input("Видалення всіх нотаток скасоване. Натисніть Enter для продовження.")
    else:
        input("Некоректний ввід, дію скасовано. Натисніть Enter для продовження.")



#################################################################################################################################



# def files_menu():
#     folder_path = "your_folder"  # Замініть на шлях до папки, яку ви хочете сортувати
#     file_manager = FileManager(folder_path)

#     while True:
#         clear_screen()
#         print("2Файли")
#         print("1. Сортувати файли за категоріями")
#         print("2. Назад")

#         choice = input("Оберіть опцію (1/2): ")

#         if choice == "1":
#             file_manager.sort_files_by_category()
#             input("Файли успішно відсортовано за категоріями. Натисніть Enter для продовження.")
#         elif choice == "2":
#             return
#         else:
#             input("Некоректний вибір. Натисніть Enter для продовження.")

if __name__ == "__main__":
    main_menu()
