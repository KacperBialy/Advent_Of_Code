with open('./input_data/day3.txt', mode='r') as file:
    data = file.read().split()

# PART 1
data_duplicates = []
columns = len(data[0])
rows = len(data)
duplicates = int(rows * 3 / columns) + 1

for i in range(len(data)):
    data_duplicates.append(data[i] * duplicates)

output_1 = 0
row = 0
col = 0
for i in range(rows):
    if data_duplicates[row][col] == "#":
        output_1 += 1
    row += 1
    col += 3
print(output_1)

# PART 2
data_duplicates_2 = []
duplicates = int(rows * 7 / columns) + 1

for i in range(len(data)):
    data_duplicates_2.append(data[i] * duplicates)

output_2 = 1

numbers_of_trees = []
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for j in range(5):
    row = 0
    col = 0
    counter = 0
    row_val = slopes[j][1]
    col_val = slopes[j][0]
    for i in range(rows):
        if data_duplicates_2[row][col] == "#":
            counter += 1
        row += row_val
        col += col_val
        if row > rows:
            break
    numbers_of_trees.append(counter)

for val in numbers_of_trees:
    output_2 *= val

print(output_2)
