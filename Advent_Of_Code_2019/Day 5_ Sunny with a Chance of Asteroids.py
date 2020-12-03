
def parse_code(code):
    mode = str(code)
    mode = '0' * (5 - len(mode)) + mode
    modes = [int(x) for x in mode[:3]][::-1]
    instruction = mode[-1]
    return int(instruction), modes

program = [int(x) for x in open('./input_data/day5.txt').read().split(sep=',')]
program_steps = [0, 3, 3, 1, 1, 2, 2, 3, 3]

if __name__ == '__main__':
    i = 0
    while program[i] != 99:
        opcode, modes = parse_code(program[i])
        operands = [program[i+x+1] if modes[x] else program[program[i+x+1]] for x in range(program_steps[opcode])]
        if opcode == 1:
            program[program[i+3]] = operands[0] + operands[1]
        elif opcode == 2:
            program[program[i+3]] = operands[0] * operands[1]
        elif opcode == 3:
            program[program[i+1]] = 1
        elif opcode == 4:
            print(operands[0])
        elif opcode == 5:
            i = operands[1] - 3 if operands[0] != 0 else i
        elif opcode == 6:
            i = operands[1] - 3 if operands[0] == 0 else i
        elif opcode == 7:
            if operands[0] < operands[1]:
                program[program[i + 3]] = 1
            else:
                program[program[i+3]] = 0
        elif opcode == 8:
            if operands[0] == operands[1]:
                program[program[i + 3]] = 1
            else:
                program[program[i+3]] = 0

        i += program_steps[opcode] + 1


