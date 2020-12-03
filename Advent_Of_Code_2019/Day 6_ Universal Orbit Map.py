import time


def sum(value, orbits):
    ans = 0
    for y in orbits.get(value, []):
        ans += sum(y, orbits)
        ans += 1
    return ans


if __name__ == '__main__':
    start = time.time()
    orbits = {}
    for line in open("./input_data/day6.txt").readlines():
        a, b = line.strip().split(")")
        if a not in orbits:
            orbits[a] = []
        orbits[a].append(b)
    print(orbits)
    summary = 0
    for x in orbits:
        summary += sum(x, orbits)
        print(summary)
    print(summary)
    stop = time.time()
    print("time", stop - start)
