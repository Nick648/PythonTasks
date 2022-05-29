"""
Вариант 1
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
    table = list(map(list, zip(*new_table)))  # transposition
    new_table = list()
    for row in table:
        if row not in new_table and set(row) != {None}:  # =~ del empty row and similar row(column)
            new_table.append(row)
    table = list(map(list, zip(*new_table)))  # transposition -> original
    for row in table:
        data = row[0].strip().split('/')  # date
        row[0] = data[2][2:] + '/' + data[1] + '/' + data[0]
        finder = row[1].find(':')
        row.append(row[1][row[1].rfind(' ', 0, finder) + 1:finder])  # name
        if row[1][finder + 1:].strip() == 'Выполнено':
            row[1] = 'true'  # Logical(bool)
        else:
            row[1] = 'false'  # Logical(bool)
    table = list(map(list, zip(*table)))

    return table


input_1 = [[None, None, None, None],
           ['22/04/2003', None, '22/04/2003', 'А.Ф. Вувян:Не выполнено'],
           ['20/03/2004', None, '20/03/2004', 'Т.О. Русберг:Не выполнено'],
           ['24/02/2000', None, '24/02/2000', 'С.С. Лишазяк:Не выполнено '],
           ['18/04/2003', None, '18/04/2003', ' Н.В. Цогак:Не выполнено']]

main(input_1)


# For CAP, you only need what is above, having checked in advance for PEP8


def output_data(arr, number=0):  # output array
    print("Table " + str(number) + ":\n")
    pprint(main(arr))
    print('\n', '-' * 120, '\n')


input_1 = [[None, None, None, None],
           ['22/04/2003', None, '22/04/2003', 'А.Ф. Вувян:Не выполнено'],
           ['20/03/2004', None, '20/03/2004', 'Т.О. Русберг:Не выполнено'],
           ['24/02/2000', None, '24/02/2000', 'С.С. Лишазяк:Не выполнено '],
           ['18/04/2003', None, '18/04/2003', ' Н.В. Цогак:Не выполнено']]

input_2 = [[None, None, None, None],
           ['04/07/2004', None, '04/07/2004', 'П.Ц. Зобянц:Выполнено'],
           ['28/08/2000', None, '28/08/2000', 'К.Ф. Шуцаляк:Выполнено '],
           ['15/07/1999', None, '15/07/1999', ' С.В. Нузозли:Не выполнено']]

if __name__ == "__main__":
    print('\nResult:\n')
    print('-' * 120, '\n')
    output_data(input_1, 1)
    output_data(input_2, 2)
    print('Done!')
