with open('./input_data/day6.txt', mode='r') as file:
    data = file.read().split('\n')

# PART 1

group = ""
Groups1 = []

for txt in data:
    if txt != "":
        for i in range(len(txt)):
            group += txt[i]
    else:
        Groups1.append(group)
        group = ""
Groups1.append(group)

output_1 = sum([len(set(group)) for group in Groups1])
print(output_1)

# PART 2

group = []
Groups2 = []

for i in range(len(data)):
    if data[i] != "":
        group.append(data[i])
    else:
        Groups2.append(group)
        group = []
Groups2.append(group)

same_answers = []

for index, group in enumerate(Groups2):
    keys = set(Groups1[index])
    for person in group:
        keys = keys & set(person)
    same_answers.append(keys)

output_2 = sum([len(answer) for answer in same_answers])
print(output_2)
