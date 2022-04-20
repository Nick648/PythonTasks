import pprint


# Функция перехода из комнаты в комнату
def go(room):
    def func(state):
        return dict(state, room=room)

    return func


def go_conditional(room, cond):
    def func(state):
        if cond(state):
            return dict(state, room=room)
        else:
            return state

    return func


def toggle_lever(lever_name):
    def func(state):
        result = dict(state)
        result[lever_name] = not state[lever_name]
        return result

    return func


# Структура игры. Комнаты и допустимые в них действия
game = {
    'room0': dict(
        left=go('room1'),
        up=go('room2'),
        right=go('room3')
    ),
    'room1': dict(
        up=go('room2'),
        right=go('room0')
    ),
    'room2': dict(
    ),
    'room3': dict(
        up=go('room4'),
        right=go('room5')
    ),
    'room4': dict(
        down=go('room3'),
        right=go('room5')
    ),
    'room5': dict(
        up=go('room4'),
        left=go('room3')
    )
}

# Стартовое состояние
START_STATE = dict(room='room0', lever1=False, lever2=False, lever3=False)


def is_goal_state(s):
    '''
    Проверить, является ли состояние целевым.
    На входе ожидается множество пар ключ-значение.
    '''
    return ('room', 'room2') in s


def get_current_room(state):
    '''
    Выдать комнату, в которой находится игрок.
    '''
    return state['room']


def make_model(game, start):
    result = dict()
    to_visit = [start]
    visited = list()
    while to_visit:
        state = to_visit.pop()
        state_tuple = tuple(state.items())
        result[state_tuple] = list()
        visited.append(state_tuple)
        for name, action in list(game[get_current_room(state)].items()):
            new_state = action(state)
            new_state_tuple = tuple(new_state.items())
            if new_state_tuple not in visited and new_state not in to_visit:
                to_visit.append(new_state)
            result[state_tuple].append(new_state_tuple)
    pprint.pprint(visited)
    return result


def find_dead_ends(graph):
    result = list()
    for state in graph:
        to_visit = [state]
        visited = list()
        is_dead = True
        while to_visit:
            next_state = to_visit.pop()
            if next_state in visited:
                continue
            if is_goal_state(next_state):
                is_dead = False
            to_visit.extend(graph[next_state])
            visited.append(next_state)
        if is_dead:
            result.append(state)
    return result


def print_dot(graph, start_key):
    dead_ends = find_dead_ends(graph)
    print('digraph {')
    graph_keys = list(graph.keys())
    for x in graph:
        n = graph_keys.index(x)
        if x == start_key:
            print(f'n{n} [style="filled",fillcolor="dodgerblue",shape="circle"]')
        elif is_goal_state(x):
            print(f'n{n} [style="filled",fillcolor="green",shape="circle"]')
        elif x in dead_ends:
            print(f'n{n} [style="filled",fillcolor="red",shape="circle"]')
        else:
            print(f'n{n} [shape="circle"]')
    for x in graph:
        n1 = graph_keys.index(x)
        for y in graph[x]:
            n2 = graph_keys.index(y)
            print(f'n{n1} -> n{n2}')
    print('}')


graph = make_model(game, START_STATE)
print(graph)
print_dot(graph, START_STATE)
