with open('./input_data/day5.txt', mode='r') as file:
    data = file.read().split()

# PART 1
all_id = []
for j in range(len(data)):
    rowMin = 0
    rowMax = 127
    for i in range(7):
        if data[j][i] == 'F':
            rowMax -= int((rowMax - rowMin + 1) / 2)
        elif data[j][i] == 'B':
            rowMin += int((rowMax - rowMin + 1) / 2)
    colMin = 0
    colMax = 7
    for i in range(7, 10, 1):
        if data[j][i] == 'L':
            colMax -= int((colMax - colMin + 1) / 2)
        elif data[j][i] == 'R':
            colMin += int((colMax - colMin + 1) / 2)

    all_id.append(rowMax * 8 + colMax)

all_id.sort()
output_1 = all_id[-1]

print(output_1)

# PART 2

output_2 = 0
for i in range(len(all_id)):
    if all_id[i] + 1 != all_id[i + 1]:
        output_2 = all_id[i] + 1
        break

print(output_2)
