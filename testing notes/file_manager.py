import os
import shutil

class FileManager:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def sort_files_by_category(self):
        # Створюємо словник для категорій файлів і їх розширень.
        categories = {
            "images": ('.jpeg', '.jpg', '.png', '.svg'),
            "videos": ('.avi', '.mp4', '.mov', '.mkv'),
            "documents": ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
            "music": ('.mp3', '.ogg', '.wav', '.amr'),
            "archives": ('.zip', '.gz', '.tar'),
            "unknown": ()
        }

        # Створюємо папки для кожної категорії, якщо вони не існують.
        for category in categories:
            category_folder = os.path.join(self.folder_path, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

        # Перебираємо файли у вказаній папці та сортуємо їх за категоріями.
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)

            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[-1].lower()
                moved = False

                for category, extensions in categories.items():
                    if file_extension in extensions:
                        destination_folder = os.path.join(self.folder_path, category)
                        destination_path = os.path.join(destination_folder, filename)

                        shutil.move(file_path, destination_path)
                        moved = True
                        break

                if not moved:
                    destination_folder = os.path.join(self.folder_path, "unknown")
                    destination_path = os.path.join(destination_folder, filename)

                    shutil.move(file_path, destination_path)

if __name__ == "__main__":
    folder_path = "your_folder"
    file_manager = FileManager(folder_path)
    file_manager.sort_files_by_category()
