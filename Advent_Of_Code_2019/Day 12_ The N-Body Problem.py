def update_gravity(update_position):
    actual_position = update_position.copy()
    for j in range(4):
        for i in range(4):
            if actual_position['x%d' % j] > actual_position['x%d' % i]:
                update_position['x%d' % j] -= 1
            elif actual_position['x%d' % j] < actual_position['x%d' % i]:
                update_position['x%d' % j] += 1
            if actual_position['y%d' % j] > actual_position['y%d' % i]:
                update_position['y%d' % j] -= 1
            elif actual_position['y%d' % j] < actual_position['y%d' % i]:
                update_position['y%d' % j] += 1
            if actual_position['z%d' % j] > actual_position['z%d' % i]:
                update_position['z%d' % j] -= 1
            elif actual_position['z%d' % j] < actual_position['z%d' % i]:
                update_position['z%d' % j] += 1
    return update_position


def calculate_velocity(update_position, actual_position):
    vel_xyz = dict()
    for j in range(4):
        vel_xyz['x%d' % j] = update_position['x%d' % j] - actual_position['x%d' % j]
        vel_xyz['y%d' % j] = update_position['y%d' % j] - actual_position['y%d' % j]
        vel_xyz['z%d' % j] = update_position['z%d' % j] - actual_position['z%d' % j]
    return vel_xyz


def add_velocity(update_position, vel):
    for j in range(4):
        update_position['x%d' % j] += vel['x%d' % j]
        update_position['y%d' % j] += vel['y%d' % j]
        update_position['z%d' % j] += vel['z%d' % j]
    return update_position


def calculate_energy(update_position, vel):
    all_energy = 0
    for j in range(4):
        kinematic_energy = 0
        potential_energy = 0
        kinematic_energy = abs(vel['x%d' % j]) + abs(vel['y%d' % j]) + abs(vel['z%d' % j])
        potential_energy = abs(update_position['x%d' % j]) + abs(update_position['y%d' % j]) + abs(
            update_position['z%d' % j])
        print(kinematic_energy * potential_energy)
        all_energy += kinematic_energy * potential_energy
    print(all_energy)


def main():
    moons_positions_update = dict(x0=5, y0=13, z0=-3, x1=18, y1=-7, z1=13, x2=16, y2=3, z2=4, x3=0,
                                  y3=8, z3=8)
    # PART 1
    steps = 1000
    actual_position = moons_positions_update.copy()
    sum_of_potential_energy = 0
    vel_xyz = dict()
    for i in range(0, steps):
        vel_xyz = calculate_velocity(moons_positions_update, actual_position)
        actual_position = moons_positions_update.copy()
        update_gravity(moons_positions_update)
        add_velocity(moons_positions_update, vel_xyz)
    vel_xyz = calculate_velocity(moons_positions_update, actual_position)
    calculate_energy(moons_positions_update, vel_xyz)


main()
