# Открываем исходный файл для чтения
with open('text.txt', 'r', encoding='utf-8') as file:
    # Читаем все строки из файла в список
    lines = file.readlines()

# Открываем новый файл для записи
with open('output.txt', 'w', encoding='utf-8') as file:
    # Проходим по каждой строке
    for line in lines:
        # Заменяем все буквы 'о' на 'а' в строке
        new_line = line.replace('о', 'а')
        # Записываем измененную строку в новый файл
        file.write(new_line)

print("Файл output.txt успешно создан")