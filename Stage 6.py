# Этот немного сложнее.
# Вы можете сделать 2 вещи для статистики:
# 1 - Напишите словарь внутри своего словаря как:
# flash_cards = {имя_карты 1:{определение: card_def1, номер ошибки:3},
# имя_карты 2:{определение: card_def2, номер ошибки:1}}

# Я думаю, что это элегантный способ. Но для этого вам может потребоваться изменить свой предыдущий код.


# 2 - Напишите другой словарь, который принимает в качестве ключа "имя карты" при неправильном ответе и
# в качестве значения обновляет его, поскольку он продолжает ошибаться. Это самый простой способ, так как
# вам может не понадобиться так сильно ретушировать свой код.
#
# Получение самой сложной карты - это просто пролистывание словаря, сравнивая 0 со следующим значением,
# если оно больше, измените его на это значение, сравните со следующим и повторите сравнение. Вы можете
# составить список и добавить "ключ" из этого значения. Если следующее значение равно вашему фактическому
# значению, добавьте этот ключ. теперь просто распечатайте это.
#
# - Для использования регистратора :
# из ввода-вывода импортируйте строку
# - создайте свой конструктор:
# memory_file = строковый файл()
# - каждый раз, когда вы хотите написать, сначала прочитайте файл следующим образом:
# memory_file.read()
# файл памяти.запись ("строка")
#
# чтобы сохранить его, просто используйте обычный контекстный менеджер:
# с открытым (имя_файла, "w") в качестве журнала:
# для строки в файле memory_file:
# войти.записать (строка)
#
# Я надеюсь, что это поможет.

import random
import io
import logging


class Flashcards:
    dict_termin = dict()  # диск для сохранение терминов с их значениями
    list_key_termin = []  # список для сохранение ключей диска, точнение терминов
    list_value_termin = []  # список для сохранение значении диска
    list_number_of_errors_termin = []  # список для сохранение количество ошибок при проверке знание терминов
    logging.basicConfig(filename='log_file.txt', filemode='w',
                        format='%(message)s', level='DEBUG')

    output = io.StringIO()

    @classmethod
    def add(cls):
        key_termin = input("The card:\n").strip()
        logging.debug(f'The card:\n{key_termin}')
        while cls.list_key_termin.count(key_termin) != 0:
            key_termin = input(f'The card "{key_termin}" already exists. Try again:\n').strip()
            logging.debug(f'The card "{key_termin}" already exists. Try again:\n{key_termin}')
        cls.list_key_termin.append(key_termin)

        value_termin = input("The definition of the card:\n").strip()
        logging.debug(f'The definition of the card:\n{value_termin}')
        while cls.list_value_termin.count(value_termin) != 0:
            value_termin = input(f'The definition "{value_termin}" already exists. Try again:\n').strip()
            logging.debug(f'The definition "{value_termin}" already exists. Try again:\n{value_termin}')
        cls.list_value_termin.append(value_termin)

        cls.dict_termin.update({key_termin: value_termin})

        cls.list_number_of_errors_termin.append(0)

        print(f'"The pair ("{cls.list_key_termin[-1]}":"{cls.list_value_termin[-1]}") has been added."')
        logging.debug(f'"The pair ("{cls.list_key_termin[-1]}":"{cls.list_value_termin[-1]}") has been added."')

        return Flashcards.x()

    @classmethod
    def remove(cls):
        try:
            key_termin = input("Which card?\n").strip()
            logging.debug(f'Which card?\n{key_termin}')
            cls.list_value_termin.remove(cls.dict_termin.pop(key_termin))
            cls.list_number_of_errors_termin.pop(cls.list_key_termin.index(key_termin))
            cls.list_key_termin.remove(key_termin)
            print("The card has been removed.")
            logging.debug("The card has been removed.")
        except KeyError:
            print(f'Can\'t remove "{key_termin}": there is no such card.')
            logging.debug(f'Can\'t remove "{key_termin}": there is no such card.')
        return Flashcards.x()

    @classmethod
    def import_termin(cls):
        try:
            file_name = input("File name:\n")
            logging.debug(f'File name:\n{file_name}')
            with open(file_name, 'r', encoding='utf-8') as file:
                b = file.read()
                n = len(b.strip().split('\n'))
                print(f"{n} cards have been loaded.")
                logging.debug(f"{n} cards have been loaded.")
                for i in b.strip().split('\n'):
                    key_termin, value_termin = i.split(':')
                    cls.dict_termin.update({key_termin: value_termin})
                    if cls.list_key_termin.count(key_termin) == 0:
                        cls.list_key_termin.append(key_termin)
                        cls.list_value_termin.append(value_termin)
                        cls.list_number_of_errors_termin.append(0)
                    else:
                        cls.list_value_termin.pop(cls.list_key_termin.index(key_termin))
                        cls.list_value_termin.insert(cls.list_key_termin.index(key_termin), value_termin)

                        cls.list_number_of_errors_termin.pop(cls.list_key_termin.index(key_termin))
                        cls.list_number_of_errors_termin.insert(cls.list_key_termin.index(key_termin), 0)
        except FileNotFoundError:
            print("File not found.")
            logging.debug("File not found.")

        return Flashcards.x()

    @classmethod
    def export(cls):
        try:
            file_name = input("File name:\n")
            logging.debug(f'File name:\n{file_name}')
            with io.open(file_name, 'w', encoding="utf-8") as file:
                for i in range(len(cls.list_key_termin)):
                    key_termin, value_termin = cls.list_key_termin[i], cls.list_value_termin[i]
                    file.write(f'{key_termin}:{value_termin}\n')
        except FileNotFoundError:
            print("File not found.")
            logging.debug("File not found.")

        print(f"{len(cls.list_key_termin)} cards have been saved.")
        logging.debug(f"{len(cls.list_key_termin)} cards have been saved.")
        return Flashcards.x()

    @classmethod
    def ask(cls):
        count = int(input("How many times to ask?\n"))
        logging.debug(f"How many times to ask?\n{count}")
        for i in range(count):
            try:
                a = random.choice(cls.list_key_termin)
                b = cls.list_value_termin[cls.list_key_termin.index(a)]
                value_proverka = input(f'Print the definition of "{a}":\n').strip()
                logging.debug(f'Print the definition of "{a}f":\n{value_proverka}')
                err = cls.list_key_termin[cls.list_value_termin.index(value_proverka)]

                if b == value_proverka:
                    print("Correct!")
                    logging.debug("Correct!")
                else:
                    print(f'Wrong. The right answer is "{b}", but your definition is correct for "{err}".')
                    logging.debug(f'Wrong. The right answer is "{b}", but your definition is correct for "{err}".')
                    cls.list_number_of_errors_termin[cls.list_key_termin.index(a)] += 1
            except ValueError:
                print(f'Wrong. The right answer is "{b}".')
                logging.debug(f'Wrong. The right answer is "{b}".')
                cls.list_number_of_errors_termin[cls.list_key_termin.index(a)] += 1
        return Flashcards.x()

    @classmethod
    def log(cls):
        file_name = input("File name:\n")
        with open(file_name, 'a', encoding='utf-8') as file1, open('log_file.txt', 'r', encoding='utf-8') as file2:
            for i in file2:
                file1.write(i)
            print('The log has been saved.\n')
            logging.debug('The log has been saved.\n')



    @classmethod
    def hardest_card(cls):
        k = cls.list_number_of_errors_termin
        max_errors = max(k)
        bnm = [cls.list_key_termin[i] for i in range(len(k)) if k[i] == max_errors]
        if len(bnm) == 0:
            print('There are no cards with errors.')
            logging.debug('There are no cards with errors.')
        elif len(bnm) > 1:
            a = ', '.join(bnm)
            print(f'The hardest cards are {a}. You have {max_errors} errors answering them.')
            logging.debug(f'The hardest cards are {a}. You have {max_errors} errors answering them.')
        elif len(bnm) == 1:
            print(f"The hardest card is {bnm[0]}. You have {max_errors} errors answering it")
            logging.debug(f'The hardest card is {bnm[0]}. You have {max_errors} errors answering it')

        return Flashcards.x()

    @classmethod
    def reset_stats(cls):
        for i in range(len(cls.list_number_of_errors_termin)):
            cls.list_number_of_errors_termin[i] = 0

        print("Card statistics have been reset.")
        logging.debug("Card statistics have been reset.")
        return Flashcards.x()

    @staticmethod
    def x():
        action = input("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n")
        logging.debug(f'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n{action}')
        if action == 'add':
            return Flashcards.add()
        elif action == 'remove':
            return Flashcards.remove()
        elif action == 'import':
            return Flashcards.import_termin()
        elif action == 'export':
            return Flashcards.export()
        elif action == 'ask':
            return Flashcards.ask()
        elif action == 'exit':
            print('Bye bye!')
            return
        elif action == 'log':
            return
        elif action == 'hardest card':
            return Flashcards.hardest_card()
        elif action == 'reset stats':
            return Flashcards.reset_stats()


Flashcards.x()
