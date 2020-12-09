with open('./input_data/day7.txt', mode='r') as file:
    data = file.read().split('\n')


def FindBagsWithGold(output, bags_with_gold, summed_up):
    bags_with_gold1 = []
    for i, line in enumerate(data):
        for bag in bags_with_gold:
            if bag in line:
                if i not in summed_up:
                    bag = line.split("contain")
                    if len(bag) > 1:
                        bags_with_gold1.append(bag[0].split(" bag")[0])
                    summed_up.append(i)
                    output += 1
    return bags_with_gold1, output


def First():
    output = 0
    summed_up = []
    bags_with_gold = []

    for i, line in enumerate(data):
        bag = line.split("contain")
        if "shiny gold" in bag[1]:
            output += 1
            bags_with_gold.append(bag[0].split(" bag")[0])
            summed_up.append(i)

    while True:
        old_output = output
        bags_with_gold, output = FindBagsWithGold(output, bags_with_gold, summed_up)
        if old_output == output:
            break
    print(output)


def Second():
    roots = []
    for i, line in enumerate(data):
        bag = line.split("contain")
        if "shiny gold" in bag[0]:
            splited_bags = bag[1].replace('.', '').split(',')
            for splited_bag in splited_bags:
                split_bag_values = splited_bag.split()
                bag = [split_bag_values[0], split_bag_values[1], split_bag_values[2]]
                roots.append(bag)
            break
    all = []
    for root in roots:
        bag = [int(root[0]), root[1] + " " + root[2]]
        all.append(bag)
    while True:
        new_roots = []
        for i, line in enumerate(data):
            if "no other bag" in line:
                continue
            for root in roots:
                bag = line.split("contain")
                value = root[1] + ' ' + root[2]
                if value in bag[0]:
                    splited_bags = bag[1].replace('.', '').split(',')
                    for splited_bag in splited_bags:
                        split_bag_values = splited_bag.split()
                        bag = [int(root[0]) * int(split_bag_values[0]),
                               split_bag_values[1], split_bag_values[2]]
                        new_roots.append(bag)
                        all.append(bag)

        if not new_roots:
            break
        roots = new_roots
    output_2 = 0

    for value in all:
        output_2 += value[0]

    print(output_2)


# PART 1

First()

# PART 2

Second()
