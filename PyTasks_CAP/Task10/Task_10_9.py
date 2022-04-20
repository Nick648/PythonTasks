"""
Вариант 9
table = [[1,2,3],
        [4,5,6]]
zip(*table) = [(1,4),(2,5),(3,6)]
"""
from pprint import pprint


def main(table):
    new_table = list()
    for row in table:
        if row not in new_table and set(row) != {None}:  # =~ del empty row and similar row
            new_table.append(row)

    for row in new_table:
        if row[2].strip() == '1':
            row[2] = 'Да'  # Logical(bool)
        elif row[2].strip() == '0':
            row[2] = 'Нет'  # Logical(bool)
        data = row[0].strip().split('/')  # date
        row[0] = data[2] + '/' + data[1] + '/' + data[0]
        digit = str(round(float(row[1].strip()), 2))  # digit
        while len(digit) != 4:
            digit += '0'  # if 0.4 != 0.40
        row[1] = digit
        row[3] = row[3][row[3].rfind('@') + 1:].strip()  # email

    table = list(map(list, zip(*new_table)))  # transposition
    return table


input_1 = [['25/02/00', '0.9774', '1', 'cezskij49@mail.ru'],
           ['18/11/02', '0.4027', '0', 'serskij63@gmail.com'],
           ['18/11/02', '0.4027', '0', 'serskij63@gmail.com'],
           ['18/11/02', '0.4027', '0', 'serskij63@gmail.com'],
           ['24/09/02', '0.1432', '1', 'rorko52@rambler.ru'],
           ['11/08/01', '0.3415', '0', 'fadan4@yandex.ru']]

main(input_1)


# For CAP, you only need what is above, having checked in advance for PEP8

def output_data(arr, number=0):  # output array
    print("Table " + str(number) + ":\n")
    pprint(main(arr))
    print('\n', '-' * 120, '\n')


input_1 = [['25/02/00', '0.9774', '1', 'cezskij49@mail.ru'],
           ['18/11/02', '0.4027', '0', 'serskij63@gmail.com'],
           ['18/11/02', '0.4027', '0', 'serskij63@gmail.com'],
           ['18/11/02', '0.4027', '0', 'serskij63@gmail.com'],
           ['24/09/02', '0.1432', '1', 'rorko52@rambler.ru'],
           ['11/08/01', '0.3415', '0', 'fadan4@yandex.ru']]

input_2 = [['19/06/04', '0.2120', '0', 'disuzuk91@rambler.ru'],
           ['15/08/00', '0.6387', '0', 'bicusberg95@gmail.com'],
           ['15/08/00', '0.6387', '0', 'bicusberg95@gmail.com'],
           ['15/08/00', '0.6387', '0', 'bicusberg95@gmail.com'],
           ['01/10/99', '0.8157', '0', 'cabuk81@mail.ru']]

if __name__ == "__main__":
    print('\nResult:\n')
    print('-' * 120, '\n')
    output_data(input_1, 1)
    output_data(input_2, 2)
    print('Done!')
