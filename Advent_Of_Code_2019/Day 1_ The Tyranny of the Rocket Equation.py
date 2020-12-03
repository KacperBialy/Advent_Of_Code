import time

# PART 1

modules_mass = [106947, 129138, 56893, 75116, 96763, 108475, 62574, 137915, 73556, 69652, 74098, 131265, 77267, 72940,
                74859, 128578, 128024, 125887, 140457, 97314, 126150, 148019, 116715, 54231, 98892, 73242, 131621,
                122572, 107437, 75142, 103755, 141267, 141024, 80452, 60619, 104099, 51541, 63863, 106932, 75346, 77073,
                57263, 128967, 124504, 79388, 124167, 100073, 97108, 74180, 137778, 73793, 131458, 67579, 102695,
                143794, 96093, 64490, 96122, 88901, 53381, 77850, 96527, 51943, 107511, 120126, 64622, 63053, 116916,
                83990, 143278, 72390, 101767, 135915, 126354, 109714, 56139, 129849, 89505, 115213, 145001, 56506,
                83700, 59071, 80895, 143177, 120738, 78270, 100436, 108389, 62456, 145335, 102210, 111779, 95937, 52626,
                134932, 61925, 97086, 50211, 96413]


def calculate_fuel():
    fuel_calc = 0
    for module_mass in modules_mass:
        fuel_calculation = module_mass / 3 - 2
        fuel_calculation = int(fuel_calculation)
        fuel_calc += fuel_calculation
    return fuel_calc


def calculate_fuel_fuel(module_mass):
    fuel_calc = module_mass / 3 - 2
    fuel_calc = int(fuel_calc)
    return fuel_calc


# PART 1
print(calculate_fuel())

# PART 2
if __name__ == "__main__":
    start = time.time()
    all_fuel_fuel = 0
    for module_mass in modules_mass:
        all_fuel = 0
        fuel = calculate_fuel_fuel(module_mass)
        while fuel > 0:
            all_fuel += fuel
            fuel = calculate_fuel_fuel(fuel)
        all_fuel_fuel += all_fuel
    print(all_fuel_fuel)
    stop = time.time()
    print("time : ", stop - start)
