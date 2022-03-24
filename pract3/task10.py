import csv
import datetime

import matplotlib.pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


with open('data/messages.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))
with open('data/results.csv', encoding='utf8') as f:
    results = list(csv.reader(f, delimiter=','))

# print(messages[0]) # ['1', '0', '4', 'ИКБО-01-20', '2022-02-18 12:58:23.489167']
# print(results[0]) # ['0', '10', 'ИКБО-01-20', '2022-02-18 13:16:58.637975', '2']

def z1():
    hours = [parse_time(row[-1]).hour for row in messages]
    plt.hist(hours, bins = 24)
    plt.xticks(range(24))
    plt.title("Активность на день") # заголовок
    plt.xlabel("Часы") # ось абсцисс
    plt.ylabel("Кол-во") # ось ординат
    plt.grid() # включение отображение сетки
    plt.show()

def z2():
    days = [parse_time(row[-1]).weekday() for row in messages]
    plt.hist(days, bins = 7)
    plt.xticks(range(7))
    plt.title("Активность на неделе") # заголовок
    plt.xlabel("День недели") # ось абсцисс
    plt.ylabel("Кол-во") # ось ординат
    plt.grid() # включение отображение сетки
    plt.show()

def z3():
    groups = [row[-2] for row in messages]
    groups_set = set(groups)
    groups_dict = {group: groups.count(group) for group in groups_set}
    sorted_groups = sorted(groups_dict.items(), key=lambda x: x[1])
    plt.bar([x[0] for x in sorted_groups], [x[1] for x in sorted_groups])
    plt.xticks(rotation=60)
    plt.title("Кол-во сообщений") # заголовок
    plt.xlabel("Группа") # ось абсцисс
    plt.ylabel("Кол-во") # ось ординат
    plt.grid() # включение отображение сетки
    plt.show()

def z4():
    groups = [row[-3] for row in results if row[-1] == '2']
    groups_set = set(groups)
    groups_dict = {group: groups.count(group) for group in groups_set}
    sorted_groups = sorted(groups_dict.items(), key=lambda x: x[1])
    plt.bar([x[0] for x in sorted_groups], [x[1] for x in sorted_groups])
    plt.xticks(rotation=60)
    plt.title("Кол-во правильных решений") # заголовок
    plt.xlabel("Группа") # ось абсцисс
    plt.ylabel("Кол-во") # ось ординат
    plt.grid() # включение отображение сетки
    plt.show()

def z5():
    tasks = [row[1] for row in messages]
    plt.hist(tasks, bins=len(set(tasks)))
    plt.xticks(range(1, len(set(tasks))+1))
    plt.title("Сложность задания") # заголовок
    plt.xlabel("Задание") # ось абсцисс
    plt.ylabel("Кол-во") # ось ординат
    #plt.grid() # включение отображение сетки
    plt.show()

if __name__ == "__main__":
    z1()
    z2()
    z3()
    z4()
    z5()