import re


def Print_Menu() -> str:
    choice = input("1. Ввод строки и величины сдвига\n"
                   "2. Выполнить шифрование\n"
                   "3. Вывести результат\n"
                   "4. Завершить работу программы\n")
    return choice


def String_Work():
    eng_pattern = r"^[A-Za-z]+$"

    input_string = input("Введите вашу строку (только с англ. буквами): ")
    if not bool(re.match(eng_pattern, input_string)):
        return "Строка введена некорректно!"
    shift_value = int(input("Введите величину сдвига: "))
    if not shift_value:
        return "Величина сдвига указана некорретно!"
    encrypt_info: list = [input_string, shift_value]
    return encrypt_info


def Encryption_Process(text_to_encrypt: str, shift_value: int) -> str:
    if not text_to_encrypt or not shift_value:
        return "Не хватает данных!"

    encrypted_text = ""
    key = "LIME"
    key_length = len(key)

    for i, char in enumerate(text_to_encrypt):
        if char.isalpha():
            shift_amount = (ord(key[i % key_length].upper()) - ord('A') + shift_value) % 26
            encrypted_char = chr((ord(char.upper()) - ord('A') + shift_amount) % 26 + ord('A'))
            if char.islower():
                encrypted_text += encrypted_char.lower()
            else:
                encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text


def Printing_A_Result():
    return "образец"


def Quitting():
    return "образец"