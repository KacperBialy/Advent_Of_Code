import copy

with open('./input_data/day11.txt', mode='r') as file:
    data = file.read().split('\n')

steps = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for i in range(len(data)):
    data[i] = list('.' + data[i] + '.')
empty_line = list('.' * len(data[0]))
data.insert(0, empty_line)
data.append(empty_line)


def func(input_data):
    copy_array = copy.deepcopy(input_data)
    for i in range(1, len(input_data) - 1):
        for j in range(1, len(input_data) - 4):
            counter = 0
            for step in steps:
                symbol = input_data[i + step[0]][j + step[1]]
                if symbol == '#':
                    counter += 1
            if counter >= 4 and input_data[i][j] == '#':
                copy_array[i][j] = 'L'
            if counter == 0 and input_data[i][j] == 'L':
                copy_array[i][j] = '#'
    return copy_array


def First():
    old = copy.deepcopy(data)
    while True:
        array = func(old)
        if array == old:
            break
        old = copy.deepcopy(array)
    output_1 = 0
    for line in array:
        output_1 += line.count("#")
    print(output_1)

First()
