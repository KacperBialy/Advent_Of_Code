import time

start = time.time()

A, B, _ = open("input_data/day3.txt").read().split('\n')
A, B = [x.split(',') for x in [A, B]]
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def points(data):
    x = 0
    y = 0
    length = 0
    ans = {}
    for cmd in data:
        d = cmd[0]
        n = int(cmd[1:])
        for i in range(n):
            x += DX[d]
            y += DY[d]
            length += 1
            if (x, y) not in ans:
                ans[(x, y)] = length
    return ans


if __name__ == '__main__':
    # PART 1
    PA = points(A)
    PB = points(B)
    both = set(PA.keys()) & set(PB.keys())
    ans_1 = min(abs(x) + abs(y) for (x, y) in both)
    print(ans_1)
    ans_2 = min([PA[p] + PB[p] for p in both])
    print(ans_2)

stop = time.time()
print("time : ", stop - start)
