import  time

start = time.time()
# PART 1
ans_1 = 0
for number in range(206938, 679128 + 1):
    digits = [int(x) for x in str(number)]
    pair_condition = any([digits[i] == digits[i + 1] for i in range(len(digits) - 1)])
    if pair_condition:
        decrease_condition = any([digits[i] > digits[i + 1] for i in range(len(digits) - 1)])
        if not decrease_condition:
            ans_1 += 1
print(ans_1)

# PART 2

ans_2 = 0
for number in range(206938, 679128 + 1):
    digits = [int(x) for x in str(number)]
    pair_condition = any([(i == 0 or digits[i] != digits[i - 1]) and digits[i] == digits[i + 1] and (
            i == len(digits) - 2 or digits[i] != digits[i + 2]) for i in range(len(digits) - 1)])
    if pair_condition :
        decrease_condition = any([digits[i] > digits[i + 1] for i in range(len(digits) - 1)])
        if not decrease_condition:
            ans_2 += 1
print(ans_2)

end = time.time()
print("time", end - start)