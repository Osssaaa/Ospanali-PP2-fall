import os

file_path = r"C:\\Users\\User\\Desktop\\code\\git-lessons\\lab06\\dir-and-files\\del.txt"

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):  
        os.remove(file_path)
        print("Файл удалён.")
    else:
        print("Нет прав на удаление файла.")
else:
    print("Файл не существует.")