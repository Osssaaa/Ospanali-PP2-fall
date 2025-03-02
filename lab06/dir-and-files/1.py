import os

def list_items(path):
    if not os.path.exists(path):
        return print("Путь не существует")
    
    items = os.listdir(path)
    print("\nТолько директории:", [d for d in items if os.path.isdir(os.path.join(path, d))] or "Нет директорий")
    print("Только файлы:", [f for f in items if os.path.isfile(os.path.join(path, f))] or "Нет файлов")
    print("Все файлы и директории:", items or "Папка пуста")

list_items(input("Введите путь к папке: "))