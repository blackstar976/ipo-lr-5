text = input("Введите строку на руском языке: ")

vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'

vowe1_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char in consonants)

print(f"Длинна строки: {len(text)}")
print(f"Гласные: {vowe1_count}")
print(f"Согласные: {consonant_count}")
