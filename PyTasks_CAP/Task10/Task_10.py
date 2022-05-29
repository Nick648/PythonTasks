"""
Вариант 18
table = [[1,2,3],
        [4,5,6]]
zip(*table) = [(1,4),(2,5),(3,6)]
copy input data when error send answer
"""
from pprint import pprint


def main(table):
    new_table = list()
    for row in table:
        if row not in new_table and set(row) != {None}:  # =~ del empty row and similar row
            new_table.append(row)
    table = list(map(list, zip(*new_table)))  # transposition
    new_table = list()
    for row in table:
        if row not in new_table and set(row) != {None}:  # =~ del empty row and similar row
            new_table.append(row)
    table = list(map(list, zip(*new_table)))  # transposition -> original
    '''
    i = 0
    while i < len(table):
        if set(table[i]) == {None}: # del empty column(row)
            del table[i]
        i += 1
    for i in range(len(table)): # del similar column(row)
        if i > 0 and table[i] == table[i-1]:
            del table[i]
    table = list(map(list, zip(*table))) # transposition -> original
    '''
    for row in table:
        if row[0].strip() == 'true':
            row[0] = 'Да'
        elif row[0].strip() == 'false':
            row[0] = 'Нет'
        row[1] = row[1].strip().split(']')[1]  # email
        number = row[2].strip()[row[2].find(' ', 3) + 1:]
        number = number[:number.find('-') + 1] + number[number.find('-') + 1:].replace('-', '')
        row[2] = number
        row[3] = row[3].strip()[:-4] + row[3].strip()[-2:]  # date
    # new_table.sort(key=lambda x: x[3])
    return table


input_str = [[None, 'true', 'leonid49[at]mail.ru', '+7 435 974-48-88', '06-06-1999', '06-06-1999'],
             [None, None, None, None, None, None],
             [None, None, None, None, None, None],
             [None, 'false', 'miroslav78[at]rambler.ru', '+7 554 685-39-99', '04-09-2003', '04-09-2003'],
             [None, 'false', 'Sahar19[at]gmail.com', '+7 254 789-44-24', '16-11-2003', '16-11-2003']]

main(input_str)


# For CAP, you only need what is above, having checked in advance for PEP8


def output_data(arr, number=0):  # output array
    print("Table " + str(number) + ":\n")
    pprint(main(arr))
    print('\n', '-' * 120, '\n')


if __name__ == "__main__":
    print('\nResult:\n')
    print('-' * 120, '\n')
    output_data(input_str, 1)
    print('Done!')
