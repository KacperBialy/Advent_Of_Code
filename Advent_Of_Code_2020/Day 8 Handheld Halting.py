from copy import deepcopy


def Data():
    with open('./input_data/day8.txt', mode='r') as file:
        data = file.read().split('\n')
    instructions = []
    for line in data:
        line_splited = line.split()
        instruction = [line_splited[0], int(line_splited[1])]
        instructions.append(instruction)
    return instructions


def FindInfinityLoop(instructions):
    output_1 = 0
    step = 0
    steps = []
    while True:
        steps.append(step)
        if instructions[step][0] == "acc":
            output_1 += instructions[step][1]
        if instructions[step][0] == "jmp":
            step += instructions[step][1]
        else:
            step += 1
        if step in steps:
            return output_1


def FindEnd(instructions):
    instructions_copy = deepcopy(instructions)

    index = 0
    cont = True
    while True:
        output_2 = 0
        step = 0
        steps = []
        while cont:
            steps.append(step)
            if instructions_copy[step][0] == "acc":
                output_2 += instructions_copy[step][1]
            if instructions_copy[step][0] == "jmp":
                step += instructions_copy[step][1]
            else:
                step += 1
            if step in steps:
                break
            if step == len(instructions):
                return output_2

        instructions_copy = deepcopy(instructions)
        cont = False
        for a in range(index, len(instructions), 1):
            index += 1
            if instructions[a][0] == 'nop':
                if instructions[a][1] != 0:
                    instructions_copy[a][0] = 'jmp'
                    cont = True
                    break
            if instructions[a][0] == 'jmp':
                instructions_copy[a][0] = 'nop'
                cont = True
                break


def First():
    instructions = Data()
    print(FindInfinityLoop(instructions))


def Second():
    instructions = Data()
    print(FindEnd(instructions))


# PART 1
First()
# PART 2
Second()
