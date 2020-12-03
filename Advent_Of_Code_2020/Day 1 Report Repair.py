with open('./input_data/day1.txt', mode='r') as file:
    data = list(map(int, file.read().split()))

# PART 1

output_1 = 0
for i in range(len(data)):
    for j in range(i, len(data)):
        if data[i] + data[j] == 2020:
            output_1 = data[i] * data[j]
            print(output_1)
            break
# PART 2

output_2 = 0
for i in range(len(data)):
    for j in range(i, len(data)):
        for k in range(j, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                output_2 = data[i] * data[j] * data[k]
                print(output_2)
                break
