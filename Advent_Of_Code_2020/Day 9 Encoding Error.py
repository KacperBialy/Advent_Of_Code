with open('./input_data/day9.txt', mode='r') as file:
    data = list(map(int, file.read().split()))

# PART 1

preamble = 25
output_1 = 0
for i in range(preamble, len(data)):
    value = data[i]
    actually_data = data[i - preamble:i]
    isOk = False
    for j, val in enumerate(data[i - preamble:i]):
        for val1 in data[i + j + 1 - preamble:i]:
            if val + val1 == value:
                isOk = True
                break
    if not isOk:
        output_1 = value
        break

print(output_1)

# PART 2

output_2 = 0
max_val = 0
min_val = 0
index = 0
for i, val in enumerate(data):
    sum = val
    index += 1
    for j, val1 in enumerate(data[index:-1]):
        sum += val1
        if sum == output_1:
            max_val = max(data[i:j + index])
            min_val = min(data[i:j + index])

output_2 = min_val + max_val
print(output_2)
