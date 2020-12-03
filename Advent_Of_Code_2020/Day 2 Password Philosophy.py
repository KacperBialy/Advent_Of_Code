with open('./input_data/day2.txt', mode='r') as file:
    data = file.read().split()

# PART 1

numbers = []
letters = []
texts = []

for i, val in enumerate(data):
    if i % 3 == 0:
        numbers.append(list(map(int, val.split("-"))))
    if i % 3 == 1:
        letters.append(val[0])
    if i % 3 == 2:
        texts.append(val)
print(numbers)
print(letters)
print(texts)
counter_letter = 0
output_1 = 0
for i in range(len(texts)):
    counter = texts[i].count(letters[i])
    if numbers[i][0] <= counter <= numbers[i][1]:
        output_1 += 1
print(output_1)

# PART 2
output_2 = 0

for i in range(len(texts)):
    counter = 0
    if texts[i][numbers[i][0]-1] == letters[i]:
        counter += 1
    if texts[i][numbers[i][1]-1] == letters[i]:
        counter += 1
    if counter == 1:
        output_2 += 1
print(output_2)
