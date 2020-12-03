import time
import sys

def program_alarm(a, b):
    opcodes = load_data(a, b)
    index = 0
    while True:
        if opcodes[index] == 1:
            opcodes[opcodes[index + 3]] = opcodes[opcodes[index + 1]] + opcodes[opcodes[index + 2]]
            index += 4
        elif opcodes[index] == 2:
            opcodes[opcodes[index + 3]] = opcodes[opcodes[index + 1]] * opcodes[opcodes[index + 2]]
            index += 4
        elif opcodes[index] == 99:
            break
    return opcodes


def load_data(a, b):
    list_of_opcodes = [int(x) for x in open("./input_data/day2.txt").read().split(sep=',')]
    list_of_opcodes[1] = a
    list_of_opcodes[2] = b
    return list_of_opcodes


# PART 1
start = time.time()
print(program_alarm(12, 2)[0])
# PART 2
output = 0
for i in range(99):
    for j in range(99):
        if program_alarm(i, j)[0] == 19690720:
            output = program_alarm(i, j)
            noun = output[1]
            verb = output[2]
            print(100 * noun + verb)
            stop = time.time()
            print("time : ", stop - start)
            sys.exit()

