import time
import os
import pyautogui as pg
import random


def check_set():  # Возврат длины set() - количество различных символов(кодов)
    HomeDir = os.path.expanduser('~')
    HomeDir += r'\Desktop'
    file = open(file=HomeDir + r'\text.txt', mode='r', encoding='utf-8')
    lines = file.read()
    count_char = set(lines)
    # print(count_char, len(count_char))
    file.close()
    return len(count_char)


def check_ord(lines):  # Проверка кода символа
    for i in lines:
        print(i)
        s = input("Узнать код?(+/-): ")
        if s == "+":
            for char in i:
                print(ord(char), end=" ")


def check_symbol():  # Проверка символов в файле
    HomeDir = os.path.expanduser('~')
    HomeDir += r'\Desktop'
    file = open(file=HomeDir + r'\text.txt', mode='r', encoding='utf-8')
    for line in file:
        line = line.lower()
        lines = line.split(' ')
        check_ord(lines)
        print(lines)

    file.close()


def exi_t():  # Выход из программы
    seconds = [0.03, 0.04, 0.05, 0.06]
    print()
    s = "Спасибо за использование нашей программы.\nВсего хорошего!"
    for i in s:
        print(i, end="")
        time.sleep(random.choice(seconds))
    time.sleep(2)


def algorithm(HomeDir):  # Основной алгоритм
    asci_punctuation = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                        46, 47, 58, 59, 60, 61, 62, 63, 91, 92, 93, 94,
                        95, 96, 123, 124, 125, 126, 171, 187, 8212]  # Знаки препинания
    dict_words = {}  # Словарь dict()
    count_words = 0
    count_digits = 0
    count_char = check_set()
    file = open(file=HomeDir + r'\text.txt', mode='r', encoding='utf-8')

    for line in file:

        line = line.lower()
        for char in line:
            if ord(char) in asci_punctuation:
                line = line.replace(char, ' ')

        lines = line.split(' ')
        for item in lines:
            if item:  # Не пустая строка
                if "\n" in item and len(item) != 1: # Если без пробела началась новая строка
                    item = item[:-1]
                if item in dict_words:
                    dict_words[item] += 1
                    if item.isdigit():
                        count_digits += 1
                    else:
                        count_words += 1
                else:
                    dict_words[item] = 1
                    if item.isdigit():
                        count_digits += 1
                    else:
                        count_words += 1
    file.close()
    if "\n" in dict_words.keys():  # Есть ли абзацы
        all_words = count_words - dict_words["\n"]
    else:
        all_words = count_words

    print("Количество различных символов в файле: ", count_char)
    print("Количество слов в тексте: ", all_words)
    print("Количество чисел в тексте: ", count_digits)
    for item_keys in sorted(dict_words.keys()):
        if item_keys == "\n":
            print("Абзацев:", dict_words[item_keys], "\n")
        else:
            print(item_keys.title(), ": ", dict_words[item_keys])

    with open(file='Number_of_words.txt', mode='w', encoding='utf-8') as file_2:  # a
        n = "\n"
        file_2.write(f"Количество различных символов в файле: {count_char}\n")
        file_2.write(f"Количество слов в тексте: {all_words}\n")
        file_2.write(f'Количество чисел в тексте: {count_digits}\n')
        if "\n" in dict_words.keys():
            file_2.write(f'Абзацев: {dict_words[n]}\n')
        file_2.write(f'\n')

        for item_keys in sorted(dict_words.keys()):
            if item_keys == "\n":
                pass
            else:
                file_2.write(f'{item_keys.title()}: {dict_words[item_keys]}\n')

    pg.alert(text=f"Количество слов в тексте: {all_words}\n", title='Итог работы программы', button='OK')
    return  # Прочитан весь файл


def file_open(HomeDir):  # Проверка готовности файла
    while True:
        print("Создайте на рабочем столе текстовый файл с нужным содержанием и именем: 'text.txt'")
        print("Введите '-' если хотите выйти из программы")
        print("Введите '+' если создали файл text.txt: ")
        s = input()

        if s == "-":
            return 0

        elif s == "+":
            try:
                with open(file=HomeDir + r'\text.txt', mode='r', encoding='utf-8') as _:
                    print('\nВсё ок! Файл открыт!\n')
                    return 1

            except FileNotFoundError:  # Ошибка
                print("\nУ вас НЕТ на рабочем столе файла с именем 'text.txt'!\n")

        else:
            print("\nВы ввели иной символ не подходящий для данной программы(\n")


def main():  # Старт программы
    print("Программа по подсчёту слов текста из файла")
    HomeDir = os.path.expanduser('~')
    HomeDir += r'\Desktop'
    # print("Путь к рабочему столу: " + HomeDir + "\n")
    if file_open(HomeDir) == 1:
        algorithm(HomeDir)

    exi_t()


if __name__ == "__main__":
    # check_symbol()
    # check_set()
    main()
