import os
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


def Printing_A_Result(encrypted_text: str) -> str:
    return encrypted_text


def Quitting():
    exit()


if __name__ == "__main__":
    while True:
        os.system("cls")
        user_choice = Print_Menu()
        match user_choice:
            case "1":
                encryption_info = String_Work()
                if type(encryption_info) is not list:
                    input(f"Ошибка: {encryption_info}.\n"
                          f"Нажмите любую клавишу, чтобы продолжить...")
                try:
                    encrypted_string = ""
                except:
                    pass
            case "2":
                try:
                    if type(encryption_info) is list:
                        encrypted_string = Encryption_Process(encryption_info[0], encryption_info[1])
                except:
                    input("Сперва введите данные для шифрования!\n"
                          "Нажмите любую клавишу, чтобы продолжить...")
            case "3":
                try:
                    input(f"Ваша зашифрованная строка: {encrypted_string}\n"
                          f"Нажмите любую клавишу, чтобы продолжить...")
                except:
                    input("Вы не осуществили шифрование, результат отсутствует\n"
                          "Нажмите любую клавишу, чтобы продолжить...")
            case "4":
                Quitting()
