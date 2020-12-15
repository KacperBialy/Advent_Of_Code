def CreateData():
    with open('./input_data/day12.txt', mode='r') as file:
        data = file.read().split('\n')

    commands = []

    for command in data:
        key_val = [command[0], int(command[1:])]
        commands.append(key_val)

    directions = [False, True, False, False]  # N E S W

    return commands, directions


def command_L_R(command, val, directions):
    gain = 1
    if command == 'L':
        gain = -1
    for [i, direction] in enumerate(directions):
        if direction:
            directions[i] = False
            if (i * 90 + gain * val) % 360 == 0:
                directions[0] = True
            if (i * 90 + gain * val) % 360 == 90:
                directions[1] = True
            if (i * 90 + gain * val) % 360 == 180:
                directions[2] = True
            if (i * 90 + gain * val) % 360 == 270:
                directions[3] = True
            break


def command_waypoint_L_R(command, val, waypoints):
    new_waypoints = [0, 0, 0, 0]
    gain = -1
    if command == 'L':
        gain = 1
    for i in range(len(waypoints)):
        if val == 90:
            for j in range(4):
                new_waypoints[j] = waypoints[(j + gain) % 4]
        if val == 180:
            for j in range(4):
                new_waypoints[j] = waypoints[(j + 2 * gain) % 4]
        if val == 270:
            for j in range(4):
                new_waypoints[j] = waypoints[(j + 3 * gain) % 4]
        break
    return new_waypoints


def First():
    position = [0, 0, 0, 0]
    [commands, directions] = CreateData()
    for key, val in commands:
        if key == 'F':
            for i, direction in enumerate(directions):
                if direction:
                    position[i] += val
        if key == 'R':
            command_L_R(key, val, directions)
        if key == 'L':
            command_L_R(key, val, directions)
        if key == 'N':
            position[0] += val
        if key == 'E':
            position[1] += val
        if key == 'S':
            position[2] += val
        if key == 'W':
            position[3] += val
    ew = abs(position[0] - position[2])
    ns = abs(position[1] - position[3])
    print(ew + ns)


def Second():
    position = [0, 0, 0, 0]
    way_point = [1, 10, 0, 0]
    [commands, directions] = CreateData()
    for key, val in commands:
        if key == 'F':
            for i, direction in enumerate(directions):
                if direction:
                    for [i, val_waitpoint] in enumerate(way_point):
                        position[i] += val * val_waitpoint
        if key == 'R':
            way_point = command_waypoint_L_R(key, val, way_point)
        if key == 'L':
            way_point = command_waypoint_L_R(key, val, way_point)
        if key == 'N':
            way_point[0] += val
        if key == 'E':
            way_point[1] += val
        if key == 'S':
            way_point[2] += val
        if key == 'W':
            way_point[3] += val
        print(way_point)
    ew = abs(position[0] - position[2])
    ns = abs(position[1] - position[3])
    print(ew + ns)


First()

Second()
