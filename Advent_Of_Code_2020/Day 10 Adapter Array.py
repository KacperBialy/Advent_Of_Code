with open('./input_data/day10.txt', mode='r') as file:
    data = [0] + list(map(int, file.read().split()))

data.sort()
data.append(data[-1] + 3)
# PART 1

differences = [data[i] - data[i - 1] for i in range(1, len(data))]
print(differences.count(1) * differences.count(3))

# PART 2

ways = [1] * (data[-1] + 1)
for d in data[1:]:
    help = []
    for n in range(d - 3, d):
        if n in data:
            help.append(ways[n])
    ways[d] = sum(help)
print(ways[-1])
