with open('./input_data/day13.txt', mode='r') as file:
    data = file.read().split('\n')

# PART 1

timestamp = int(data[0])
bus_id = []

for value in data[1].split(','):
    if value != 'x':
        bus_id.append(int(value))

closest_numbers = []

j = 0

while True:
    i = 0
    while True:
        i += 1
        num = i * bus_id[j]
        if num > timestamp:
            closest_numbers.append([bus_id[j], num - timestamp])
            break
    j += 1
    if j > len(bus_id) - 1:
        break
index = closest_numbers[1].index(min(closest_numbers[1]))
print(closest_numbers[index][0]*closest_numbers[index][1])

# PART 2
buses = [set(), set(),set(),set(),set()]

i = 0
while True:
    i += 1
    buses[0].add(bus_id[0] * i)
    buses[1].add(bus_id[1] * i - 1)
    buses[2].add(bus_id[2] * i - 4)
    buses[3].add(bus_id[3] * i - 6)
    buses[4].add(bus_id[4] * i - 7)
    a = buses[0] & buses[1]& buses[2]& buses[3]& buses[4]
    if len(a) > 0:
        a = 0
